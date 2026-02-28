# # pip install SpeechRecognition
# ######################################################### pip install pipwin         No
# ######################################################### pipwin install pyaudio
#
# import speech_recognition
#
#
# sp = speech_recognition.Recognizer()
# # print(type(sp))
# # print(*dir(sp), sep='\n')
# # breakpoint()
# sp.pause_threshold = 0.5
#
#
# def listen_voice():
#     print('.' * 80)
#     print('Скажіть щось, а я напишу те, що зрозумів...\n')
#     try:
#         with speech_recognition.Microphone() as mic:
#             sp.adjust_for_ambient_noise(source=mic, duration=0)
#             audio = sp.listen(source=mic)
#             query = sp.recognize_google(audio_data=audio, language='uk-UA', show_all=True)
#             # query = sp.recognize_google(audio_data=audio, language='uk-UA')
#             # query = sp.recognize_google(audio_data=audio, language='en-US')
#             # query = sp.recognize_google(audio_data=audio, language='fr-FR').lower()
#         return query
#     except speech_recognition.UnknownValueError:
#         return 'Я не зрозумів. Повторіть, будь ласка.'
#
#
# def run():
#     voice = listen_voice()
#     print(voice)
#     return voice
#
#
# if __name__ == "__main__":
#     answer = ' '
#     while answer != 'зупинись':
#         answer = run()
#     print('=' * 80)
#     print('STOP PROGRAM!')
#
# #######################################################
# #
# #
# # from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
# # import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
# # import wave  # создание и чтение аудиофайлов формата wav
# # import json  # работа с json-файлами и json-строками
# # import os  # работа с файловой системой
# #
# #
# # def record_and_recognize_audio(*args: tuple):
# #     """
# #     Запись и распознавание аудио
# #     """
# #     with microphone:
# #         recognized_data = ""
# #
# #         # регулирование уровня окружающего шума
# #         recognizer.adjust_for_ambient_noise(microphone, duration=2)
# #
# #         try:
# #             print("Listening...")
# #             audio = recognizer.listen(microphone, 5, 5)
# #
# #             with open("microphone-results.wav", "wb") as file:
# #                 file.write(audio.get_wav_data())
# #
# #         except speech_recognition.WaitTimeoutError:
# #             print("Can you check if your microphone is on, please?")
# #             return
# #
# #         # использование online-распознавания через Google
# #         try:
# #             print("Started recognition...")
# #             recognized_data = recognizer.recognize_google(audio, language="ru").lower()
# #
# #         except speech_recognition.UnknownValueError:
# #             pass
# #
# #         # в случае проблем с доступом в Интернет происходит попытка
# #         # использовать offline-распознавание через Vosk
# #         except speech_recognition.RequestError:
# #             print("Trying to use offline recognition...")
# #             recognized_data = use_offline_recognition()
# #
# #         return recognized_data
# #
# #
# # def use_offline_recognition():
# #     """
# #     Переключение на оффлайн-распознавание речи
# #     :return: распознанная фраза
# #     """
# #     recognized_data = ""
# #     try:
# #         # проверка наличия модели на нужном языке в каталоге приложения
# #         if not os.path.exists("models/vosk-model-small-ru-0.4"):
# #             print("Please download the model from:\n"
# #                   "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
# #             exit(1)
# #
# #         # анализ записанного в микрофон аудио (чтобы избежать повторов фразы)
# #         wave_audio_file = wave.open("microphone-results.wav", "rb")
# #         model = Model("models/vosk-model-small-ru-0.4")
# #         offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())
# #
# #         data = wave_audio_file.readframes(wave_audio_file.getnframes())
# #         if len(data) > 0:
# #             if offline_recognizer.AcceptWaveform(data):
# #                 recognized_data = offline_recognizer.Result()
# #
# #                 # получение данных распознанного текста из JSON-строки
# #                 # (чтобы можно было выдать по ней ответ)
# #                 recognized_data = json.loads(recognized_data)
# #                 recognized_data = recognized_data["text"]
# #     except:
# #         print("Sorry, speech service is unavailable. Try again later")
# #
# #     return recognized_data
# #
# #
# # if __name__ == "__main__":
# #
# #     # инициализация инструментов распознавания и ввода речи
# #     recognizer = speech_recognition.Recognizer()
# #     microphone = speech_recognition.Microphone()
# #
# #     while True:
# #         # старт записи речи с последующим выводом распознанной речи
# #         # и удалением записанного в микрофон аудио
# #         voice_input = record_and_recognize_audio()
# #         os.remove("microphone-results.wav")
# #         print(voice_input)
#
# #############################################################
# #############################################################
#
# # `pip3 install assemblyai` (macOS)
# # `pip install assemblyai` (Windows)
#
# import assemblyai as aai
#
# aai.settings.api_key = "9a099670686b499f92b960ab61c62a96"
# transcriber = aai.Transcriber()
#
# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# # transcript = transcriber.transcribe("./my-local-audio-file.wav")
#
# print(transcript.text)


#
# import speech_recognition as sr
#
# def record_audio():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Скажіть щось:")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         audio = recognizer.listen(source)
#     return audio
#
# def recognize_speech(audio):
#     recognizer = sr.Recognizer()
#     try:
#         print("Розпізнано:")
#         text = recognizer.recognize_google(audio, language="uk-UA")
#         print(text)
#     except sr.UnknownValueError:
#         print("Не вдалося розпізнати мову")
#     except sr.RequestError as e:
#         print("Помилка сервісу розпізнавання мови: {0}".format(e))
#
# if __name__ == "__main__":
#     audio_data = record_audio()
#     recognize_speech(audio_data)
###################################################################

import speech_recognition



def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition:
            print("Check your Internet Connection, please")

        return recognized_data

if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        # старт записи речи с последующим выводом распознанной речи
        voice_input = record_and_recognize_audio()
        print(voice_input)