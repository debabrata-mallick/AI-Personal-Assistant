import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def intro():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning")
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Night")
        speak("Good Night")
    # print("Hello sir, I am Mogalee, how may I help you?")
    # speak("Hello sir, I am moglee, how may I help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        # r.pause_threshold = 5
        energy_threshold = 300  # minimum audio energy to consider for recording
        dynamic_energy_threshold = True
        dynamic_energy_adjustment_damping = 0.15
        dynamic_energy_ratio = 1.5
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


if __name__ == "__main__":
    # intro()
    # while True:

        query = take_command().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            print("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=6)
            speak("According to Wikipedia")
            print(results)
            speak(results)

            # speak('Searching Wikipedia...')
            # query = query.replace("wikipedia", "")
            # results = wikipedia.summary(query, sentences=2) 
            # speak("According to Wikipedia")
            # print(results)
            # speak(results)
        elif 'open youtube' in query:
            print("openning youtube")
            urL = 'https://www.youtube.com'
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)
        elif 'open facebook' in query:  
            print("openning facebook")
            urL='https://www.facebook.com'
            chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)
        elif 'play music' in query:
            print("playing music")
            music_dir = 'H:\\Collection\\Mann'  # Path of directory.
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play video' in query:
            print("playing video")
            video_dir = 'H:\\Movies\\Mum.Bhai.S01E01-12.Zee5.WebDL.720p.Hindi.AAC.2.0.x264.ESub-InextMovies'  # Path of directory.
            videos = os.listdir(video_dir)
            # print(videos)
            os.startfile(os.path.join(video_dir, videos[0]))
        elif 'open gallery' in query:
            print("openning gallery")
            path = 'C:\\Users\\MUNNA\\Pictures\\scan 15-09-17\\POST office'  # Path of directory.
            items = os.listdir(path)
            # print(items)
            os.startfile(os.path.join(path, items[0]))
            # print(items[0])
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {str_time}")
            print(str_time)

        elif 'open code' in query:
            print("openning vs code")
            code_path = "C:\\Users\\MUNNA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Go to desktop code icon -> Right click -> property -> copy target and paste inside double quots
            os.startfile(code_path)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "munnapaswan135@gmail.com"
                send_email(to, content)
                speak("mail has been sent!")
            except Exception as e:
                print(e)
                speak("sorry")
        elif 'resolution algorithm' in query:
            path = 'E:\\1 IIT Bombay\\Spring Semester Cources\\CS 621\\project\\project_name\\app_name1\\file.txt'
            content = open(path, "r+")
            # print(content.read())
            for i in range(110):
                print(content.readline())
            print(content.readline())
            content.close()
        else:
            exit()

