# gTTS module is used to convert text to speech - Google Text To Speech
# pip install gtts

from gtts import gTTS
import os

file_contect = open('text.txt', 'r').read()

text = "LOL this is really funny. " + file_contect
language = 'en'
audio_output = gTTS(text=text, lang=language, slow=False)		# This will return the audio
audio_output.save('speech.mp3')

# Play the mp3 file
os.system("start speech.mp3")		# Using the OS program this will play the mp3 file
