import json
import os
import shutil
import subprocess
import time
import urllib.request
from typing import Any, Callable

import streamlit as st
from yt_dlp import YoutubeDL

DOWNLOAD_DIR = "downloads"
DEFAULT_SPEED_TEST_URL = "http://ipv4.download.thinkbroadband.com/10MB.zip"
MAX_TEST_BYTES = 5 * 1024 * 1024
SPEED_CACHE_PATH = os.path.join(DOWNLOAD_DIR, ".speed_cache.json")


def resolve_ffmpeg_path() -> str | None:
    return shutil.which("ffmpeg")


def resolve_js_runtime() -> str | None:
    for runtime in ("node", "deno"):
        runtime_path = shutil.which(runtime)
        if runtime_path:
            return runtime_path
    return None


def create_ytdlp_config(js_runtime_path: str | None) -> None:
    config_dir = os.path.expanduser("~/.config/yt-dlp")
    os.makedirs(config_dir, exist_ok=True)
    config_file = os.path.join(config_dir, "config.txt")

    if js_runtime_path:
        config_content = f"--js-runtime nodejs:{js_runtime_path}\n"
    else:
        config_content = ""

    try:
        with open(config_file, "w", encoding="utf-8") as handle:
            handle.write(config_content)
    except OSError:
        pass


def measure_download_speed(test_url: str, max_bytes: int) -> float:
    start = time.perf_counter()
    downloaded = 0
    with urllib.request.urlopen(test_url, timeout=20) as response:
        while downloaded < max_bytes:
            chunk = response.read(min(256 * 1024, max_bytes - downloaded))
            if not chunk:
                break
            downloaded += len(chunk)
    elapsed = time.perf_counter() - start
    if elapsed <= 0 or downloaded <= 0:
        raise RuntimeError("Speed test failed.")
    return (downloaded * 8) / (elapsed * 1_000_000)


def load_cached_speed() -> float | None:
    if not os.path.exists(SPEED_CACHE_PATH):
        return None
    try:
        with open(SPEED_CACHE_PATH, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        speed = float(data.get("speed_mbps"))
        if speed <= 0:
            return None
        return speed
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        return None


def save_cached_speed(speed_mbps: float) -> None:
    os.makedirs(os.path.dirname(SPEED_CACHE_PATH), exist_ok=True)
    try:
        with open(SPEED_CACHE_PATH, "w", encoding="utf-8") as handle:
            json.dump({"speed_mbps": speed_mbps}, handle)
    except OSError:
        pass


def extract_info_with_ytdlp_api(url: str) -> dict:
    ydl_opts = {
        "noplaylist": True,
        "quiet": True,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)
    except Exception:
        return {}


def build_video_format_choices(info: dict) -> list[dict[str, Any]]:
    choices: list[dict[str, Any]] = []
    for fmt in info.get("formats", []):
        if fmt.get("vcodec") == "none":
            continue
        if fmt.get("ext") != "mp4":
            continue
        height = fmt.get("height") or 0
        size_bytes = fmt.get("filesize") or fmt.get("filesize_approx") or 0
        size_mb = size_bytes / (1024 * 1024) if size_bytes else 0
        has_audio = fmt.get("acodec") != "none"
        label = f"{height}p - {'with audio' if has_audio else 'video only'}"
        if size_mb:
            label += f" - {size_mb:.1f} MB"
        choices.append(
            {
                "label": label,
                "format_id": fmt.get("format_id"),
                "size_bytes": size_bytes,
                "has_audio": has_audio,
                "height": height,
            }
        )
    choices.sort(key=lambda item: item.get("height") or 0, reverse=True)
    return choices


def build_audio_format_choices(info: dict) -> list[dict[str, Any]]:
    choices: list[dict[str, Any]] = []
    for fmt in info.get("formats", []):
        if fmt.get("vcodec") != "none":
            continue
        size_bytes = fmt.get("filesize") or fmt.get("filesize_approx") or 0
        size_mb = size_bytes / (1024 * 1024) if size_bytes else 0
        abr = fmt.get("abr") or fmt.get("tbr") or 0
        ext = fmt.get("ext") or "unknown"
        label = f"{abr} kbps - {ext}"
        if size_mb:
            label += f" - {size_mb:.1f} MB"
        choices.append(
            {
                "label": label,
                "format_id": fmt.get("format_id"),
                "size_bytes": size_bytes,
                "abr": abr,
            }
        )
    choices.sort(key=lambda item: item.get("abr") or 0, reverse=True)
    return choices


def download_with_progress(
    url: str,
    format_id: str,
    outtmpl: str,
    log_callback: Callable[[str], None] | None = None,
) -> str:
    status = st.empty()
    progress = st.progress(0)

    def hook(data: dict[str, Any]) -> None:
        if data.get("status") == "downloading":
            total = data.get("total_bytes") or data.get("total_bytes_estimate")
            downloaded = data.get("downloaded_bytes")
            if total and downloaded:
                progress.progress(min(int(downloaded / total * 100), 100))
            status.write("Downloading...")
        elif data.get("status") == "finished":
            progress.progress(100)
            status.write("Download finished. Processing...")
            if log_callback:
                log_callback("Download finished. Processing...")

    ydl_opts = {
        "format": format_id,
        "outtmpl": outtmpl,
        "noplaylist": True,
        "quiet": True,
        "progress_hooks": [hook],
    }
    # Only enable merge if format selector requests multiple formats
    if "+" in format_id:
        ydl_opts["merge_output_format"] = "mp4"

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(result)
    return file_path


st.set_page_config(page_title="YouTube Downloader", page_icon="▶", layout="centered")

st.title("YouTube Downloader")
st.caption("Paste a YouTube link and download video or audio.")

basic_tab, format_tab, speed_tab, advanced_tab = st.tabs(
    ["Basic", "Format", "Speed", "Advanced"]
)

with basic_tab:
    url = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=...",
    )

    mode = st.radio("Download type", ["video", "audio"], horizontal=True)

    filename = st.text_input(
        "Filename (optional)",
        placeholder="Leave blank to use the video title",
    ).strip()

with format_tab:
    manual_select = st.checkbox("Choose format manually", value=False)
    st.session_state["manual_select"] = manual_select
    if manual_select:
        if st.button("Load formats"):
            if not url.strip():
                st.warning("Enter a URL first to load formats.")
            else:
                with st.spinner("Loading available formats..."):
                    st.session_state["format_info"] = extract_info_with_ytdlp_api(
                        url.strip()
                    )

        format_info = st.session_state.get("format_info")
        if format_info:
            if mode == "video":
                video_choices = build_video_format_choices(format_info)
                if not video_choices:
                    st.warning("No MP4 video formats found.")
                else:
                    labels = [item["label"] for item in video_choices]
                    selected_label = st.selectbox("Video format", labels)
                    selected_index = labels.index(selected_label)
                    st.session_state["selected_format"] = video_choices[selected_index]
            else:
                audio_choices = build_audio_format_choices(format_info)
                if not audio_choices:
                    st.warning("No audio-only formats found.")
                else:
                    labels = [item["label"] for item in audio_choices]
                    selected_label = st.selectbox("Audio format", labels)
                    selected_index = labels.index(selected_label)
                    st.session_state["selected_format"] = audio_choices[selected_index]

with speed_tab:
    estimate_time = st.checkbox("Estimate download time", value=False)
    st.session_state["estimate_time"] = estimate_time
    if estimate_time:
        cached_speed = load_cached_speed()
        use_cached = False
        if cached_speed:
            use_cached = st.checkbox(
                f"Use cached speed ({cached_speed:.1f} Mbps)", value=True
            )
        st.session_state["use_cached_speed"] = use_cached
        st.session_state["cached_speed"] = cached_speed
        auto_test = st.checkbox("Run speed test", value=False)
        test_url = st.text_input(
            "Speed test URL",
            value=DEFAULT_SPEED_TEST_URL,
        )
        if auto_test and st.button("Start speed test"):
            try:
                speed_mbps = measure_download_speed(test_url, MAX_TEST_BYTES)
                save_cached_speed(speed_mbps)
                st.session_state["speed_mbps_test"] = speed_mbps
                st.success(f"Estimated speed: {speed_mbps:.1f} Mbps")
            except Exception as exc:
                st.error(f"Speed test failed: {exc}")
        manual_speed = st.number_input(
            "Manual speed (Mbps)",
            min_value=0.0,
            value=0.0,
            step=1.0,
        )
        st.session_state["manual_speed"] = manual_speed

with advanced_tab:
    use_js_runtime = st.checkbox("Use JS runtime if available", value=False)
    prefer_bestvideo_audio = st.checkbox(
        "Use bestvideo+bestaudio (merge)",
        value=False,
    )
    merge_video_audio = st.checkbox(
        "Merge video+audio for video-only formats",
        value=True,
    )
    convert_to_mp3 = st.checkbox("Convert audio to MP3 (ffmpeg)", value=True)
    keep_source_audio = st.checkbox("Keep original audio after MP3", value=False)
    reencode_aac = st.checkbox("Re-encode video audio to AAC", value=False)

if st.button("Download", use_container_width=True):
    if not url.strip():
        st.warning("Please enter a YouTube URL.")
        st.stop()

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    if filename:
        outtmpl = os.path.join(DOWNLOAD_DIR, f"{filename}.%(ext)s")
    else:
        outtmpl = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")

    manual_select_state = st.session_state.get("manual_select", False)
    selected_format = st.session_state.get("selected_format")
    selected_size = 0
    if manual_select_state and selected_format:
        selected_size = selected_format.get("size_bytes") or 0

    if st.session_state.get("estimate_time", False):
        speed_mbps = None
        manual_speed = st.session_state.get("manual_speed") or 0.0
        use_cached = st.session_state.get("use_cached_speed", False)
        cached_speed = st.session_state.get("cached_speed")
        if manual_speed > 0:
            speed_mbps = manual_speed
        elif use_cached and cached_speed:
            speed_mbps = cached_speed
        else:
            speed_mbps = st.session_state.get("speed_mbps_test")
        if selected_size and speed_mbps:
            seconds = (selected_size * 8) / (speed_mbps * 1_000_000)
            minutes = seconds / 60
            if minutes >= 1:
                st.info(f"Estimated download time: {minutes:.1f} minutes")
            else:
                st.info(f"Estimated download time: {seconds:.0f} seconds")
        else:
            st.info("Time estimate needs a selected format and speed value.")

    try:
        if use_js_runtime:
            js_runtime = resolve_js_runtime()
            if js_runtime:
                create_ytdlp_config(js_runtime)
                st.caption(f"Using JS runtime: {js_runtime}")
            else:
                st.warning("No JS runtime found; continuing without it.")

        if mode == "video":
            format_id = "best"
            if manual_select_state and selected_format:
                if selected_format.get("has_audio"):
                    format_id = selected_format.get("format_id") or "best"
                elif merge_video_audio:
                    video_id = selected_format.get("format_id")
                    format_id = f"{video_id}+bestaudio/best" if video_id else "best"
                else:
                    st.warning("Selected format is video-only; using best with audio.")
            elif prefer_bestvideo_audio:
                format_id = "bestvideo+bestaudio/best"
            st.info("Downloading video (may take a moment)...")
            file_path = download_with_progress(
                url.strip(),
                format_id,
                outtmpl,
            )
            st.success(f"Downloaded: {file_path}")
            st.caption(f"Saved to: {os.path.abspath(file_path)}")

            if reencode_aac:
                ffmpeg_path = resolve_ffmpeg_path()
                if not ffmpeg_path:
                    st.warning("ffmpeg not found. Skipping AAC re-encode.")
                elif file_path and os.path.isfile(file_path):
                    root, ext = os.path.splitext(file_path)
                    aac_path = f"{root}_aac{ext}"
                    result = subprocess.run(
                        [
                            ffmpeg_path,
                            "-y",
                            "-i",
                            file_path,
                            "-c:v",
                            "copy",
                            "-c:a",
                            "aac",
                            "-b:a",
                            "192k",
                            aac_path,
                        ],
                        capture_output=True,
                        text=True,
                        timeout=300,
                    )
                    if result.returncode != 0:
                        st.error(f"AAC re-encode failed: {result.stderr[:500]}")
                    else:
                        os.replace(aac_path, file_path)
                        st.success("AAC re-encode completed.")
        else:
            format_id = "bestaudio/best"
            if manual_select_state and selected_format:
                format_id = selected_format.get("format_id") or format_id
            file_path = download_with_progress(
                url.strip(),
                format_id,
                outtmpl,
            )
            st.success(f"Audio saved: {file_path}")
            if convert_to_mp3:
                ffmpeg_path = resolve_ffmpeg_path()
                if not ffmpeg_path:
                    st.warning("ffmpeg not found. Audio saved in original format.")
                    st.stop()

                mp3_path = os.path.splitext(file_path)[0] + ".mp3"
                try:
                    result = subprocess.run(
                        [
                            ffmpeg_path,
                            "-y",
                            "-i",
                            file_path,
                            "-acodec",
                            "libmp3lame",
                            "-q:a",
                            "0",
                            mp3_path,
                        ],
                        capture_output=True,
                        text=True,
                        timeout=300,
                    )
                    if result.returncode != 0:
                        st.error(f"MP3 conversion failed: {result.stderr[:500]}")
                        st.info(f"Original audio saved: {file_path}")
                    else:
                        st.success(f"MP3 saved: {mp3_path}")
                        if not keep_source_audio:
                            try:
                                os.remove(file_path)
                            except OSError:
                                pass
                except subprocess.TimeoutExpired:
                    st.error("MP3 conversion timed out (5+ minutes)")
                except Exception as exc:
                    st.error(f"Conversion error: {str(exc)}")
    except Exception as exc:
        st.error(f"Download failed: {exc}")
