
# Youtube Video Converter & Transcriber

There are many of us out there who would prefer to listen to audio rather than sit down and watch a YouTube video clip. And this has nothing to do with the video itself; it is just that getting time for that might be a little bit hard. It is for this reason, and many more others, that individuals prefer to convert YouTube videos to mp3 using services such as YouTube converter kostenlos or any other. But have you ever asked yourself why people would like to convert videos to mp3? Read on to find out some of the benefits.

In addition to that, many times users need to get the transcription of a given audio. Instead of downloading audio then upload it agan into a transcription platform, it is better to have a solution that perfom the two tasks in the same time. which allows the user to gain time, energy and avoid annoying websites with ads.
Our solution comes to respond to this need.

The website offers a youtube video converter to MP3 and WAV audio formats. In addition to that, transcription can be performed with two languages (french, and english).
All this is for free and without ads. 

The website comes with a simple design which is reponsive and multiplatform. 


## Requirements

The app was built using Python:

* Flask which is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

It does have many cool features like url routing, template engine. It is a WSGI web app framework.

* Youtube DLP: yt-dlp is a youtube-dl fork based on the now inactive youtube-dlc. The main focus of this project is adding new features and patches while also keeping up to date with the original project. (https://github.com/yt-dlp/yt-dlp)
* Pydub: pydub is a Python library to work with only . wav files. By using this library we can play, split, merge, edit our . wav audio files.
* speechrecognition: Library for performing speech recognition, with support for several engines and APIs, online and offline.

## Run Locally

Clone the project

```bash
  git clone https://github.com/isbainemohamed/youtube-downloader.git
```

Go to the project directory

```bash
  cd youtube-downloader
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server: 

*In the Integrated Terminal, run the app by entering python -m flask run, which runs the Flask development server. The development server looks for app.py by default. When you run Flask, you should see output similar to the following:*

```bash
  python -m flask run
```

Then you can access to the app via : http://127.0.0.1:5000 
(by default the app runs on port 5000)



## Features

- Simple Design/responsive
- Cross platform


## Demo

To try the app by your self , please visit: 
https://youtubevideotranscriber.herokuapp.com/

Here is the landing page:

![Logo](https://github.com/isbainemohamed/youtube-downloader/blob/5930b9e16989bb6f5e838ab18e8429a74200aaf7/demo_images/Screenshot%202022-08-19%20at%2022-45-12%20Convert%20Youtube%20Video%20to%20Audio%20&%20Text.png)

Copy the Youtube link in the input field:

![Logo](https://github.com/isbainemohamed/youtube-downloader/blob/e57b5caea7c762045e7bcb0d5a9a6405ff77d340/demo_images/Screenshot%202022-08-19%20at%2022-46-17%20Convert%20Youtube%20Video%20to%20Audio%20&%20Text.png)

select audio format (wav of mp3):

![Logo](https://github.com/isbainemohamed/youtube-downloader/blob/e57b5caea7c762045e7bcb0d5a9a6405ff77d340/demo_images/select_format.png)

click on process and wait for conversion to complete

![Logo](https://github.com/isbainemohamed/youtube-downloader/blob/e57b5caea7c762045e7bcb0d5a9a6405ff77d340/demo_images/down%20page.png)

Then, download your file by clicking on the Download button 

The audio file will be downloaded like this:

![Logo](https://github.com/isbainemohamed/youtube-downloader/blob/e57b5caea7c762045e7bcb0d5a9a6405ff77d340/demo_images/downloaded%20audio.png)

If you want to perform a transcription, select the transcription checkbox and select transcription language:

![Logo](https://github.com/isbainemohamed/youtube-downloader/blob/e57b5caea7c762045e7bcb0d5a9a6405ff77d340/demo_images/with%20transcription.png)

Your transcription will be generated as follows

![Logo](https://github.com/isbainemohamed/youtube-downloader/blob/e57b5caea7c762045e7bcb0d5a9a6405ff77d340/demo_images/transcription%20generated.png)

and you can download it as a txt file
![Logo](https://github.com/isbainemohamed/youtube-downloader/blob/e57b5caea7c762045e7bcb0d5a9a6405ff77d340/demo_images/final.png)



## API Reference

The API is under developement (will be released very soon)

## Feedback

If you have any feedback, please reach out to us at isbainemouhamed@gmail.com or labrijisaad@gmail.com


## FAQ

#### What is the maximum video duration can I convert ?

    There is no limitation, you can convert very large videos !

#### What is the maximum video duration I can transcribe ?

    It's better to not exceed 5 minutes !

#### What are supported audio formats?

    you can download MP3 or WAV audios from our platform !


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## 🚀 About Me
I'm a data engineer ...


## Roadmap

- Additional browser support

- Improve speech recognition

- Increase processing speed


## License

[INPT](INPT)

