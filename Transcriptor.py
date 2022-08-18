import yt_dlp
import time
import re
import os
from pydub import AudioSegment
import speech_recognition as sr
import math
from tqdm import tqdm
import time
from threading import Thread
import shutil
from datetime import datetime
from pytube import YouTube

#url = "https://www.youtube.com/watch?v=QGpmnA2JJ4U&ab_channel=VOALearningEnglish"


def get_video(url,format):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
    video_title = info_dict['title']
    yt = YouTube(url)
    video_title_=yt.title
    video_id=info_dict["id"]
    if video_title_ in video_title or video_title in video_title_:
        video_id=info_dict["id"]
        video_name = re.sub('[\\\\/*?:"<>|]', '', video_title)
        name = video_name
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'noplaylist': True,
            'continue_dl': True,
            'outtmpl': f'./{video_id}.{format}',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': f'{format}',
                'preferredquality': '192',
            }],
            'geobypass': True,
            'ffmpeg_location': 'C:\\ffmpeg\\bin'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(url)
        path = f"./{video_id}.{format}"
        return path,name,video_id
    else:
        stream=yt.streams.filter(only_audio=True)
        video_name = re.sub('[\\\\/*?:"<>|]', '', video_title_)
        name = video_name
        #stream.download()
        # to set the name of the file
        yt.set_filename(video_id)
        SAVE_PATH=f'./{video_id}.{format}'
        # get the video with the extension and
        # resolution passed in the get() function
        #d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
        try:
            # downloading the video
            stream.download(SAVE_PATH)
        except:
            print("Some Error!")
        print('Task Completed!')
        return SAVE_PATH, name, video_id

class SplitWavAudioMubin():
    def __init__(self, file_path,video_id,format):
        print("heeeeeeeeeere |||||||||||||||||||| is format")
        print(format)
        self.filepath = file_path
        self.video_id=video_id
        if format=="mp3":
            self.audio = AudioSegment.from_mp3(self.filepath)
        elif format=="wav":
            self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        print("here is split_filenmae")
        print(os.getcwd())
        print(split_filename)
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(split_filename, format="wav")

    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        dt = datetime.now()
        ts = str(datetime.timestamp(dt)).split(".")
        stamp="".join(ts)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i)+"_"+self.video_id +"_"+stamp+".wav"
            print("<<<<<<<<<<<<<<<<<<<<<<<",split_fn)
            self.single_split(i, i + min_per_split, split_fn)
            if i == total_mins - min_per_split:
                print('All splited successfully')
        print('>>> Video duration: ' + str(self.get_duration()))
        return self.video_id,stamp


def split_audio(file_path,video_id,format):
    print('""""""""""""""""')
    print(file_path)
    split_wav = SplitWavAudioMubin(file_path,video_id,format)
    stamp=split_wav.multiple_split(min_per_split=1)[1]
    return stamp


def sort_chunks(video_id,stamp,search_dir="./"):
    # Iterate directory
    files=[]
    for path in os.listdir(search_dir):
        # check if current path is a file
        if os.path.isfile(os.path.join(search_dir, path)):
            if stamp in path and video_id in path:
                files.append(os.path.join(search_dir, path))
    files.sort(key=lambda x: os.path.getmtime(x))
    print("HEEEEEEEEEREEEEEEEEEE FILESSSSSSSSS")
    print(files)
    return files


def speech_recognizer(files, lang):
    texts = []
    recognizer = sr.Recognizer()

    for file in tqdm(files):
        with sr.AudioFile(file) as source:
            recorded_audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(
                recorded_audio,
                language=lang  ## Replace with language keyword
            )
            texts.append(text)
        except Exception as ex:
            print(ex)
    result = ""
    for text in texts:
        result += " " + text

    return result



def speech_recognizer(files,lang, frames, i):
    texts = []
    recognizer = sr.Recognizer()

    for file in tqdm(files):
        with sr.AudioFile(file) as source:
            recorded_audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(
                recorded_audio,
                language=lang  ## Replace with language keyword
            )
            texts.append(text)
        except Exception as ex:
            print(ex)
    result = ""
    for text in texts:
        result += " " + text
    frames[i] = result
    return result

def split_files(files, n_batches):
    k, m = divmod(len(files), n_batches)
    return list(files[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n_batches))

def main(url,format,isTr,lang,n_batches=4):
    #url = "https://www.youtube.com/watch?v=9HOVCQDDV1I"
    path, name,video_id = get_video(url,format)
    if isTr=="on":
        print("=========== With Transcription =============")
        print(path)
        print(os.getcwd())
        stamp=split_audio(path,video_id, format)
        print(stamp)
        files = sort_chunks(video_id, stamp, "/")
        threads = [None]*n_batches
        frames = [None]*n_batches
        batches = split_files(files, n_batches)
        start = 0
        for i in range(len(batches)):
            if i>0:
                start_index=len(batches[i-1])
            else:
                start_index = 0
            t = Thread(target=speech_recognizer, args=(batches[i],lang, frames, i))
            threads[i] = t
            t.start()
        for t in threads:
            t.join()
        return frames,name,video_id,files
    else:
        return None,name,video_id,None
def write_output(result,video_id):
    #os.chdir("/")
    text_file = open("./Transcription_" + video_id + ".txt", "w")
    text_file.write(result)
    text_file.close()
    return "./Transcription_" + video_id + ".txt"


def delete_temp(files):
    for path in files:
        os.remove(path)

def run(url,isTr,lang,format,n_batches=4):
    start = time.time()
    response_body={}
    frames,name,video_id,files = main(url,format,isTr,lang,n_batches)
    # end time
    end = time.time()
    print(frames)
    result = ""
    if frames!=None:
        for frame in frames:
            result += " " + frame
        out=write_output(result, video_id)
        print(os.getcwd())
        if files!=None:
            delete_temp(files)
        #shutil.rmtree(f'/Temporary files/Splited{name}')
    # total time taken
        print(f"Runtime of the transcription  is {end - start} second")
        print(f"output at {out}")
        response_body["id"]=video_id
        #response_body["path_to_transcription"] = f"/Backend/Temp/{video_id}.txt"
        response_body["isTrans"] = True
        response_body["format"] = format
        response_body["video_name"] = name
        return response_body
    elif frames==None:
        response_body["id"] = video_id
        response_body["video_name"]=name
        response_body["format"]=format
        response_body["isTrans"] = False
        return response_body

