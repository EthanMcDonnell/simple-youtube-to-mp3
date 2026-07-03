# youtube-to-mp3

Download YouTube videos as MP3 audio files from the terminal.

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

You'll be prompted for a YouTube URL and a filename. The MP3 is saved to the current directory.

---

**Requires:** Python 3 · [yt-dlp](https://github.com/yt-dlp/yt-dlp) · [ffmpeg](https://ffmpeg.org) (`brew install ffmpeg`)
