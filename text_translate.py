# Program to translate inputed string to desired language
# Input: Input language, Output Language, String to be translated
# Output: Translated String

# This program uses translate library
# Learn more about translate here:-
# https://pypi.org/project/translate/

from translate import Translator

print("Enter Input Language:")
in_lang = input()
print("Enter Output Language:")
out_lang = input()

print("Enter String to translate:")
in_text = input()

translator = Translator(from_lang = in_lang, to_lang = out_lang)
trans_text = translator.translate(in_text)
print(trans_text)