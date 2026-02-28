import pyttsx3

# Ініціалізація синтезатора мовлення
engine = pyttsx3.init()


# Функція отримання доступних голосів
def list_available_voices():
    voices = engine.getProperty('voices')

    print("Доступні голоси у системі:\n")

    for index, voice in enumerate(voices):
        print(f"{index}:")
        print("  ID:", voice.id)
        print("  Назва:", voice.name)
        print("  Мови:", voice.languages)
        print("-" * 40)


# Функція встановлення голосу за мовним кодом
def set_voice_by_language(language_code):
    voices = engine.getProperty('voices')

    for voice in voices:
        if language_code.lower() in voice.id.lower():
            engine.setProperty('voice', voice.id)
            return True

    return False


# Функція озвучування тексту
def speak(text, rate=180, volume=1.0):
    # Встановлення швидкості мовлення
    engine.setProperty('rate', rate)

    # Встановлення гучності (0.0 - 1.0)
    engine.setProperty('volume', volume)

    engine.say(text)
    engine.runAndWait()


# Головна частина програми
if __name__ == "__main__":

    list_available_voices()

    while True:
        text = input("\nВведіть текст для озвучування (або 'exit' для виходу): ")

        if text.lower() == "exit":
            break

        language = input("Оберіть мову озвучування (uk/fr): ").lower()

        if set_voice_by_language(language):
            speak(text)
        else:
            print("Відповідний голос не знайдено у системі.")
