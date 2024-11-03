from deep_translator import Google Translator

from gtts import gTTS

import os

text = input("Enter text to translate: ")

translator = GoogleTranslator (source='en', target='es')

# Perform the translation (en -> es)

translated = translator.translate(text)

print("Original:", text)

print("Translated:", translated)

tts = gTTS(text=translated, lang='es')

tts.save("translated_speech.mp3")

os.system("start translated_speech.mp3")
