import os

from flask import Flask, render_template, request, send_file,redirect
import Transcriptor as tr
import yt_dlp

app = Flask(__name__)
import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

app.config['UPLOAD_FOLDER'] = "./"
def check_url(url):
    try:
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
        return True
    except:
        return False


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')



@app.route("/process", methods = ["POST","GET"])
def process():  # put application's code here
    url=request.form['url']
    transcription=request.form['transcription']
    print(transcription)
    lang=request.form['language']
    format=request.form["format"]
    if check_url(url):
        response_body=tr.run(url,transcription,lang,format)
    #os.chdir("/")
        return response_body
    else:
        return {"id":"error"}

"""@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    # Appending app path to upload folder path within app root folder
    uploads = os.path.join(current_app.root_path, app.config['Backend/Temp'])
    # Returning file from appended path
    return send_from_directory(directory=uploads, filename=filename)"""

@app.route('/download',methods=['GET', 'POST'])
def download():
    data={}
    data["video_id"] = request.form['video_id']
    data["isTrans"] = str(request.form['isTrans'])
    data["video_name"]=request.form['video_name']
    data["format"] = request.form['format']
    if data["isTrans"]=="true":
        filename=app.root_path+app.config["UPLOAD_FOLDER"]+"Transcription_"+data["video_id"]+".txt"
        with open(filename) as f:
            transcription = f.readline()
        data["transcription"]=transcription
    return render_template('download.html', data=data)

@app.route("/new",methods=['GET','POST'])
def new():
    data = {}
    data["video_id"] = request.form['video_id']
    data["isTrans"] = str(request.form['isTrans'])
    data["video_name"] = request.form['video_name']
    data["format"] = request.form['format']
    audio = app.root_path + app.config["UPLOAD_FOLDER"] + data["video_id"] + "." + data["format"]
    #filename = app.root_path + app.config["UPLOAD_FOLDER"] + data["video_id"] + "." + data["format"]
    text = ""
    if data["isTrans"] == "true":
        text = app.root_path + app.config["UPLOAD_FOLDER"] + "Transcription_" + data["video_id"] + ".txt"
    try:
        os.remove(audio)
        if text != "":
            os.remove(text)
        return redirect("/")
    except:
        return redirect("/")

@app.route('/ressource/audio', methods=['GET', 'POST'])
def get_audio():
    # Appending app path to upload folder path within app root folder
    uploads = os.path.join(app.config['UPLOAD_FOLDER'])
    # Returning file from appended path
    data={}
    data["video_id"] = request.form['video_id']
    data["isTrans"] = str(request.form['isTrans'])
    data["video_name"] = request.form['video_name']
    data["format"] = request.form['format']
    attachement = data["video_name"] + "." + data["format"]
    filename=app.root_path + app.config["UPLOAD_FOLDER"] + data["video_id"] + "." + data["format"]
    print(filename)
    list_files("./")
    return send_file(filename, as_attachment=True, download_name=attachement)



@app.route('/ressource/text', methods=['GET', 'POST'])
def get_text():
    # Appending app path to upload folder path within app root folder
    uploads = os.path.join(app.config['UPLOAD_FOLDER'])
    # Returning file from appended path
    data = {}
    data["video_id"] = request.form['video_id']
    data["isTrans"] = str(request.form['isTrans'])
    data["video_name"] = request.form['video_name']
    print(uploads)
    attachement = data["video_name"] + ".txt"
    filename =app.root_path+app.config["UPLOAD_FOLDER"]+"Transcription_"+data["video_id"]+".txt"
    print("=====================")
    print(filename)
    print(os.getcwd())
    return send_file(filename, as_attachment=True, download_name6=attachement)


if __name__ == '__main__':
    app.run()

#tr.speech_recognizer()

#C:\Users\ISBAINE MOHAMED\PycharmProjects\Youtube_downloader\Backend\Temp\eOemjrWnSf8.wav
