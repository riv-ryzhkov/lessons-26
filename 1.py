#
# from f2 import a
#
# print(a)
# name = 'Koval'
# number = 25
# start = 1
# end = 10
# text = ''
# while True:
#     for i in range(5):
#         print(3 / i)
#     if text[0] == '':
#         break
# print(end - start)
# print(name * number)



#
# class A:
#     def __init__(self, num=1):
#         self.num = num
#
#     def add(self, num=1):
#         self.num += num
#
# class B(A):
#     def __init__(self, num=4):
#         A.__init__(self, num)
#         self.add(num)
#
#     def add(self, num=1):
#         self.num += 2 * num
#
# a = A()
# a.add()
# b = B()
# b.add()
# print(a.num + b.num)
#
#
#
#
#

# import time
#
# if __name__ == "__main__":
#
#     file = open("Secret.txt", "r", encoding="utf-8")
#     word = file.read()
#     file.close()
#     word = word.upper()
#
#     res = '-'*len(word)
#     usedLetters = []
#     attempts = len(word)
#
#     while word != res:
#         isUsedLetter = False
#         isGuessedLetter = False
#         print("==============================")
#         print(res)
#         print("==============================")
#         print("ЛІТЕРИ, ЩО ВЖЕ ВИКОРИСТАНО: ", usedLetters)
#         print("У ВАС ЗАЛИШИЛОСЬ ", attempts, " СПРОБ")
#         print("==============================")
#         print("ВВЕДІТЬ ЛІТЕРУ:")
#         letter = input()
#         letter = letter.upper()
#
#         if len(letter) == 1 and letter.isalpha():
#             letter.upper()
#             if letter in usedLetters:
#                 print("ЦЯ ЛІТЕРА ВЖЕ ВИКОРИСТАНА, НАЖАЛЬ ")
#
#             else:
#                 usedLetters.append(letter)
#                 for i, c in enumerate(word):
#                     if letter == c:
#                         res = res[:i] + letter + res[i + 1:]
#                         isGuessedLetter = True
#                 if isGuessedLetter == False:
#                     attempts -= 1
#         else:
#             print("ПОМИЛКА, ВИ ВВЕЛИ ЦИФРУ ЧИ НЕ ОДНУ ЛІТЕРУ. СПРОБУЙТЕ ЩЕ!")
#         if res == word:
#             print("ВІТАННЯ, ВИ ВГАДАЛИ!!! ЦЕ СЛОВО: " + res)
#         elif attempts == 0:
#             print("У ВАС ЗАКІНЧИЛИСЯ СПРОБИ. НАЖАЛЬ, ВИ ПРОГРАЛИ")
#             break
#     time.sleep(5)
#     print("КІНЕЦЬ. ДЯКУЮ ЗА ГРУ!")
#








# my_list = 'УрА'
# print(my_list)
#
# print(hash(my_list), id(my_list))
# print(hash(my_list), id(my_list))
# print(hash(my_list), id(my_list))
# print(hash(my_list), id(my_list))
# my_list1 = [el for el in range(1, 7)]

#
# print(my_list)
# print(my_list1)








# my_dict = {'1': 1, '2': 2}
#
# # print(my_dict['4'])
# print(my_dict.get('7868'))




# print(2 * 2)
# print('Hello' * 2)


# say_hello(get_name())

# list1 = [element+55 for element in range(10) if element % 2 == 0]
# print(list1)

# dic1 = {'key1': 222, 'key2': 555}
# # print(dic1['key3'])
# print(dic1.get('key3'))


# print('Hello, world!')




###########################################################
# import PySimpleGUI as sg
#
#
# def execute_code():
#     print('text2')
#
# layout = [
#     [sg.Checkbox(text='On/Off', key='-CHECKBOX-', default=False)],
#     [sg.Button('Exit')],
#     [sg.Button('Check')]
# ]
#
# window = sg.Window('test', layout, size=(200, 300), keep_on_top=True)
#
# while True:
#     event, value = window.read()
#
#     if event in (sg.WINDOW_CLOSED, 'Exit'):
#         break
#     elif event == 'Check':
#         if value.get('-CHECKBOX-'):
#             execute_code()
#
# window.close()
#
####################################################




# equil = 4 > 2 #  True  /  False
# equil = ''
# equil = [0]
# equil = {}
# False  ->   0,  '',  [],   (),  {},  False,  0.0

# equil = True and True and True and True and False
# equil = False or False or not False or False or False


# if equil:
#     print('True')
# else:
#     print('False')


# if True or True and False:
#     print(True)
# else:
#     print(False)



















# print(__name__)





# text = 'Hello, world!'  # str
# words = text.split()   # list
# print(words)
# print(type(words))
# res = '='.join(words)
# print(res, type(res))


#
# import random
#
#
# def initialize_word():
#     words = ["apple", "banana", "orange", "grape", "pineapple"]  # ?????? ????
#     return random.choice(words).upper()  # ???????? ????????? ????? ? ???????? ??? ? ???????? ????????
#
#
# def display(word, guessed_letters, attempts):
#     masked_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
#     print("=" * 41)
#     print(f"{masked_word} (?????????? ?????: {', '.join(sorted(guessed_letters))})")
#     print("=" * 41)
#     print(f"? ??? ???????? {attempts} ???????.")
#     print("=" * 41)
#
#
# def game():
#     secret_word = initialize_word()
#     guessed_letters = set()
#     attempts = len(secret_word)
#
#     while True:
#         display(secret_word, guessed_letters, attempts)
#         if '_' not in ''.join([letter if letter in guessed_letters else '_' for letter in secret_word]):
#             print("???????????, ?? ??????? ?????!")
#             break
#         if attempts == 0:
#             print(f"?? ?????????! ?????????? ????? ????: {secret_word}")
#             break
#
#         user_input = input("??????? ?????: ").upper()
#         if len(user_input) != 1 or not user_input.isalpha():
#             print("??????? ???? ?????!")
#             continue
#         if user_input in guessed_letters:
#             print("??? ????? ??? ??????????????!")
#             continue
#
#         guessed_letters.add(user_input)
#         if user_input not in secret_word:
#             attempts -= 1
#
#
# if __name__ == "__main__":
#     game()










# def foo(name, surname, age):
#     print(name, surname, age)
#
#
# foo(name='Ivan', age=25, surname='Petrov')


#################################################
# pip install flake8
# flake8 1.py
########################################################

# from faker import Faker
# import requests
# import requests
# from faker import Faker
# import datetime

#
# def sin1(alfa):
#     import math
#     a = 1 + 2
#     b = a ** 2
#     print(b)
#     print()
#     print()
#
#     return math.sin(alfa)
#
#
# a = sin1(45)
# print('a=', a)
# #
# #
# #
# url_mono = 'https://api.monobank.ua/bank/currency'
# mono = requests.get(url_mono)
# url_pb = 'https://api.privatbank.ua/p24api/pubinfo?' \
#          'json&exchange&coursid=5&#39'
# privat = requests.get(url_pb)
#
# print('-' * 50)
# print('|             |  PRIVAT \t|  MONOBANK |')
# print('-' * 50)
# print('|DOLL USA sale|', privat.json()[1]['sale'], '\t|',
#       mono.json()[0]['rateSell'], '\t|')
# print('|DOLL USA buy |', privat.json()[1]['buy'], '\t|',
#       mono.json()[0]['rateBuy'], '\t|')
# print('|EURO sale    |', privat.json()[0]['sale'], '\t|',
#       mono.json()[1]['rateSell'], '\t|')
# print('|EURO buy     |', privat.json()[0]['buy'], '\t|',
#       mono.json()[1]['rateBuy'], '\t|')
#
# input("??????? Enter ??? ??????")
# #
# #
# #
# fake = Faker(locale='ru')
#
# print(*dir(fake), sep='\n')
#
# # print(fake.word())
# # print(type(fake.name()), fake.name())
# f = fake.name()
# print(f)
# name = f.split()[0]
# surname = f.split()[1]
# print('name :', name)
# print('surname :', surname)
#
# #
# #
# url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"
#
# payload = {
#     "from": "auto",
#     "to": "en",
#     "text": "xin ch�o"
# }
# headers = {
#     "content-type": "application/x-www-form-urlencoded",
#     "X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
#     "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
# }
#
# response = requests.post(url, data=payload, headers=headers)
#
# print(response.json())
# #
# #
# #
# # fake = Faker()
# # print(fake.first_name(), fake.last_name(), fake.words(7))
# #
# # print(*dir(fake), sep='\n')
#
#
# # print(__name__)


# text = 'Hello, world!'
#
# print(f' ? ?????? ????? ?????: {text}')
#


# a = [1, 2]
# print(*dir(a), sep='\n')

# for i in range(5):
#     for j in range(5):
#         print(i, '-', j)


# l = [1, 2, 3]
# l.append(999)
#
# l1 = l.append(999)
# print(l)
# print(l1)
#
# def my_func(text):
#     print(text)
#     return sym
#
#
#
#
# d = my_func('Hello')
# print(d)


# # ?????? ???? ? ??????? ??????
# input_data = [
#     "??????????1 ????1 5",
#     "??????????2 ?????1 2",
#     "??????????1 ???2 3",
#     "??????????3 ?????2 1",
#     "??????????2 ????3 4",
# ]
#
# # ????????? ???????? ??? ?????????? ?????????? ??? ??????????? ?? ??????
# customer_data = {}
#
# # ?????????? ?????? ???? ?? ?????? ?????? ?? ?????????? ????? ?????
# for line in input_data:
#     parts = line.split()
#     customer = parts[0]
#     product = parts[1]
#     quantity = int(parts[2])
#
#     # ????????? ??????? ?? ?????????? ??? ????? ?? ????????
#     if customer not in customer_data:
#         customer_data[customer] = {}
#     if product not in customer_data[customer]:
#         customer_data[customer][product] = 0
#     customer_data[customer][product] += quantity
#
# # ?????????? ???????? ?? ????? ??????? ? ????????????????? ???????
# sorted_customers = sorted(customer_data.keys())
# for customer in sorted_customers:
#     print(customer)
#     sorted_products = sorted(customer_data[customer].keys())
#     for product in sorted_products:
#         print(f"    {product}: {customer_data[customer][product]}")
#

# a = 8
#
# result = 'Ukraine' if a == 1 else 'France'
#
# print(result)


# for i in range(32, 256):
#     print(i, '->', chr(i), '->', chr(i - 32))
# #
#
# def capitalize(symbol):
#     return chr(ord(symbol) - 32)
#
#
# text = input('??????? ????? ? ????????? : ').split()
# # print(text)
# for i in text:
#     print(capitalize(i[0]) + i[1:], end=' ')


# raise TypeError


# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
#
# print(l1 == l2)
# print(l1 is l2)
#
# print(id(l1))
# print(id(l2))
