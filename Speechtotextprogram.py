#Speech to text Program 

#pip install SpeechRecognition
import speech_recognition as sr
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
speech_to_text()
from pydub import AudioSegment

def audiofile_to_text():
    mp3_file = "output.mp3"
    wav_file = "converted_audio.wav" 
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        print("Processing audio file...")
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language='en-US')
        print("The audio file contains: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
audiofile_to_text()




