import speech_recognition as sr
from datetime import datetime
from google import genai
from gtts import gTTS
import pygame
import os
import time
from my_API import api_key as API_KEY

# Ініціалізація Pygame для відтворення звуку
pygame.mixer.init()

# Ініціалізація розпізнавача
recognizer = sr.Recognizer()

# Мови
LANGUAGES = {
    "Українська": "uk-UA",
    "Англійська": "en-US"
}


def speak(text):
    """Перетворює текст у голос та відтворює його."""
    try:
        # Створюємо аудіофайл (мова автоматично українська для відповідей)
        tts = gTTS(text=text, lang='uk')
        filename = "reply.mp3"
        tts.save(filename)

        # Відтворення
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Чекаємо, поки файл дограє
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()
        os.remove(filename)  # Видаляємо тимчасовий файл
    except Exception as e:
        print(f"Помилка синтезу мовлення: {e}")


def recognize_speech():
    """Слухає голос користувача."""
    with sr.Microphone() as source:
        print("\n[Слухаю...]")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    for language_name, language_code in LANGUAGES.items():
        try:
            text = recognizer.recognize_google(audio, language=language_code)
            print(f"Ви сказали ({language_name}): {text}")
            return text
        except:
            continue
    return None


if __name__ == "__main__":
    # Налаштування Gemini
    client = genai.Client(api_key=API_KEY)
    MODEL_ID = "gemini-3-flash-preview"

    # Системна інструкція, щоб Gemini була лаконічною (важливо для голосових відповідей)
    chat_session = client.chats.create(
        model=MODEL_ID,
        config={
            'system_instruction': "Відповідай коротко і лаконічно, максимум 2-3 речення. Ти — корисний голосовий асистент."}
    )

    speak("Привіт! Я готовий до спілкування.")

    while True:
        user_input = recognize_speech()

        if not user_input:
            continue

        if user_input.lower() in ['вихід', 'exit', 'stop', 'бувай']:
            speak("До побачення!")
            break

        try:
            # Отримання відповіді від Gemini
            response = chat_session.send_message(user_input)
            gemini_text = response.text

            print(f"Gemini: {gemini_text}")

            # Озвучування відповіді
            speak(gemini_text)

        except Exception as e:
            print(f"Помилка: {e}")