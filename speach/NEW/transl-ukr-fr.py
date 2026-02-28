import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Ініціалізація розпізнавача, перекладача та синтезатора мовлення
recognizer = sr.Recognizer()
translator = Translator()
engine = pyttsx3.init()

# Функція для встановлення голосу відповідною мовою
def set_voice(language_code):
    voices = engine.getProperty('voices')
    for voice in voices:
        if language_code in voice.id.lower():
            engine.setProperty('voice', voice.id)
            return

# Функція озвучування тексту
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Функція визначення мови та перекладу
def detect_and_translate(text):
    detection = translator.detect(text)
    detected_lang = detection.lang

    if detected_lang == "uk":
        # Якщо українська → перекладаємо на французьку
        translation = translator.translate(text, src="uk", dest="fr")
        set_voice("fr")
        target_lang = "Французька"
    elif detected_lang == "fr":
        # Якщо французька → перекладаємо на українську
        translation = translator.translate(text, src="fr", dest="uk")
        set_voice("uk")
        target_lang = "Українська"
    else:
        print("Мова не підтримується. Говоріть українською або французькою.")
        return None, None

    return translation.text, target_lang

def listen_and_translate():
    with sr.Microphone() as source:
        print("Говоріть українською або французькою...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Спроба розпізнати обидві мови
        try:
            text = recognizer.recognize_google(audio, language="uk-UA")
        except:
            text = recognizer.recognize_google(audio, language="fr-FR")

        print("Розпізнаний текст:", text)

        translated_text, target_lang = detect_and_translate(text)

        if translated_text:
            print("Переклад (" + target_lang + "):", translated_text)
            speak(translated_text)

    except sr.UnknownValueError:
        print("Не вдалося розпізнати мовлення.")
    except sr.RequestError:
        print("Помилка сервісу розпізнавання.")

if __name__ == "__main__":
    while True:
        listen_and_translate()
