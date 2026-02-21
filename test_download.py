#!/usr/bin/env python3
"""Simple test script to verify YouTube downloader audio fix."""

import os
import json
from yt_dlp import YoutubeDL


def test_download():
    url = "https://www.youtube.com/watch?v=GIFaD8jGkKE"
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    # Test format extraction first
    print("=" * 60)
    print("Step 1: Extracting available formats...")
    print("=" * 60)

    ydl_opts_info = {
        "noplaylist": True,
        "quiet": False,
    }

    try:
        with YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get("formats", [])
            print(f"\nTotal formats available: {len(formats)}")

            # Show video-only formats
            video_only = [
                f
                for f in formats
                if f.get("vcodec") != "none" and f.get("acodec") == "none"
            ]
            print(f"Video-only formats: {len(video_only)}")
            if video_only:
                fmt = video_only[0]
                print(
                    f"  Best video-only: {fmt.get('format_id')} - {fmt.get('height')}p - {fmt.get('ext')}"
                )

            # Show audio-only formats
            audio_only = [
                f
                for f in formats
                if f.get("vcodec") == "none" and f.get("acodec") != "none"
            ]
            print(f"Audio-only formats: {len(audio_only)}")
            if audio_only:
                fmt = audio_only[0]
                print(
                    f"  Best audio-only: {fmt.get('format_id')} - {fmt.get('acodec')} - {fmt.get('ext')}"
                )

            # Show combined formats
            combined = [
                f
                for f in formats
                if f.get("vcodec") != "none" and f.get("acodec") != "none"
            ]
            print(f"Combined video+audio formats: {len(combined)}")
            if combined:
                fmt = combined[0]
                print(
                    f"  Best combined: {fmt.get('format_id')} - {fmt.get('height')}p - {fmt.get('acodec')} - {fmt.get('ext')}"
                )
    except Exception as e:
        print(f"Error extracting info: {e}")
        return

    # Now test download with simpler format
    print("\n" + "=" * 60)
    print("Step 2: Downloading with combined format (18)...")
    print("=" * 60)

    format_selector = "18"  # Combined video+audio format
    outtmpl = os.path.join(output_dir, "test_video_combined.%(ext)s")

    ydl_opts_download = {
        "format": format_selector,
        "outtmpl": outtmpl,
        "noplaylist": True,
        "quiet": False,
        "progress_hooks": [progress_hook],
    }

    # Only enable merge_output_format if format selector contains '+' (merging requirement)
    if "+" in format_selector:
        ydl_opts_download["merge_output_format"] = "mp4"

    print(f"\nFormat selector: {format_selector}")
    print(f"Output template: {outtmpl}")

    try:
        with YoutubeDL(ydl_opts_download) as ydl:
            result = ydl.extract_info(url, download=True)
            if result:
                filename = ydl.prepare_filename(result)
                print(f"\n✓ Download completed: {filename}")

                # Check file info
                if os.path.exists(filename):
                    size_mb = os.path.getsize(filename) / (1024 * 1024)
                    print(f"  File size: {size_mb:.1f} MB")
    except Exception as e:
        print(f"Download error: {e}")
        import traceback

        traceback.print_exc()


def progress_hook(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "N/A")
        speed = d.get("_speed_str", "N/A")
        print(f"  {percent} at {speed}", end="\r")
    elif d["status"] == "finished":
        print(f"\n  Download phase finished: {d.get('_filename_string', 'unknown')}")
    elif d["status"] == "processing":
        print(f"  Processing: {d.get('info_dict', {}).get('ext', 'unknown')}")


if __name__ == "__main__":
    test_download()
