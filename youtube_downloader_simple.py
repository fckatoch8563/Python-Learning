"""Simple Streamlit YouTube Downloader using yt-dlp."""

import os
import shutil
import subprocess
from typing import Any

import streamlit as st
from yt_dlp import YoutubeDL

DOWNLOAD_DIR = "downloads"


def download_with_progress(url: str, format_id: str, outtmpl: str) -> str:
    """Download using yt-dlp and update Streamlit progress."""
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

    ydl_opts = {
        "format": format_id,
        "outtmpl": outtmpl,
        "noplaylist": True,
        "quiet": True,
        "progress_hooks": [hook],
    }
    if "+" in format_id:
        ydl_opts["merge_output_format"] = "mp4"

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(result)


def convert_to_mp3(file_path: str, keep_source: bool) -> str | None:
    """Convert audio file to MP3 using ffmpeg."""
    ffmpeg_path = shutil.which("ffmpeg")
    if not ffmpeg_path:
        st.warning("ffmpeg not found. Install: winget install FFmpeg")
        return None

    mp3_path = os.path.splitext(file_path)[0] + ".mp3"
    try:
        result = subprocess.run(
            [ffmpeg_path, "-y", "-i", file_path, "-q:a", "0", mp3_path],
            capture_output=True,
            text=True,
            timeout=300,
        )
        if result.returncode != 0:
            st.error(f"MP3 conversion failed: {result.stderr[:300]}")
            return None
        if not keep_source:
            try:
                os.remove(file_path)
            except OSError:
                pass
        return mp3_path
    except subprocess.TimeoutExpired:
        st.error("MP3 conversion timed out (5+ minutes)")
        return None
    except Exception as exc:
        st.error(f"MP3 conversion failed: {exc}")
        return None


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
    st.info("Format selection is not available in the simple version.")

with speed_tab:
    st.info("Speed tools are not available in the simple version.")

with advanced_tab:
    convert_audio = st.checkbox("Convert audio to MP3 (ffmpeg)", value=False)
    keep_source_audio = st.checkbox("Keep original audio after MP3", value=False)

if st.button("Download", use_container_width=True):
    if not url.strip():
        st.warning("Please enter a YouTube URL.")
        st.stop()

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    if filename:
        outtmpl = os.path.join(DOWNLOAD_DIR, f"{filename}.%(ext)s")
    else:
        outtmpl = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")

    format_id = "best" if mode == "video" else "bestaudio/best"

    try:
        file_path = download_with_progress(url.strip(), format_id, outtmpl)
        st.success(f"Downloaded: {file_path}")
        st.caption(f"Saved to: {os.path.abspath(file_path)}")

        if mode == "audio" and convert_audio:
            mp3_path = convert_to_mp3(file_path, keep_source_audio)
            if mp3_path:
                st.success(f"MP3 saved: {mp3_path}")
    except Exception as exc:
        st.error(f"Download failed: {exc}")
