import wikipedia
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
r.pause_threshold = 0.7                                                                     #it works with 1.2 as well
r.energy_threshold = 400
mic = sr.Microphone()
while True:
    with mic as source:
            engine = pyttsx3.init()
            engine.say("Say something");
            engine.runAndWait()
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                text = str(r.recognize_google(audio))
            except sr.UnknownValueError:
                engine.say("Sorry,I couldn't understand")
                engine.runAndWait()
                continue
            except sr.RequestError as e:
                engine.say("Sorry, Something went wrong. Check your network connection".format(e))
            details = wikipedia.summary(text,sentences='2')
            engine = pyttsx3.init()
            engine.say(details)
            engine.runAndWait()
            engine = pyttsx3.init()
            engine.say("Do you wish to continue?")
            engine.runAndWait()
            r.adjust_for_ambient_noise(source)
            command = r.listen(source)
            try:
                text = str(r.recognize_google(audio))
            except sr.UnknownValueError:
                engine.say("Sorry,I couldn't understand")
                engine.runAndWait()
            except sr.RequestError as e:
                engine.say("Sorry, Something went wrong. Check your network connection".format(e))
    if command=="yes":
        continue
    elif command=="no":
        break
            

    





    
