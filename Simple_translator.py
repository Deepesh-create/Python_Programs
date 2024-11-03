#Import the Google Translator class

from deep_translator import Google Translator

# Prompt user to enter text to be translated

text = input("Enter text to translate: ")

# Create translator instance

translator = GoogleTranslator(source='en', target='de')

# Perform the translation (en -> de)

translated = translator.translate(text)

# Print original text

print("Original:", text)

# Print translated text

print("Translated:", translated)
