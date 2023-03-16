import yt_dlp

import os


def download_video_ydl(link: str) -> None:
    """
    Downloads a video from a link
    """
    os.system("yt-dlp --rm-cache-dir")
    ydl_opts = {"outtmpl": "video.mp4"}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    print("Download complete")
