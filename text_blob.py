# Program to translate inputed string to desired language
# Input: Output Language, String to be translated
# Output: Translated String

# This program uses textblob library
# Learn more about translate here:-
# https://pypi.org/project/textblob/

# Update 1:
# Added functionality to speak out the translated output.
# I have used gtts library for producing the audio and playsound library to play the produced audio

# Update 2:
# Added speech recognition to the program so that it can take input string using speech recognition. The user still needs to type the output language.
# I have used speech_recognition, pyaudio & pyspeech libraries for the above purpose.

# Update 3:
# Added speech recognition to take in the input language and output language
# The user first needs to speak out from which language to which language s/he wants to translate. For eg:
# "translate from french to english"
# then the user needs to speak out the string which s/he wants to translate. 
# Option for typing in the input is also available. If the speech recognition fails for some reason, then the user can type in the inputs.
# I have used pycountry library to take out info about different languages.

from textblob import TextBlob
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pycountry as pyctry

def record(lang='en'):
    # A fucntion to recognize input speech audio and convert it to text of speech language.
    # Input: An optional parameter of recognising the audio input as specific language speech. By default, it is english
    # Output: A string which will be text equivalent of the input speech. The string will be in the same language script as of the input audio language.

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Recognising...")
    try:
        string = r.recognize_google(audio, language=lang)
        print("Input: " + string)
    except sr.UnknownValueError:
        print("Sorry! Unable to understand you")
        print("Try typing in:")
        string = input()
        
    except sr.RequestError:
        print("Unable to request Google Speech Recognition services. Make sure you have good internet connection.")
        print("Try typing in:")
        string = input()

    return string
# Function ends
print('Please input language names [from "lang1" to "lang2"]:')
lang_speech = record()    # first voice command to tell from which language to which language needs to be translated

lang_speech = lang_speech.split()
lang_arr = ["en", "en"]   # array of names of languages that stores input_language and output_language
for word in range(len(lang_speech)):
    lang_inst = pyctry.languages.get(name = lang_speech[word])
    try:
        code_name = lang_inst.alpha_2
        if (lang_speech[word-1] == "to"):   # output language
            lang_arr[1] = code_name
        else:                               # input language
            lang_arr[0] = code_name
    except:
        continue

print("Please speak out the sentance you want to translate:")
string_speech = record(lang_arr[0])
# String which needs to be converted.

# Translating using textblob
try:
    adding_blob = TextBlob(string_speech)
    translated_text = adding_blob.translate(to = lang_arr[1])
    print("Translated Text:")
    print(translated_text)
except:
    print("Error while translating. Probably the input string and the translated string are same or your internet is unstable.")
    exit()


# text-to-speech 
# speaking out the output/translated text.
try:
    tts = gTTS(text=str(translated_text), lang=str(lang_arr[1]))
    tts.save("translation.mp3")
    playsound("translation.mp3")
except:
    print("Error while performing text-to-speech")
    exit()
