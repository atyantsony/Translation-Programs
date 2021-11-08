
# Python Translate Programs

Translate user input to desired output language using Python Libararies like Goslate, Translate & Textblob.

This repository have 3 independent python files. Each file uses different above-mentioned Libararies. 

The program which uses the library Textblob, namely text_blob.py, is the most reliable and accurate among all 3 programs.


## Run Locally

Clone the project

```bash
  git clone https://github.com/atyantsony/Translation-Programs
```

Go to the project directory

```bash
  cd Translation-Programs
```

Install dependencies

```bash
  pip install goslate
  pip install translate
  pip install textblob
  pip install pycountry
  pip install pyspeech
  pip install speech_recognition
  pip install gtts
  pip install playsound
  pip install pipwin
  pipwin install pyaudio
```

Run the Program

```bash
  python text_goslate.py
  python text_translate.py
  python text_blob.py
```


## How to use the programs

Your computer should have installed Python 3 and the libraries given below:
- goslate
- translate
- textblob
- speech_recognition
- pycountry
- gtts
- playsound
- pyspeech
- pyaudio
Good Internet Connectivity is required while running the programs.

You can run desired program by typing below command in command prompt
```bash
  python <filename>.py
```
Enter the name of file in place of <filename>.

The text_goslate.py program is pretty straight forward as the output instructions are clearly printed to the terminal.

The text_translate.py and text_blob.py programs includes speech recognition. Below are the voice commands you need to give to run the programs smoothly:
- When the program prints "Listening..." on the terminal, speak out a voice command of following format
```
    "Translate from English to French"
```
Or
```
    "Ok Computer, translate from French to English"
```
Make sure your voice commands are clear and loud & your microphone is working properly.
- After you stopped speaking, you will see "Recognising..." printed on the screen. After few seconds, the program will print out the Input it has recognised.
- If for some reason, the program fails to recognise your voice command, the program gives you an option to type in the command.
- After you have given the first command & see "Listening..." printed on terminal, now speak out the sentence that you want to translate.
- You can also type in the sentence if voice recognition fails.
- After the second command, the program will translate the sentence to desired language and print it on the terminal and speak it out.
## Tech Stack

**Programming Language:** Python 3.9.1

**Libraries Used:** goslate, translate, textblob, speech_recognition, playsound, gtts, pycountry


## Authors
Below are links to my 2 GitHub profiles
- [@atyantsony](https://github.com/atyantsony)
- [@atyant20039](https://github.com/atyant20039)

