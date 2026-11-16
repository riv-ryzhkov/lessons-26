import speech_recognition as sr
from datetime import datetime
from google import genai
from my_API import api_key as API_KEY

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

            return text

        except sr.UnknownValueError:
            continue
        except sr.RequestError:
            print("Помилка сервісу розпізнавання.")
            return

    print("Не вдалося розпізнати мовлення жодною з підтримуваних мов.")


# Головний цикл програми
if __name__ == "__main__":

    while True:
        text = recognize_speech()

        client = genai.Client(api_key=API_KEY)

        # 2. Инициализация модели
        # "gemini-3-flash-preview" — быстрая и легкая модель.
        MODEL_ID = "gemini-3-flash-preview"

        # 3. Запуск сессии чата с пустой историей
        chat_session = client.chats.create(model=MODEL_ID)

        print("--- Gemini Chat (для выхода введите 'exit' или 'quit') ---")

        user_input = text

        if user_input.lower() in ['exit', 'quit', 'выход']:
            print("Пока!")
            break

        try:
            # Отправка сообщения и получение ответа
            response = chat_session.send_message(user_input)

            print(f"\nGemini: {response.text}\n")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

