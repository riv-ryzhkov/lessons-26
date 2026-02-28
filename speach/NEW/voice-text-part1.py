import speech_recognition as sr
from datetime import datetime

# Ініціалізація розпізнавача
recognizer = sr.Recognizer()

# Список мов для спроби розпізнавання
LANGUAGES = {
    "Українська": "uk-UA",
    "Французька": "fr-FR",
    "Англійська": "en-US"
}


# Функція запису тексту у файл
def save_to_file(text, language):
    filename = "recognized_speech.txt"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"[{datetime.now()}] ({language}) {text}\n")


# Функція розпізнавання мовлення
def recognize_speech():
    with sr.Microphone() as source:
        print("Говоріть...")

        # Калібрування під фоновий шум
        recognizer.adjust_for_ambient_noise(source)

        # Запис аудіо
        audio = recognizer.listen(source)

    # Спроба розпізнавання різними мовами
    for language_name, language_code in LANGUAGES.items():
        try:
            text = recognizer.recognize_google(audio, language=language_code)

            print(f"Розпізнана мова: {language_name}")
            print("Текст:", text)

            save_to_file(text, language_name)

            return

        except sr.UnknownValueError:
            continue
        except sr.RequestError:
            print("Помилка сервісу розпізнавання.")
            return

    print("Не вдалося розпізнати мовлення жодною з підтримуваних мов.")


# Головний цикл програми
if __name__ == "__main__":
    while True:
        recognize_speech()
