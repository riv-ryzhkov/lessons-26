import speech_recognition as sr
from googletrans import Translator
import pyttsx3
from datetime import datetime
import time

recognizer = sr.Recognizer()
translator = Translator()

# Правильні мовні коди
SPEECH_LANG_CODES = {
    "uk": "uk-UA",
    "fr": "fr-FR"
}

SUPPORTED_LANGUAGES = {
    "uk": "Українська",
    "fr": "Французька"
}

# ======================
# РОЗПІЗНАВАННЯ
# ======================

def recognize_speech():
    with sr.Microphone() as source:
        print("\nГоворіть...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    for lang_code, speech_code in SPEECH_LANG_CODES.items():
        try:
            text = recognizer.recognize_google(audio, language=speech_code)
            return text
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print("Помилка сервісу:", e)
            return None

    print("Не вдалося розпізнати мову.")
    return None

# ======================
# ПЕРЕКЛАД
# ======================

def detect_and_translate(text):
    try:
        detection = translator.detect(text)
        detected_lang = detection.lang
    except Exception as e:
        print("Помилка визначення мови:", e)
        return None, None

    if detected_lang not in SUPPORTED_LANGUAGES:
        print("Мова не підтримується.")
        return None, None

    target_lang = "fr" if detected_lang == "uk" else "uk"

    try:
        translation = translator.translate(text, src=detected_lang, dest=target_lang)
        return translation.text, target_lang
    except Exception as e:
        print("Помилка перекладу:", e)
        return None, None

# ======================
# СИНТЕЗ МОВЛЕННЯ
# ======================

def speak(text, language_code):
    engine = pyttsx3.init()  # Ініціалізація щоразу — стабільніше

    voices = engine.getProperty('voices')
    for voice in voices:
        if language_code in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.say(text)
    engine.runAndWait()
    engine.stop()  # Очищення рушія

# ======================
# ЛОГУВАННЯ
# ======================

def save_log(original, translated, lang_code):
    with open("system_log.txt", "a", encoding="utf-8") as file:
        file.write("=====================================\n")
        file.write(f"Час: {datetime.now()}\n")
        file.write(f"Оригінал: {original}\n")
        file.write(f"Переклад ({SUPPORTED_LANGUAGES[lang_code]}): {translated}\n")

# ======================
# ГОЛОВНИЙ ЦИКЛ
# ======================

def run_system():
    text = recognize_speech()

    if not text:
        return

    print("Розпізнаний текст:", text)

    translated_text, target_lang = detect_and_translate(text)

    if not translated_text:
        return

    print("Переклад:", translated_text)

    speak(translated_text, target_lang)
    save_log(text, translated_text, target_lang)

    time.sleep(0.5)  # Невелика пауза для стабільності

if __name__ == "__main__":
    while True:
        run_system()
