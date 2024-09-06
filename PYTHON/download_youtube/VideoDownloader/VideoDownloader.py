import youtube_dl

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = input("Enter the YouTube video URL: ")
download_video(video_url)
