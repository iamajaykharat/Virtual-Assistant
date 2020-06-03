import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Computer Voice is set here using sapi5 API
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 145
engine.setProperty('rate', newVoiceRate)
engine.setProperty('voice', voices[0].id)


# Computer speak here
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Computer is wishing here according to time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Sir,I am your assistant. Please tell me how can I help you")


# Computer is taking command from user(through microphone) and converting it into string
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 3000
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        print("Say that again Please....")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = "D:\\MUSIC"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime1 = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, now the time is ", strTime1)

        elif 'quit' in query:
            speak("Thank you sir,meet you again,.......byyyye")
            exit()
