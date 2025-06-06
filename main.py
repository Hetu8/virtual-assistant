import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()

    if "open google" in command:
        speak("opening google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://youtube.com") 

    elif command.startswith("play"):
        song = command.split(" ")[1]
        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            speak(f"playing {song}")
            webbrowser.open(link)
        else: 
            speak("sorry, I couldn't find that song")    

    elif "news" in command(): 
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=38321bcf91cf43f592683d62c6c91233")
    
        if r.status_code == 200:
            # parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get("articles", [])

            #print the headlines
            for article in articles:
                speak(article['title'])

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        # Listen for the wake word "Jarvis"
        
        # Obtain audio from the microphone
        r = sr.Recognizer()
        
        # Recognize speech using Sphinx
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "hello"):
                speak("yaa")
                #listen for command
                with sr.Microphone() as source:
                    print("Hello Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"error; {0}".format(e))