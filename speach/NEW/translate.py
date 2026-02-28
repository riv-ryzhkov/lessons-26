import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Инициализация
recognizer = sr.Recognizer()
translator = Translator()
engine = pyttsx3.init()

# Настройка английского голоса (если доступен)
voices = engine.getProperty('voices')
for voice in voices:
    if "english" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_and_translate():
    with sr.Microphone() as source:
        print("Говорите...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Распознаем русский текст
        russian_text = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали:", russian_text)

        # Переводим на английский
        translation = translator.translate(russian_text, src='ru', dest='en')
        english_text = translation.text
        print("Перевод:", english_text)

        # Озвучиваем перевод
        speak(english_text)

    except sr.UnknownValueError:
        print("Не удалось распознать речь.")
    except sr.RequestError:
        print("Ошибка сервиса распознавания.")

if __name__ == "__main__":
    while True:
        listen_and_translate()
