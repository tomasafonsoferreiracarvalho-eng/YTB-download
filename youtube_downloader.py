#!/usr/bin/env python3
"""
YouTube Music Downloader
Uso: python youtube_downloader.py <url>

Instalação:
    pip install yt-dlp
    (ffmpeg para converter para MP3 - https://ffmpeg.org/download.html)
"""

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Uso: python youtube_downloader.py <url>")
        print("Exemplo: python youtube_downloader.py https://youtube.com/watch?v=...")
        sys.exit(1)

    url = sys.argv[1]

    try:
        import yt_dlp
    except ImportError:
        print("A instalar yt-dlp...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        import yt_dlp

    opcoes = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    print(f"A fazer download: {url}\n")

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

    print("\nDownload completo!")

if __name__ == "__main__":
    main()
