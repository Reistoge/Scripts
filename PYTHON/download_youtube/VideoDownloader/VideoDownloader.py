from pytube import YouTube
#pip intstall pytube
def download_video(link):
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download()  # Downloads the video
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_link = input("Enter the YouTube video URL: ")
    download_video(video_link)
