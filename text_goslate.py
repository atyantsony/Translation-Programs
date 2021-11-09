# Note: goslate only allows limited numbers of translations (nearly 7-8 translations per day from one machine)


# Program to translate inputed english string to inputed language
# Input: English String to Translate, Language to be translated to
# Output: Translated String to the inputed language

# This program uses goslate library which uses Google API to convert input strings to desired language.
# Learn about goslate here:- 
# https://pypi.org/project/goslate/

try:
    import goslate
    import urllib
except:
    print("Error while importing goslate module.\nPlease make sure that you have installed the goslate module using bash command 'pip install goslate' without quotes")
    
gs = goslate.Goslate()

print("Enter Input String: ")
input_text = input()

print("Enter language to transform to: ")
lang = input()

try:
    trans_text = gs.translate(input_text, lang)
    print(trans_text)
except urllib.error.HTTPError:
    print("You have reached the translation request limit!\nCannot translate too many requests in a day. Try again tomorrow.")
except urllib.error.URLError:
    print("Unable to connect to internet!\nPlease make sure that you have good internet connection.")
except:
    print("Error while translating.")