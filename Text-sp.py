#text to Speech  

#pip install gTTS

from gtts import gTTS

def text_to_speech(text, lang='te'):
    speech= gTTS(text=text, lang=lang, slow=False)
    speech.save("output.wav")

#pip install googletrans==4.0.0-rc1
from googletrans import Translator

def English_text_to_Telugu(text):
    translator =Translator()
    translation = translator.translate(text,  src='en', dest='te')
    telugu_text = translation.text
    print("teleugu_text", telugu_text)
    speech = gTTS(text=telugu_text, lang='te', slow=False)
    speech.save("telugu_output.mp3")

text = input("Enter the text you want to convert to speech: ")
text_to_speech(text)
English_text_to_Telugu(text)   