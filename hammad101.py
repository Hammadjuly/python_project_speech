import os
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
import tkinter as tk
from tkinter import ttk
import platform

# Define supported languages and their ISO 639-1 codes
languages = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Russian': 'ru',
    'Chinese (Simplified)': 'zh-CN',
    'Chinese (Traditional)': 'zh-TW',
    'Arabic': 'ar',
    'Dutch': 'nl',
    'Portuguese': 'pt',
    'Swedish': 'sv',
    'Turkish': 'tr',
    'Hindi': 'hi',
    'Urdu': 'ur',      # Added Urdu
    'Punjabi': 'pa',   # Added Punjabi
}

def translate_text():
    text = text_to_translate_entry.get()
    target_language = translation_language_combobox.get()

    try:
        # Translate the text to the selected language
        translator = Translator()
        translated_text = translator.translate(text, dest=target_language)
        translated_text = translated_text.text

        # Display the translated text
        translated_text_result_label.config(text="Translated Text: " + translated_text)
    except Exception as e:
        print("Error:", e)
        translated_text_result_label.config(text="Translation Error")

def speech_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        recognized_text_result_label.config(text="Recognized Text: " + recognized_text)
    except sr.UnknownValueError:
        recognized_text_result_label.config(text="Sorry, couldn't understand the audio.")
    except sr.RequestError:
        recognized_text_result_label.config(text="Sorry, there was an error with the speech recognition service.")

# Create the main window
root = tk.Tk()
root.title("Speech Recognition and Text Translation")

# Create and configure the notebook
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create frames for each tab
speech_recognition_frame = ttk.Frame(notebook)
text_translation_frame = ttk.Frame(notebook)

notebook.add(speech_recognition_frame, text="Speech Recognition")
notebook.add(text_translation_frame, text="Text Translation")

# Speech Recognition Tab
start_listening_button = ttk.Button(speech_recognition_frame, text="Start Listening", command=speech_recognition)
start_listening_button.pack()
recognized_text_result_label = ttk.Label(speech_recognition_frame, text="Recognized Text:")
recognized_text_result_label.pack()

# Text Translation Tab
text_to_translate_label = ttk.Label(text_translation_frame, text="Enter text to translate:")
text_to_translate_label.pack()
text_to_translate_entry = ttk.Entry(text_translation_frame)
text_to_translate_entry.pack()
language_label = ttk.Label(text_translation_frame, text="Select the target language:")
language_label.pack()
translation_language_combobox = ttk.Combobox(text_translation_frame, values=list(languages.keys()))
translation_language_combobox.pack()
translation_language_combobox.set('English')  # Default language

translate_text_button = ttk.Button(text_translation_frame, text="Translate", command=translate_text)
translate_text_button.pack()
translated_text_result_label = ttk.Label(text_translation_frame, text="Translated Text:")
translated_text_result_label.pack()

root.mainloop()
