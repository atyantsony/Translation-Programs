# Program to translate inputed string to desired language
# Input: Output Language, String to be translated
# Output: Translated String

# This program uses translate library
# Learn more about translate here:-
# https://pypi.org/project/translate/

# Update 1:
# Added functionality to speak out the translated output.
# I have used gtts library for producing the audio and playsound library to play the produced audio

# Update 2:
# Added speech recognition to the program so that it can take input string using speech recognition. The user still needs to type the output language.
# I have used speech_recognition, pyaudio & pyspeech libraries for the above purpose.


from translate import Translator
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    print("Processing...")
try:
    in_text = r.recognize_google(audio)
    print("Input String: " + in_text)
except sr.UnknownValueError:
    print("Sorry! Unable to understand you.")
    print("Try typing in the input")
    in_text = input()
except sr.RequestError:
    print("Unable to request Google Speech Recognition services. Make sure you have good internet connection.")
    print("Try typing in the input")
    in_text = input()

print("Enter Output Language:")
out_lang = input()

try:
    translator = Translator(to_lang = out_lang)
    trans_text = translator.translate(in_text)
    print(trans_text)
except:
    print("Error while translating. Probably the input string and output string are same or your internet is unstable.")
    exit()

try:
    tts = gTTS(text=str(trans_text), lang=str(out_lang))
    tts.save("translation.mp3")
    playsound("translation.mp3")
except:
    print("Error while performing text-to-speech")
    exit()
