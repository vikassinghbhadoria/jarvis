import pyttsx3
import datetime
import speech_recognition as sp
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
 #print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else :
        speak("good evening!")
    speak("I am jarvis master....How may I help you??")
    speak("i am designed in english so kindly use that language")
    speak("master i will suggest you to go through below instruction")
    print("Basically its KIND OF MINI ALEXA with simple functions\nYOU CAN:\n1.ask the time/the date\n2.can ask to open google, email ,youtube,instagram, facebook etc")
    print("3.for seaching anything in preimported wikipedia module....just ask that word along with wikipedia in sentence")
    print("4.can also ask how are you and something about you because these are pre installed questions")
def takecommand():
    r = sp.Recognizer()
    with sp.Microphone() as source:
         print("listening..............")
         r.pause_threshold = 1
         audio = r.listen(source)
    try:
         print("Recognising.............")
         query = r.recognize_google(audio, language='en-in')
         print(f"user(YOU) said: {query}\n")
    except Exception  as e:
        # print(e)
         print("say that again please.........")
         return "None"
    return query
if __name__== "__main__":
    wishme()
    while True:
      query = takecommand().lower()
      # LOGIC BASED ON QUERY
      if 'wikipedia' in query:
          speak("searching in wikipedia....................")
          speak("   ")
          query = query.replace("wikipedia","")
          result= wikipedia.summary(query, sentences= 3)
          speak("according to wikipedia")
          print(result)
          speak(result)
      elif'how are you' in query:
          speak("I am good.....hope you have a great day master")
      elif 'something about you' in query:
          speak("i am kind of AI present here to helf you out.......")
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
      elif 'open google' in query:
          webbrowser.open("google.com")
      elif 'open geeks for geeks' in query:
          webbrowser.open("geeksforgeeks.com")
      elif 'play music' in query:
          webbrowser.open("gaana.com")
      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          print(strTime)
          speak(f"the time is :{strTime}")
      elif 'open stack overflow' in query:
          webbrowser.open("stackoverflow.com")
      elif 'open flipkart' in query:
          webbrowser.open("flipkart.com")
      elif 'open whatsapp' in query:
          webbrowser.open("whatsapp.com")
      elif 'open instagram' in query:
          webbrowser.open("instagram.com")
      elif 'open facebook' in query:
          webbrowser.open("facebook.com")
      elif 'open linkedin' in query:
          webbrowser.open("linkedin.com")
      elif 'open quora' in query:
          webbrowser.open("quora.com")
      elif 'open code' in query:
          codepath="F:\\Microsoft VS Code\\Code.exe"
          os.startfile(codepath)
      elif 'open email' in query:
          webbrowser.open("gmail.com")
      elif 'the date' in query:
          from datetime import date
          today = date.today()
          print(f"today's date is {today}")
          speak(f"today's date is {today}")
