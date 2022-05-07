import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

# All function of personal Assistance

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

class _TTS:
    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()

    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()
# end block

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def intro():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning")
        tts = _TTS()
        tts.start("Good Morning")
        del(tts)
    elif hour >= 12 and hour < 18:
        print("Good Afternoon")
        tts = _TTS()
        tts.start("Good Afternoon")
        del(tts)
    else:
        print("Good Night")
        tts = _TTS()
        tts.start("Good Night")
        del(tts)
    print("Hello sir, I am Lucifer. Your personal assistance. How may I help you?")
    msg = "Hello sir, I am Lucifer. Your personal assistance. How may I help you?"
    tts = _TTS()
    tts.start(msg)
    del(tts)
    return msg

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        # energy_threshold = 300  # minimum audio energy to consider for recording
        # dynamic_energy_threshold = True
        # dynamic_energy_adjustment_damping = 0.15
        # dynamic_energy_ratio = 1.5
        # self.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
        # self.operation_timeout = None  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

        # self.phrase_threshold = 0.3  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        # self.non_speaking_duration = 0.5
        audio = r.listen(source)

    try:
        print("               Rcognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("              ", query)
    except Exception as e:
        # print(e)
        print("Sorry say that again...")
        return "NONE"
    return query


# Enable " less secure app " in your gmail
def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('munnapaswan135@gmail.com', '9007953343')
    server.sendmail('munnapaswan135@gmail.com', to, content)
    server.close()


def wikipedia_search(query):
    print("In wikipedia function")
    print(query)
    msg = 'Searching Wikipedia'
    tts = _TTS()
    tts.start(msg)
    del(tts)
    print("searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    msg = "According to Wikipedia"
    tts = _TTS()
    tts.start(msg)
    del(tts)
    print(results)
    msg = results
    tts = _TTS()
    tts.start(msg)
    del(tts)
    return(results)

def youtube():
    print("openning youtube")
    msg = 'openning youtube'
    tts = _TTS()
    tts.start(msg)
    del(tts)
    urL = 'https://www.youtube.com'
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(urL)
        
def facebook():
    print("openning facebook")
    msg = 'openning facebook'
    tts = _TTS()
    tts.start(msg)
    del(tts)
    urL='https://www.facebook.com'
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(urL)
            
def music():
    print("playing music")
    tts = _TTS()
    tts.start("Playing music")
    del(tts)
    music_dir = 'C:\\Users\\shubh\\Desktop\\Ai Final project\\Ai Final project\\project_name\\Music'  # Path of directory.
    songs = os.listdir(music_dir)
    # print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))
       
def video():
    print("playing video")
    msg = 'playing video'
    tts = _TTS()
    tts.start(msg)
    del(tts)
    video_dir = 'H:\\Movies\\Mum.Bhai.S01E01-12.Zee5.WebDL.720p.Hindi.AAC.2.0.x264.ESub-InextMovies'  # Path of directory.
    videos = os.listdir(video_dir)
    # print(videos)
    os.startfile(os.path.join(video_dir, videos[0]))
       
def gallery():
    print("openning gallery")
    msg = 'openning gallery'
    tts = _TTS()
    tts.start(msg)
    del(tts)
    path = 'C:\\Users\\shubh\\Desktop\\Ai Final project\\Ai Final project\\project_name\\Gallery'  # Path of directory.
    items = os.listdir(path)
    # print(items)
    os.startfile(os.path.join(path, items[1]))
    # print(items[0])
        
def time():
    str_time = datetime.datetime.now().strftime("%H:%M:%S")
    # speak(f"sir, the time is {str_time}")
    msg = 'The time is ' + str_time
    tts = _TTS()
    tts.start(msg)
    del(tts)
    print(msg)
    return msg
        
def code():
    print("openning vs code")
    msg = 'openning visual studio code'
    tts = _TTS()
    tts.start(msg)
    del(tts)
    code_path = "C:\\Users\\MUNNA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Go to desktop code icon -> Right click -> property -> copy target and paste inside double quots
    os.startfile(code_path)

def mail():
    try:
        speak("What should I say?")
        content = takecommand()
        to = "munnapaswan135@gmail.com"
        send_email(to, content)
        speak("mail has been sent!")
    except Exception as e:
        print(e)
        speak("sorry")
        
def resolution():
    # path = 'E:\\1 IIT Bombay\\Spring Semester Cources\\CS 621\\project\\project_name\\app_name1\\file.txt'
    # content = open(path, "r+")
    # # print(content.read())
    # for i in range(110):
    #     print(content.readline())
    # print(content.readline())
    # content.close()
    tts = _TTS()
    tts.start("Here is the Resolution Algorithm")
    del(tts)

def website(query):
    print("openning " + query + "...")
    msg = 'openning ' + query
    tts = _TTS()
    tts.start(msg)
    del(tts)
    url = 'https://www.' + query
    print(url)
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)
