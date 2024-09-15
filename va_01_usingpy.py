import speech_recognition as sr
import pyttsx3 # python text to speech 
import pywhatkit # Gives you the package to hyperlink social medias

user_recorded = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
    
def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("Hello, How may I assist you today?")

def user_givenAssist():
    pass

    try:
        with sr.Microphone() as main_source:
            user_recorded.adjust_for_ambient_noise(main_source, duration=1)
            print("Give me a command...")
            voice = user_recorded.listen(main_source)
            assistant = user_recorded.recognize_google(voice)
            print(f"You said: {assistant}")
    except Exception as e:
        print(e)
        
    return assistant
    
def running_userAssist():
    assistant = user_givenAssist()
    print(assistant)
    if 'play' in assistant:
        song = assistant.replace('play', '')
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
        
running_userAssist()    
    
