
from yt_dlp import YoutubeDL

def download_video(url):
    opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True
    }
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print("✅ Yuklab olindi:", info['title'])

download_video("https://www.youtube.com/watch?v=XXXXXXXXXXX")
