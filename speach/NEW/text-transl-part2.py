from googletrans import Translator
from datetime import datetime

# Ініціалізація перекладача
translator = Translator()

# Підтримувані мови
SUPPORTED_LANGUAGES = {
    "uk": "Українська",
    "fr": "Французька"
}


# Функція збереження перекладу у файл
def save_translation(original_text, detected_lang, translated_text):
    filename = "translations.txt"

    with open(filename, "a", encoding="utf-8") as file:
        file.write("=====================================\n")
        file.write(f"Час: {datetime.now()}\n")
        file.write(f"Визначена мова: {SUPPORTED_LANGUAGES.get(detected_lang, 'Невідома')}\n")
        file.write(f"Оригінал: {original_text}\n")
        file.write(f"Переклад: {translated_text}\n")


# Функція визначення мови та перекладу
def detect_and_translate(text):
    # Визначення мови тексту
    detection = translator.detect(text)
    detected_lang = detection.lang

    print("Визначена мова:", SUPPORTED_LANGUAGES.get(detected_lang, "Невідома"))

    if detected_lang == "uk":
        # Переклад з української на французьку
        translation = translator.translate(text, src="uk", dest="fr")
        target_lang = "Французька"

    elif detected_lang == "fr":
        # Переклад з французької на українську
        translation = translator.translate(text, src="fr", dest="uk")
        target_lang = "Українська"

    else:
        print("Мова не підтримується.")
        return

    print("Переклад (" + target_lang + "):", translation.text)

    # Збереження результату
    save_translation(text, detected_lang, translation.text)


# Головна частина програми
if __name__ == "__main__":
    while True:
        user_input = input("\nВведіть текст українською або французькою (або 'exit' для виходу): ")

        if user_input.lower() == "exit":
            break

        detect_and_translate(user_input)
