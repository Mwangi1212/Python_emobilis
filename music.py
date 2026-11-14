import yt_dlp

 

ydl_opts = {

    'format': 'bestaudio/best',
    'ffmpeg_location': '/usr/bin/ffmpeg',
'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
}]
        }


 

with yt_dlp.YoutubeDL(ydl_opts) as ydl:

  ydl.download(['https://youtu.be/_VZbqyollBo'])