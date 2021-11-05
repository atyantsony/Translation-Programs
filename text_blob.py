# Program to translate inputed string to desired language
# Input: Output Language, String to be translated
# Output: Translated String

# This program uses textblob library
# Learn more about translate here:-
# https://pypi.org/project/textblob/


from textblob import TextBlob

print("Enter Input String:")
str = input()
print("Enter Output language:")
out_lang = input()

adding_blob = TextBlob(str)
translated_text = adding_blob.translate(to = out_lang)
print(translated_text)