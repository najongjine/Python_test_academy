# pip install yt_dlp

from yt_dlp import YoutubeDL

def download_video(url):
    ydl_opts = {
        'format': 'bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url="https://www.youtube.com/watch?v=AF0Lfs6vs_U"
download_video(url)