# Program to translate inputed string to desired language
# Input: Output Language, String to be translated
# Output: Translated String

# This program uses textblob library
# Learn more about translate here:-
# https://pypi.org/project/textblob/

# Update:
# Added functionality to speak out the translated output.
# I have used gtts library for producing the audio and playsound library to play the produced audio

from textblob import TextBlob
from gtts import gTTS
from playsound import playsound

print("Enter Input String:")
string = input()
print("Enter Output language:")
out_lang = input()

try:
    adding_blob = TextBlob(string)
    translated_text = adding_blob.translate(to = out_lang)
    print("Translated Text:")
    print(translated_text)
except:
    print("Error while translating. Probably the input string and the translated string are same.")

try:
    tts = gTTS(text=str(translated_text), lang=str(out_lang))
    tts.save("translation.mp3")
    playsound("translation.mp3")
except:
    print("Error while performing text-to-speech")
