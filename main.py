
# importing packages
from pytube import YouTube
from pathlib import Path
import os
import yt_dlp

# url input from user



uri = input("Enter the URL of the video you want to download: \n>> ")
filename = input("Enter the name you want to save the video as: \n>> ")
Path().mkdir(
    parents=True, exist_ok=True)

print("Downloading the backgrounds audio... please be patient 🙏 ")
print(f"Downloading {filename} from {uri}")
ydl_opts = {
    "outtmpl": f"./{filename}.mp3",
    "format": "bestaudio/best",
    "extract_audio": True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([uri])

# result of success
print(filename+ " has been successfully downloaded.")
