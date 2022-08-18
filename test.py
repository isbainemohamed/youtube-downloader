import os
from pathlib import Path
from pydub import AudioSegment

import yt_dlp
#Importing library and thir function
from pydub import AudioSegment
from pydub.silence import split_on_silence
url="https://www.youtube.com/watch?v=5o9J_6RqsKc"
ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'noplaylist': True,
        'continue_dl': True,
        'outtmpl': f'./Backend/test__.mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'geobypass': True,
        'ffmpeg_location': 'C:\\ffmpeg\\bin'
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      error_code = ydl.download(url)
#reading from audio mp3 file
sound = AudioSegment.from_mp3("Backend/test__.mp3")
# spliting audio files
audio_chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40 )
#loop is used to iterate over the output list
for i, chunk in enumerate(audio_chunks):
   directory = "./Backend"
   #print("Exporting file", output_file)
   #chunk.export(output_file, format="wav")
   #Path(directory).mkdir(parents=True, exist_ok=True)
   filename = f"{i}.wav"
   chunk.export(filename, format="wav")
