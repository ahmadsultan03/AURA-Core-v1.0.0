# copyrights © Muhammad Ahmad Sultan

import datetime
import time
import webbrowser
import sys
import os
import pyautogui
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
        # print(day_of_week)
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


def social_media(command):
    if 'facebook' in command:
        speak("Taking you to Facebook...")
        webbrowser.open("https://www.facebook.com/")
    elif 'discord' in command:
        speak("Taking you to Discord...")
        webbrowser.open("https://discord.com/")
    elif 'whatsapp web' in command:
        speak("Taking you to WhatsApp Web...")
        webbrowser.open("https://web.whatsapp.com/")
    elif 'instagram' in command:
        speak("Taking you to Instagram...")
        webbrowser.open("https://www.instagram.com/")
    elif 'youtube' in command:
        speak("Taking you to YouTube...")
        webbrowser.open("https://www.youtube.com/")
    elif 'linkedin' in command:
        speak("Taking you to LinkedIn...")
        webbrowser.open("https://www.linkedin.com/")
    elif 'tiktok' in command:
        speak("Taking you to TikTok...")
        webbrowser.open("https://www.tiktok.com/")
    elif 'twitter' in command:
        speak("Taking you to Twitter...")
        webbrowser.open("https://x.com/")
    elif 'snapchat' in command:
        speak("Taking you to Snapchat...")
        webbrowser.open("https://www.snapchat.com/")
    elif 'reddit' in command:
        speak("Taking you to Reddit...")
        webbrowser.open("https://www.reddit.com/")
    elif 'chatgpt web' in command:
        speak("Taking you to ChatGPT Web...")
        webbrowser.open("https://chatgpt.com/")
    else:
        speak("Sorry, I couldn't identify the social media platform.")

def get_schedule_for_day(day):
    week = {
        "monday": "Hey Buddy! Ready to kick off the week? You’ve got Human-Computer Interaction from 9:00 to 9:50, then it’s Software Quality Engineering from 10:00 to 11:50. Enjoy a well-deserved break from 12:00 to 2:00, and later, dive into Information Retrieval Lab from 2:00 onwards!",
        "tuesday": "Good morning, Boss! First up, Formal Methods from 9:00 to 9:50, followed by a short seminar break from 10:00 to 10:50. From 11:00 to 12:50, you’ll be tackling Software Project Management, then take a quick Duhr Prayer break. Wrap up with your Human-Computer Interaction lab at 2:00 PM.",
        "wednesday": "Hey Buddy, it’s a busy one today! Start your day with Machine Learning from 9:00 to 10:50, then Entrepreneurship class from 11:00 to 11:50. At 12:00, it’s Software Project Management for an hour, followed by a Duhr Prayer break at 1:00. Finish strong with the Software Quality Engineering workshop from 2:00 PM onwards.",
        "thursday": "Good vibes for Thursday, Boss! Begin with Information Retrieval from 9:00 to 10:50, then get into Software Project Management from 11:00 to 12:50. Take your Duhr Prayer break at 1:00, and dive into Formal Methods at 2:00 PM for your final class of the day.",
        "friday": "It’s Friday, Buddy! Start with Entrepreneurship from 9:00 to 9:50, then dive into Software Quality Engineering at 10:00 to 10:50. From 11:00 to 12:50, it’s Machine Learning class, followed by your Jumma Prayer break at 1:00. Finish the day with a productive Machine Learning Lab from 2:00 PM.",
        "saturday": "It’s a more relaxed day, Boss! You’ve got team meetings for your Final Year Project from 9:00 to 11:50, then the rest of the day is yours to chill or catch up on work. Take it easy!",
        "sunday": "Happy Sunday, Buddy! It’s a holiday today, but why not use this time to catch up on readings or projects? Stay ahead on those deadlines, and enjoy the downtime!"
    }
    return week.get(day, "Oops! Something went wrong. Please check the day and try again.")


def schedule():
    day = calc_day().lower()  # assuming calc_day() gives current day in string format
    # speak("Boss today's schedule is ")
    schedule_message = get_schedule_for_day(day)
    speak(schedule_message)


def openApp(command):
    if "calculator" in command:
        speak("Opening Calculator...")
        os.startfile('C:\\Windows\\System32\\calc.exe')

    elif "notepad" in command:
        speak("Opening Notepad...")
        os.startfile('C:\\Windows\\System32\\notepad.exe')

    elif "paint" in command:
        speak("Opening Paint...")
        os.startfile('C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2504.551.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe')

    elif "word" in command or "microsoft word" in command:
        speak("Opening Microsoft Word...")
        os.startfile(
            'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')

    elif "excel" in command or "microsoft excel" in command:
        speak("Opening Microsoft Excel...")
        os.startfile(
            'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE')

    elif "browser" in command or "chrome" in command:
        speak("Opening Google Chrome...")
        os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

    elif "opera" in command:
        speak("Opening Opera GX Browser...")
        os.startfile('C:\\Users\\mahma\\AppData\\Local\\Programs\\Opera GX\\opera.exe')

    elif "explorer" in command or "file explorer" in command:
        speak("Opening File Explorer...")
        os.startfile('C:\\Windows\\explorer.exe')

    elif "cmd" in command or "command prompt" in command:
        speak("Opening Command Prompt...")
        os.startfile('C:\\Windows\\System32\\cmd.exe')

    elif "settings" in command:
        speak("Opening Settings...")
        os.startfile('ms-settings:')

    elif "vlc" in command or "video player" in command:
        speak("Opening Video and Media Player...")
        os.startfile('C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe')

    elif "zoom" in command:
        speak("Opening Zoom...")
        os.startfile('C:\\Users\\mahma\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')

    elif "vs code" in command or "visual studio code" in command:
        speak("Opening Visual Studio Code...")
        os.startfile(
            'C:\\Users\\mahma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

    elif "pycharm" in command or "python ide" in command:
        speak("Opening PyCharm IDE...")
        os.startfile('D:\\myStudy\\PyCharm\\PyCharm Community Edition 2025.1.2\\bin\\pycharm64.exe')

    elif "whatsapp app" in command:
        speak("Opening WhatsApp App...")
        os.startfile('C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2528.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe')

    elif "chatgpt app" in command:
        speak("Opening ChatGPT App...")
        os.startfile('C:\\Program Files\\WindowsApps\\OpenAI.ChatGPT-Desktop_1.2025.202.0_x64__2p2nqsd0c76g0\\app\\ChatGPT.exe')

    else:
        speak("Sorry, I don't recognize that command.")


if __name__ == "__main__":
    # greetings()
    # while True:
        # query = command().lower()
    query = input("Enter your command -> ").lower()
    if ('facebook' in query) or ('discord' in query) or ('whatsapp web' in query) or ('instagram' in query) or \
            ('youtube' in query) or ('linkedin' in query) or ('tiktok' in query) or ('twitter' in query) or \
            ('snapchat' in query) or ('reddit' in query) or ('chatgpt web' in query):
        social_media(query)
    elif ("university time table" in query) or ("schedule" in query):
        schedule()
    elif("volume up" in query) or ("increase volume" in query):
        pyautogui.press("volumeup")
        speak("Volume increased")
    elif ("volume down" in query) or ("decrease volume" in query):
        pyautogui.press("volumedown")
        speak("Volume decreased")
    elif ("volume mute" in query) or ("mute the sound" in query) or ("mute" in query):
        pyautogui.press("volumemute")
        speak("Volume muted")
    elif ("open calculator" in query) or ("open notepad" in query) or ("open paint" in query) or (
            "open word" in query) or ("open excel" in query) or ("open browser" in query) or (
            "open opera" in query) or ("open explorer" in query) or ("open cmd" in query) or (
            "open settings" in query) or ("open video player" in query) or ("open camera" in query) or (
            "open zoom" in query) or ("open vs code" in query) or ("open pycharm" in query) or (
            "open whatsapp app" in query) or ("open chatgpt app" in query):
        openApp(query)

    elif "exit" in query:
        sys.exit()

    else:
        speak("Sorry, I did not understand the command.")



# Example usage
# speak("Hi! I’m AURA. Standing by for your commands.")
