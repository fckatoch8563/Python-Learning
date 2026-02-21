import json
import os
import shutil
import subprocess
import time
import urllib.request

from yt_dlp import YoutubeDL

DEFAULT_SPEED_TEST_URL = "http://ipv4.download.thinkbroadband.com/10MB.zip"
MAX_TEST_BYTES = 5 * 1024 * 1024
SPEED_CACHE_PATH = os.path.join("downloads", ".speed_cache.json")


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
    os.makedirs(os.path.dirname(SPEED_CACHE_PATH), exist_ok=True)
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


def resolve_ffmpeg_path() -> str | None:
    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path:
        return ffmpeg_path
    manual_path = input(
        "ffmpeg not found. Enter full path to ffmpeg.exe (Enter to skip): "
    ).strip()
    if not manual_path:
        return None
    if os.path.isfile(manual_path) and manual_path.lower().endswith("ffmpeg.exe"):
        return manual_path
    print("Invalid ffmpeg path; skipping MP3 conversion.")
    return None


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
        with open(config_file, "w", encoding="utf-8") as f:
            f.write(config_content)
    except OSError as e:
        print(f"Warning: Could not write yt-dlp config: {e}")


def download_with_ytdlp_api(url: str, format_selector: str, outtmpl: str) -> str | None:
    """Download using YoutubeDL API with merged output."""
    ydl_opts = {
        "format": format_selector,
        "outtmpl": outtmpl,
        "noplaylist": True,
        "quiet": False,
    }

    # Only enable merge_output_format if format selector contains '+' (merging requirement)
    if "+" in format_selector:
        ydl_opts["merge_output_format"] = "mp4"

    try:
        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=True)
            if result:
                return ydl.prepare_filename(result)
        return None
    except Exception as e:
        print(f"Download error: {e}")
        return None


def extract_info_with_ytdlp_api(url: str) -> dict:
    """Extract video info using YoutubeDL API."""
    ydl_opts = {
        "noplaylist": True,
        "quiet": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)
    except Exception as e:
        print(f"Extract info error: {e}")
        return {}


url = input("Enter the YouTube video URL: ")

try:
    download_type = (
        input("Download type (video/audio, Enter for video): ").strip().lower()
    )
    if download_type and download_type not in {"video", "audio"}:
        raise RuntimeError("Invalid download type. Use 'video' or 'audio'.")
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    js_runtime = resolve_js_runtime()
    if not js_runtime:
        print("Info: No JS runtime found, using standard format selector.")
    else:
        print(f"Using JS runtime: {js_runtime}")
        create_ytdlp_config(js_runtime)

    info = extract_info_with_ytdlp_api(url)

    if download_type == "audio":
        formats = [
            fmt for fmt in info.get("formats", []) if fmt.get("vcodec") == "none"
        ]
        if not formats:
            raise RuntimeError("No audio-only streams found for this video.")

        formats.sort(
            key=lambda fmt: fmt.get("abr") or fmt.get("tbr") or 0, reverse=True
        )
        print("Available audio options:")
        for index, fmt in enumerate(formats, start=1):
            size_bytes = fmt.get("filesize") or fmt.get("filesize_approx") or 0
            size_mb = size_bytes / (1024 * 1024)
            label = fmt.get("abr") or fmt.get("tbr")
            label_text = f"{label} kbps" if label else "unknown bitrate"
            ext = fmt.get("ext") or "unknown"
            print(f"{index}. {label_text} - {ext} - {size_mb:.1f} MB")

        choice = input("Choose an audio option by number (Enter for best): ").strip()
    else:
        manual_select = (
            input("Select resolution manually? (y/N): ").strip().lower() == "y"
        )
        if manual_select:
            formats = [
                fmt
                for fmt in info.get("formats", [])
                if fmt.get("vcodec") != "none" and fmt.get("ext") == "mp4"
            ]
            if not formats:
                raise RuntimeError(
                    "No compatible MP4 video stream found for this video."
                )

            combined_formats = [fmt for fmt in formats if fmt.get("acodec") != "none"]
            display_formats = combined_formats or formats
            if not combined_formats:
                print(
                    "No combined video+audio streams found. Will merge audio if needed."
                )

            display_formats.sort(key=lambda fmt: fmt.get("height") or 0, reverse=True)
            print("Available resolutions:")
            for index, fmt in enumerate(display_formats, start=1):
                size_bytes = fmt.get("filesize") or fmt.get("filesize_approx") or 0
                size_mb = size_bytes / (1024 * 1024)
                height = fmt.get("height")
                label = f"{height}p" if height else "unknown"
                has_audio = fmt.get("acodec") != "none"
                audio_label = "with audio" if has_audio else "video only"
                print(f"{index}. {label} - {audio_label} - {size_mb:.1f} MB")

            choice = input(
                "Choose a resolution by number (Enter for highest): "
            ).strip()
        else:
            display_formats = []
            choice = ""

    if not manual_select or not display_formats:
        selected_format = None
    elif choice:
        try:
            selected_index = int(choice) - 1
            selected_format = display_formats[selected_index]
        except (ValueError, IndexError) as exc:
            raise RuntimeError("Invalid resolution choice.") from exc
    else:
        selected_format = display_formats[0]

    size_bytes = 0
    if selected_format is not None:
        size_bytes = (
            selected_format.get("filesize")
            or selected_format.get("filesize_approx")
            or 0
        )
    if size_bytes:
        auto_speed = (
            input("Auto-detect download speed for time estimate? (y/N): ")
            .strip()
            .lower()
        )
        speed_mbps = None
        if auto_speed == "y":
            cached_speed = load_cached_speed()
            if cached_speed is not None:
                use_cached = (
                    input(f"Use cached speed {cached_speed:.1f} Mbps? (Y/n): ")
                    .strip()
                    .lower()
                )
                if use_cached in {"", "y", "yes"}:
                    speed_mbps = cached_speed
            test_url = input(f"Speed test URL (Enter for default): ").strip()
            if not test_url:
                test_url = DEFAULT_SPEED_TEST_URL
            try:
                if speed_mbps is None:
                    speed_mbps = measure_download_speed(test_url, MAX_TEST_BYTES)
                    save_cached_speed(speed_mbps)
                    print(f"Estimated speed: {speed_mbps:.1f} Mbps")
            except Exception as exc:
                print(f"Speed test failed: {exc}")
        if speed_mbps is None:
            speed_input = input(
                "Enter your download speed in Mbps for time estimate (Enter to skip): "
            ).strip()
            if speed_input:
                try:
                    speed_mbps = float(speed_input)
                    if speed_mbps <= 0:
                        raise ValueError
                except ValueError:
                    print("Invalid speed input. Skipping time estimate.")
                    speed_mbps = None
        if speed_mbps:
            seconds = (size_bytes * 8) / (speed_mbps * 1_000_000)
            minutes = seconds / 60
            if minutes >= 1:
                print(f"Estimated download time: {minutes:.1f} minutes")
            else:
                print(f"Estimated download time: {seconds:.0f} seconds")
    else:
        print("File size unknown; skipping time estimate.")

    filename = input(
        "Enter filename without extension (Enter to keep default): "
    ).strip()
    if filename:
        outtmpl = os.path.join(output_dir, f"{filename}.%(ext)s")
    else:
        outtmpl = os.path.join(output_dir, "%(title)s.%(ext)s")

    if download_type == "video":
        if selected_format is None:
            # Use 'best' which prefers combined formats, avoiding merge issues
            format_selector = "best"
        else:
            format_id = selected_format.get("format_id")
            if selected_format.get("acodec") == "none":
                # Use 'best' as fallback to find combined formats
                format_selector = "best"
            else:
                format_selector = format_id
    else:
        if selected_format is None:
            format_selector = "best"
        else:
            format_selector = selected_format.get("format_id")

    print(f"Downloading with format: {format_selector}")
    file_path = download_with_ytdlp_api(url, format_selector, outtmpl)

    if not file_path:
        print("Download failed - no file path returned")

    if download_type == "video":
        ffmpeg_path = resolve_ffmpeg_path()
        if file_path:
            print(f"Downloaded file path: {file_path}")
        else:
            print("Download completed but file not found.")
            raise RuntimeError("Downloaded file not found in downloads folder.")
        if ffmpeg_path and file_path and os.path.isfile(file_path):
            try:
                probe = subprocess.run(
                    [ffmpeg_path, "-i", file_path],
                    capture_output=True,
                    text=True,
                )
                print("ffmpeg stream info:")
                print(probe.stderr.strip() or "(no stream info)")
            except Exception as exc:
                print(f"ffmpeg probe failed: {exc}")
            root, ext = os.path.splitext(file_path)
            aac_path = f"{root}_aac{ext}"
            try:
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
                )
                if result.returncode != 0:
                    print("AAC re-encode failed:")
                    print(result.stderr.strip() or "(no stderr output)")
                else:
                    os.replace(aac_path, file_path)
                    print(f"AAC re-encoded video saved to: {file_path}")
            except Exception as exc:
                print(f"AAC re-encode failed: {exc}")

    if download_type == "audio":
        convert = input("Convert to MP3 with ffmpeg? (y/N): ").strip().lower()
        if convert == "y":
            ffmpeg_path = resolve_ffmpeg_path()
            if ffmpeg_path:
                mp3_path = os.path.splitext(file_path)[0] + ".mp3"
                try:
                    subprocess.run(
                        [ffmpeg_path, "-y", "-i", file_path, "-q:a", "0", mp3_path],
                        check=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                    )
                    print(f"MP3 saved to: {mp3_path} (VBR quality: ~245 kbps)")
                except Exception as exc:
                    print(f"MP3 conversion failed: {exc}")
    print("Download completed!")
except Exception as exc:
    print(f"Download failed: {exc}")


# streamlit run streamlit_app.py
