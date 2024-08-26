import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak out the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio input from the user and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {command}\n")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that. Could you please repeat?")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

def respond_to_command(command):
    """Respond to simple commands."""
    if 'hello' in command:
        speak("Hello! How can I assist you today?")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {current_time}.")
    elif 'date' in command:
        today = datetime.date.today().strftime('%B %d, %Y')
        speak(f"Today's date is {today}.")
    elif 'search' in command:
        speak("What would you like to search for?")
        query = listen()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching Google for {query}.")
    else:
        speak("Sorry, I can only perform simple tasks like telling the time or date, or searching the web.")

if __name__ == "__main__":
    speak("Welcome! I am your voice assistant.")
    while True:
        command = listen()
        if command:
            respond_to_command(command)
            
        # Stop listening if the user says 'exit'
        if command == 'exit':
            speak("Goodbye!")
            break
