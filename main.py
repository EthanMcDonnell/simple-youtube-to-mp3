import sys
import yt_dlp


def download(url: str, filename: str) -> None:
    ydl_opts = {
        "outtmpl": f"./{filename}.%(ext)s",
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "no_warnings": True,
        "noplaylist": True,
    }

    print(f"\nDownloading: {url}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Saved → ./{filename}.mp3")


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else input("YouTube URL: ").strip()
    if not url:
        print("Error: no URL provided.")
        sys.exit(1)

    filename = input("Save as (no extension): ").strip()
    if not filename:
        print("Error: no filename provided.")
        sys.exit(1)

    try:
        download(url, filename)
    except yt_dlp.utils.DownloadError as e:
        print(f"Download failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
