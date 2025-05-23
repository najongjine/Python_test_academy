from pytube import YouTube

url = 'https://www.youtube.com/watch?v=kPa7bsKwL-c'

yt=YouTube(url)
strem=yt.streams.get_highest_resolution()

strem.download()
print(f"{yt.title} 영상이 다운로드 되었씁니다")