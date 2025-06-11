import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speed of speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize recognizer
listener = sr.Recognizer()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant', '').strip()
            return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except:
        speak("Please try again.")
    return ""

def run_assistant():
    speak("Hi! How can I help you?")
    while True:
        command = listen_command()
        if not command:
            continue

        print(f"🗣️ Command: {command}")

        if 'play' in command:
            song = command.replace('play', '').strip()
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")

        elif 'who is' in command:
            person = command.replace('who is', '').strip()
            info = wikipedia.summary(person, sentences=2)
            speak(info)

        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif 'open youtube' in command:
            speak("Opening YouTube")
            pywhatkit.search("YouTube")
        
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I can’t do that yet. Try asking something else.")

# Start
if __name__ == "__main__":
    run_assistant()
