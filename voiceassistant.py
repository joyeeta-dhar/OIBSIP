import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyaudio

# Initialize the speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

# Function to get the current date
def get_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%A, %B %d, %Y")
    return current_date

# Function to take a command from the user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you repeat?")
        return "None"
    return command.lower()

# Function to perform tasks based on voice commands
def voice_assistant():
    speak("Hello! How can I assist you today?")
    while True:
        command = take_command()

        # Respond to "hello"
        if 'hello' in command:
            speak("Hello! How can I help you?")

        # Tell the time
        elif 'time' in command:
            current_time = get_time()
            speak(f"The current time is {current_time}")

        # Tell the date
        elif 'date' in command:
            current_date = get_date()
            speak(f"Today's date is {current_date}")

        # Search the web
        elif 'search' in command:
            speak("What would you like to search for?")
            query = take_command()
            if query != "None":
                speak(f"Searching for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")

        # Search Wikipedia
        elif 'wikipedia' in command:
            speak("What would you like to search on Wikipedia?")
            query = take_command()
            if query != "None":
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)

        # Exit the voice assistant
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I'm sorry, I didn't understand that. Could you please repeat?")

# Run the voice assistant
if __name__ == "__main__":
    voice_assistant()
