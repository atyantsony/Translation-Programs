# Program to translate inputed string to desired language
# Input: Output Language, String to be translated
# Output: Translated String

# This program uses translate library
# Learn more about translate here:-
# https://pypi.org/project/translate/

from translate import Translator

print("Enter String to translate:")
in_text = input()

print("Enter Output Language:")
out_lang = input()

translator = Translator(to_lang = out_lang)
trans_text = translator.translate(in_text)
print(trans_text)