import yt_dlp
import os
from yt_dlp.postprocessor import FFmpegPostProcessor
#install and import the libraries requiered.
 
FFmpegPostProcessor._ffmpeg_location.set(R"C:\ffmpeg\bin") # location of the ffmpeg formatter 

# Get the absolute path to the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the output folder (subdirectory)
output_folder = os.path.join(current_directory, 'mp3_output')
# Rest of your yt-dlp code here

# Define your download options


ydl_opts = {
    'ignoreerrors': True,  # Skip over videos with errors
    'format': 'bestaudio/best',  # Download best audio quality
    'postprocessors': [{
        
        'key': 'FFmpegExtractAudio',  # Extract audio using ffmpeg
        'preferredcodec': 'mp3',  # Convert to mp3
        'preferredquality': '320',  # Set audio quality
    }],

        'outtmpl': os.path.join(output_folder, '%(title)s'),  # Set output template for downloaded files
}

# URL of the playlist you want to download

playlist_url = input("Playlist Url: ")

# Download the playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])#load the playlist with the configs
