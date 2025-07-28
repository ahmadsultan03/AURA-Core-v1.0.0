# copyrights © Muhammad Ahmad Sultan

import datetime
import time
import pyttsx3                    # For converting text to speech
import speech_recognition as sr   # For converting speech to text

# Set up the text-to-speech engine with preferred voice, speed, and volume
def initialize_engine():
    engine = pyttsx3.init("sapi5")              # Use built-in Windows speech engine
    voices = engine.getProperty('voices')       # Fetch available system voices
    engine.setProperty('voice', voices[1].id)   # Choose a female voice (index may vary)

    rate = engine.getProperty('rate')           # Get current speaking rate
    engine.setProperty('rate', rate - 50)       # Make speech slightly slower for clarity

    volume = engine.getProperty('volume')       # Get current volume level
    engine.setProperty('volume', min(volume + 0.25, 1.0))  # Boost volume, but cap at 100%

    return engine

# Speak out the given text
def speak(text):
    engine = initialize_engine()    # Load and configure engine
    engine.say(text)                # Add text to speech queue
    engine.runAndWait()             # Speak the queued text

# Listen to the microphone and prepare for voice input
def command():
    r = sr.Recognizer()             # Create a speech recognizer
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)  # Reduce background noise effect
        print("Listening...", end = "", flush=True)
        r.pause_threshold = 1.0     # Wait 1 sec if user pauses mid-sentence
        r.phrase_threshold = 0.3    # Accept short phrases more easily
        r.sample_rate = 48000
        r.dynamic_energy_threshold=True
        r.operation_timeout=5
        r.non_speaking_duration=0.5
        r.dynamic_energy_adjustment=2
        r.energy_threshold=4000
        r.phrase_time_limit=10
        # print(sr.Microphone.list_microphone_names())
        audio = r.listen(source)

        try:
            print("\r", end="", flush=True)
            print("Just a moment while I process that...", end="", flush=True)
            query = r.recognize_google(audio, language='en-in')
            print("\r", end="", flush=True)
            print(f"User said: {query}\n")
        except Exception as e:
            print("Oops, didn’t get that. Mind saying it again?")
            return "None"

        return query

def calc_day():
    day = datetime.datetime.today().weekday()+1
    day_dict={
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }
    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)
    return day_of_week

def greetings():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M:%p")
    day = calc_day()

    if (hour >= 5) and (hour < 12) and ('AM' in t):
        speak(f"Good morning Ahmad, it's {day} and the time is {t}")
    elif (hour >= 12) and (hour < 17) and ('PM' in t):
        speak(f"Good afternoon Ahmad, it's {day} and the time is {t}")
    elif (hour >= 17) and (hour < 21) and ('PM' in t):
        speak(f"Good evening Ahmad, it's {day} and the time is {t}")
    else:
        speak(f"Good night Ahmad, it's {day} and the time is {t}")


if __name__ == "__main__":
    greetings()
    # while True:
        # query = command().lower()
        # query = input("Enter your command -> ")




# Example usage
# speak("Hi! I’m AURA. Standing by for your commands.")
