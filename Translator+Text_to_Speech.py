from deep_translator import Google Translator

from gtts import gTTS

import os

def translate_text(text):
	t = GoogleTranslator (source='en', target='hi') 
	return t.translate(text)

def text_to_speech (text, file_name="speech.mp3"): 
	tts gTTS(text=text, lang='hi') 
	tts.save(file_name) 
	os.system("start" + file_name)

text = input("Please enter a text: ")

translated = translate_text(text)

print("Original:", text)

print("Translated:", translated)

text_to_speech (translated)
