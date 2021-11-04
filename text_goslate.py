# Note: goslate only allows limited numbers of translations (nearly 7-8 translations per day from one machine)


# Program to translate inputed english string to inputed language
# Input: English String to Translate, Language to be translated to
# Output: Translated String to the inputed language

# This program uses goslate library which uses Google API to convert input strings to desired language.
# Learn about goslate here:- 
# https://pypi.org/project/goslate/

import goslate
gs = goslate.Goslate()

print("Enter Input String: ")
input_text = input()

print("Enter language to transform to: ")
lang = input()

trans_text = gs.translate(input_text, lang)
print(trans_text)