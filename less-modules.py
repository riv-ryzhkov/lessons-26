
# import func
#
#
# text = 'Hello, world!'
#
# # print(*dir(func), sep='\n')
#
# func.pr1(text)
# func.pr2(text)
# func.pr3(text)





from my_code import *
import my_code


# print(*dir(code), sep='\n')
# print(code.psw)

# word = input('psw = ')
# while word != psw:
#     word = input('psw = ')
# print('Доступ відкрито!!!!!')




# import math
#
#
# print(math.sin(345))
# print(math.cos(345))
# print(dir(math))
# print(*dir(math), sep='\n')


import math
# from math import *
# from math import sin, pi, cosh, asinh
from math import sin as my_sinus
from math import sin as my_sinus
from numpy import sin as num_sinus

# print(sin(34))
# print(cosh(34))
# print(pi)

# print(my_sinus(34))
# print(num_sinus(34))




# from bs4 import BeautifulSoup
import bs4
from bs4 import BeautifulSoup as BS
#
# print(*dir(bs4), sep='\n')
# res = BeautifulSoup()
# result = BS()


# print(my_sinus(56))
# print(num_sinus(56))
# print(sin(56))



# print(sin(456))
# print(cos(456))
# print(pi)
# print(asinh(.35))
# BeautifulSoup()
# print(*dir(bs4), sep='\n')










# from func import pr1 as my_new_print
# from func import pr2 as my_old_print
#
#
# my_new_print('Hello!')
# my_old_print('Hello!')


#####################    Module   colorama  ########################
# from colorama import Fore
#
# # print(*dir(Fore), sep='\n')
#
# print(Fore.GREEN + 'Цей текст буде зеленим')
# print(Fore.LIGHTGREEN_EX + 'Цей текст буде яскраво зеленим')
# print(Fore.RED + 'Цей текст буде червоним')
# print(Fore.BLUE + 'Цей текст буде блакитним')
# print(Fore.LIGHTMAGENTA_EX + 'А цей текст отакий )))')
# print(Fore.LIGHTBLACK_EX + 'А цей текст отакий )))')
# print(Fore.YELLOW + 'А цей текст отакий )))')
# print(Fore.LIGHTYELLOW_EX + 'А цей текст отакий )))')
# print(Fore.RESET + 'А цей текст отакий )))')
# print(Fore.RED + 'Цей текст буде зеленим')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print(Fore.RESET + 'А цей текст отакий )))')

#########################################################
########### shutil ######################################
#########################################################



import shutil

# print(*dir(shutil), sep='\n')

# print(shutil.disk_usage('.'))
# total_b, used_b, free_b = shutil.disk_usage('.')
#
# gb = 10 ** 9
# mb = 10 ** 6
#
# print('Total: {:6.2f} GB'.format(total_b / gb))
# print('Used: {:6.2f} GB'.format(used_b / gb))
# print('Free : {:6.2f} GB'.format(free_b / gb))
#
# print(f'Total: {total_b / gb:6.2f} GB')
# print(f'Used : {used_b / gb:6.2f} GB')
# print(f'Free : {free_b / gb:6.2f} GB')






#####################    Module   Time  ########################


import time


# print(*dir(time), sep='\n')  # можна подивитися всі атрибути модуля time

# print('Секунди з 01-01-1970 :', time.time())  # кількість секунд від початку епохи Unix
# print('Поточний час :', time.ctime())  # поточна дата і час у зручному форматі
#
# t = 3  # кількість секунд для паузи
#
# print("\nПрограма запущена...")
# time.sleep(t)  # призупиняє виконання програми на t секунд
# print(str(t) + " секунд минуло.\n")
#
# print('Секунди з 01-01-1970 :', time.time())
# print('Поточний час :', time.ctime())
#
# t = 3
# result = 0  # змінна для накопичення виміряного часу

# for i in range(1, t + 1):
#     start = time.time()
#     # час початку (може бути неточним, якщо змінюється системний час)
#
#     time.sleep(t)  # можна додати затримку для перевірки
#
#     finish = time.time()  # час завершення
#     result += finish - start  # додаємо різницю до загального результату
#     print("Час роботи (time.time): " + str(result) + " секунд.\n")

# Використання монотонного таймера (не залежить від змін системного часу)
# start = time.monotonic()
# time.sleep(3)
# result = time.monotonic() - start
# print("Час роботи (monotonic): {}".format(result) + " секунд.\n")

# # Отримання локального часу у вигляді структури
# print(time.localtime())
##################################################


# Форматування дати у читабельний рядок
# time_ = time.strftime("%A %B %d, %Y", time.localtime())
# time_ = time.strftime("%a %b %d, %y", time.localtime())
# time_ = time.strftime("Сьогодні %A - %d %B %Y року", time.localtime())
#
# print(f'time.strftime : {time_}', type(time_))
# #
#
# # Перетворення структури часу назад у секунди від епохи
# print('time.mktime :', time.mktime(time.localtime()))
#
# # Поточний час у секундах від 01-01-1970
# print(time.time())
#
# # Зсув локального часу відносно UTC (у секундах)
# print('time.timezone :', time.timezone)
# print('time.timezone :', time.timezone/(3600), "годин.")




###################   timeit   #################################
# import time
# import timeit  # модуль для вимірювання часу виконання невеликих фрагментів коду
#
#
#
# # Варіант 1 — використання циклу for
# code_loop = """
# total = 0
# for i in range(1000):
#     total += i
# """
#
# # Варіант 2 — використання вбудованої функції sum()
# code_sum = "sum(range(1000))"
#
#
# # Порівняння часу виконання
# # number=100000 означає, що код буде виконаний 100000 разів
# num = 100_000
# time_loop = timeit.timeit(stmt=code_loop, number=num)
# time_sum = timeit.timeit(stmt=code_sum, number=num)
#
# print(f"цикл for          -> {time_loop:.6f} секунд")
# print(f"sum(range(1000))  -> {time_sum:.6f} секунд")
#
# print('.'*40)
# # # ##################################
# # # # ....................................
# #
# # # Вимірювання часу вручну за допомогою монотонного таймера
# # # # (не залежить від змін системного часу)
# start = time.monotonic()
#
# for t in range(100_000):
#     total = 0
#     for i in range(1000):
#         total += i
#
# result = time.monotonic() - start
# print("Program FOR : {}".format(result) + " секунд.")
#
# # ....................................
#
# # Аналогічне вимірювання для функції sum()
# start = time.monotonic()
#
# for t in range(100_000):
#     code_sum = sum(range(1000))
#
# result = time.monotonic() - start
# print("Program SUM : {}".format(result) + " секунд.\n")
# # #

####################################################


############## Модуль DateTime ########################
import datetime  # модуль для роботи з датою та часом

# Вивести всі атрибути та методи класу datetime
# print(*dir(datetime.datetime), sep='\n')

# ....................................

# Створення конкретної дати
# a = datetime.date(2026, 3, 20)
# print('a :', a, type(a))  # об'єкт типу date

# # ....................................
#
# print(datetime.datetime.now()-datetime.datetime(1964,11,6))

# # Отримання поточної дати
# a = datetime.date.today()
# print('a today :', a)
# # # #
# print(type(a), a)
# print(*dir(a), sep='\n')  # список методів та властивостей об'єкта date

# # ....................................
#
# # Доступ до окремих компонентів дати
# print('year :', a.year)
# print('month :', a.month)
# print('day :', a.day)
# print('week_day :', a.weekday())  # день тижня (0 — понеділок, 6 — неділя)
# #
# # # ....................................
# #
# # Створення об'єкта часу
# a1 = datetime.time(9, 15, 45, 345)
# print('time :', a1, type(a1))
# #
# # # Створення різних варіантів часу
# a = datetime.time(23, 7, 45)
# b = datetime.time(9, 33)
# c = datetime.time(14)
#
# print('time :', a)
# print('time :', b)
# print('time :', c)

# # # ....................................
# #
# # # Отримання окремих компонентів часу
# a = datetime.time(12, 31, 29, 123487)
# print('time :', a)
# print('hour :', a.hour)
# print('minute :', a.minute)
# print('seconds :', a.second)
# print('microsecond :', a.microsecond)

# # ....................................
#
# Поточна дата і час
# a = datetime.datetime.today()
# b = datetime.datetime.now()  # зазвичай працює швидше
# print('a(today) :', a)
# print('now      :', b)

# ....................................

# Форматування дати та часу у рядок
# a = datetime.datetime.today().strftime("%a  %d / %m / %y")
# b = datetime.datetime.now().strftime("Сьогодні %A %D %Y: %H:%M:%S")
# c = datetime.datetime.now().strftime("Сьогодні %A %d.%m.%Y %H:%M:%S")
#
# print('today().strftime :', a)
# print('now().strftime :', b)
# print('now().strftime :', c)

# ....................................

# Виведення поточного року
# print(datetime.datetime.now().year)

# ....................................

# Об'єднання окремої дати та часу в один об'єкт datetime
# a = datetime.date(2019, 4, 22)
# b = datetime.time(22, 15, 30)
# c = datetime.datetime.combine(a, b)
#
# print('combine date :', a, type(a))
# print('combine time :', b, type(b))
# print('combine datetime :', c, type(c))


#########################################################
############## DateTime.DateTime ########################
from datetime import datetime  # імпортуємо клас datetime

# # Поточна дата і час
# a = datetime.now()
# # #
# # # # Створення конкретної дати (24 лютого 2022 року)
# # b = datetime(2022, 2, 24, 5)
# #
# # # Різниця між двома датами
# # # Результат — об'єкт типу timedelta
# # c = a - b
# # #
# # print(type(a), a)  # тип і значення поточної дати
# # print(type(b), b)  # тип і значення заданої дати
# # print(type(c), c)  # тип і значення різниці (timedelta)
# #
# # # Додавання інтервалу часу (timedelta) до дати
# # d = a + c
# # print(type(d), d)
# #
# # # # ....................................
# # #
# print('a :', a, type(a))
# # # #
# # # # # Перетворення об'єкта datetime у рядок
# r = str(a)
# print('r :', r, type(r))
# # # #
# # # # # Витяг частини рядка (місяць і день)
# print(r[8:10] + '-' + r[5:7])



############## DateTime.timedelta ########################

from datetime import datetime, timedelta  # імпортуємо класи для роботи з датою та інтервалами часу

# Створення об'єкта timedelta (інтервал часу)
# a = timedelta(days=7, hours=2, minutes=23, seconds=22)

# Перезапис змінної — тепер інтервал лише 2 дні
# a = timedelta(days=2)
# #
# print(a, type(a))  # вивід інтервалу та його типу
# # #
# # # # Додавання інтервалу часу до поточної дати
# b = datetime.now() + a
# print(b)
# # # #
# # # # Різниця між поточною датою і заданою датою
# d1 = datetime(1964, 11, 6)
# d = datetime.now()
# delta = d - d1  # результат — об'єкт timedelta
# print(delta)
#
# ################################

# from datetime import datetime, timedelta  # повторний імпорт (не обов'язковий, якщо вже імпортовано)
#
# # Створення конкретної дати
# a = datetime(2024, 10, 9)
#
# # Поточна дата і час
# n = datetime.now()
#
# # Створення складного інтервалу часу
# b = timedelta(
#     weeks=3,
#     days=5,
#     hours=9,
#     minutes=54,
#     seconds=17,
#     milliseconds=123,
#     microseconds=234,
# )
#
# print('a :', a)
# print('b :', b)
# #
# # # Додавання інтервалу до дати
# c = a + b
# print('a + b :', c)
#
# print('now :', n)
#
# # Різниця між датами
# print('n - a :', n - a)
# #
# # Додавати дві дати напряму не можна (буде помилка)
# # print('a + n :', a + n)
# #
# # # Обчислення різниці між поточним часом та новою датою
# delta = n - c
# print('delta :', delta, type(delta))
# # #
# # # Арифметичні операції з timedelta
# print('delta - delta :', delta - delta, type(delta))   # множення інтервалу
# print('delta + delta :', delta + delta, type(delta))   # множення інтервалу
# print('delta * 2     :', delta * 2, type(delta))   # множення інтервалу
# print('delta / 3     :', delta / 3, type(delta))   # ділення (результат — timedelta)
# print('delta // 3    :', delta // 3, type(delta))  # цілочисельне ділення





########################################################
######### Модуль collections ################
############## Counter #################

from collections import Counter
import collections  # модуль із додатковими структурами даних

# Вивести всі атрибути та класи модуля collections
# print(*dir(collections), sep='\n')

# --------------------------------------

# Створення Counter для підрахунку символів у рядку
# c = Counter('tdgtfkjlbhj,bvjhgfsdgsfxchvjghfxzghgghfxhgvkhgfxhg')
# print('c : ', c, type(c))  # Counter — це підклас словника
# #
# # # Вивести 5 найчастіших елементів
# print('most : ', c.most_common(4), type(c.most_common(4)))
# # #
# # # # # # # Перетворення результату most_common у звичайний словник
# dc = dict(c.most_common(4))
# print(dc, type(dc))

# --------------------------------------
#
# # Підрахунок елементів у списку
# lst = [5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7]
# c1 = Counter(lst)
# print(c1)
# # Перетворення Counter у звичайний словник
# c2 = dict(c1)
# print('dict : ', c2, type(c2))
# # #
# # # Додавання нових елементів у словник
# c2[10] = 7
# c2[11] = 7
# #
# print('dict : ', c2, type(c2))
# # #
# # # # Найчастіші 5 елементів
# print('most : ', c1.most_common(5))

# # --------------------------------------
#
# Великий текст для аналізу
text = '''
The Republican candidate for Virginia attorney general,
Cuban American Jason Miyares, was also leading that vote count.
And Republicans seemed to be closing in on control
of the state's House of Delegates.

In other elections across the US on Tuesday:

Republican challenger Jack Ciattarelli had a narrow lead
over New Jersey's Democratic Governor Phil Murphy, with 88%
of votes reported
Amid surging crime, Minneapolis voters rejected a proposal
to replace the city's police department with a new Department
of Public Safety, more than a year after the murder of George
Floyd by an officer
As expected, Democrat Eric Adams won New York City's mayoral
election to replace his party colleague Bill de Blasio;
Republican challenger Curtis Sliwa was involved in an argument
at his polling station after turning up to vote with a pet cat
and being told his furry friend Gizmo could not enter
Pittsburgh picked its first black mayor, Democrat Ed Gainey
'''
# text_clear = []
# symb = [',', '.', '"', '\n', '!', '?', '(', ')']
# for i in text:
#     if i not in symb:
#         text_clear.append(i)
# text = ''.join(text_clear)
#
# # print(text)
# #
# # # Перетворення тексту у верхній регістр та розбиття на слова
# words = text.upper().split()
# print(words)
#
# # Підрахунок кількості кожного слова
# res = Counter(words)
# print(res)
# print(type(res))

# Counter є підкласом dict

# print(isinstance(res, dict), '!!!!!!!!!!!!!!!!!!!')
# print(*dir(res), sep='\n')
# print(isinstance(False, int))
# print(type(False))
# # print('counter : ', type(res))
#
# print((2>3)*10)

# # Розділення ключів і значень у два окремі списки
# words = []
# counts = []
#
# for key, vol in res.items():
#     words.append(key)
#     counts.append(vol)
#
# print(len(words), words)
# print(len(counts), counts)
# #
# # # 5 найчастіших слів
# print('res.most_common : ', res.most_common(5))
#
# # Сортування елементів за кількістю (за спаданням)
# print('sorted : ')
# print(*sorted(res.items(), key=lambda x: x[1], reverse=True), sep='\n')
#
# # # Загальна кількість слів у тексті
# print('sum : ', sum(res.values()))
#
# # Пари (слово, кількість)
# print('item : ', res.items())
#
# # Повний Counter
# print('res : ', type(res), res)
#
# # Кількість унікальних слів
# print(len(res))

############### end of Counter ##################


###########  defaultdict ################
from collections import defaultdict  # імпортуємо defaultdict

# --------------------------------------
# Звичайний словник (dict)

# d = {}
# print(d, type(d))
#
# # Якщо звернутися до неіснуючого ключа через d['key'],
# # виникне помилка KeyError
# # print(d['key'])
# d['key'] = 55
# Метод get() повертає None, якщо ключа не існує
# print(d.get('key', 'No key!!!'))

# # --------------------------------------
# # defaultdict автоматично створює значення
# # для нового (раніше неіснуючого) ключа.
# # Тип значення задається як аргумент (тут str).
#
#
# d = defaultdict(str)
# d = defaultdict(int)
# d = defaultdict(list)
# # #
# # # # Додаємо значення вручну
# d['key1'] = 657
# print(d)
# #
# # # Звернення до неіснуючого ключа
# # # автоматично створить його зі значенням за замовчуванням
# # # для str це порожній рядок ''
# print(d['Pupkin'])
# #
# # # # Тепер ключ 'Pupkin' вже існує у словнику
# print(d)
# # # #
# # # # # # # Додаємо ще один ключ
# d['key'] = 'Hello'
# print(d)
# # #
# # # # При зверненні до нових неіснуючих ключів
# # # # вони автоматично створюються з порожнім рядком
# print(d['key'])
# print(d['key2'])
# print(d['key3'])
# # # #
# # # # # Перевіряємо кінцевий стан словника
# print(d)



######### namedtuple ----------  ##################

# from collections import namedtuple
#
# # Створюємо тип даних 'fruit' з полями: number, variety, color
# Fruit = namedtuple('Fruit', 'number variety color')
#
# # --------------------------------------
# # Варіант 1: створення через список
# guava_data = [2, 'HoneyCrisp', 'green']
#
# guava1 = Fruit(5, 'HoneyCrisp', 'red')
# guava = Fruit(*guava_data)  # розпаковка списку у аргументи
#
# print(guava, type(guava))
# print(guava1, type(guava1))
#
# # Варіант 2: створення через словник
# apple_data = {'number': 7, 'variety': 'Granny Smith', 'color': 'red'}
# apple = Fruit(**apple_data)  # розпаковка словника у аргументи
# print(apple)
#
# # --------------------------------------
# # Доступ до полів
# print(f"Гуава: {guava.variety}, колір: {guava.color}, кількість: {guava.number}")
# print(f"Яблуко: {apple.variety}, колір: {apple.color}, кількість: {apple.number}")



############### end of Collections ##################


from faker import Faker
import csv
import faker  # модуль faker для генерації випадкових даних

# Виведення всіх атрибутів модуля faker
# print(*dir(faker), sep='\n')

# --------------------------------------
# Створюємо об'єкт Faker
# fake = Faker()

# Генерація випадкового імені
# print(fake.name())

# Вивід атрибутів об'єкта fake
# print(*dir(fake), len(dir(fake)), sep='\n')
#
# # --------------------------------------
# # Використання локалізації української мови
# fake = Faker(locale='uk')
# print(fake.name())
#
# print(*dir(fake), sep='\n')
#
# # Приклади генерації різних даних
# print(fake.name())
# print(fake.address())
# print(fake.email())
# print(fake.phone_number())
#########################################################
# # --------------------------------------
# Приклади з різними локалями
# fake = Faker(locale="en_GB")
# fake = Faker("zh_CN")
# fake = Faker(locale="uk_UA")
# print(fake.name())
# print(fake.address())

# # --------------------------------------
# # Генерація детальної інформації українською
fake =Faker(locale="uk_UA")

# print('prefix :', fake.prefix())  # титул
# print('name :', fake.name())      # ім'я
# print('id :', fake.ssn())         # ідентифікаційний номер
# print('country :', fake.country())
# # print(fake.state())  # для USA
# print('city :', fake.city())
# # print(fake.zipcode())  # для USA
# print('address :', fake.address())
# print('job :', fake.job())        # професія
# print('company :', fake.company())
# print('phone number :', fake.phone_number())
# print('email :', fake.email())
# print('url :', fake.url())
# print('date :', fake.date())
# print('time :', fake.time())
# print('word :', fake.words(5))
# print('word :', fake.word())
# print('sentences :', fake.sentences(5))
# print('text :', fake.text())
# print('year :', fake.year())
# print('month :', fake.month())
#
# # --------------------------------------
# Генерація шаблонних даних
# print('% num 1-9 :', fake.bothify('%%%%%-%%%%%-%%%%%%-%%%%%%'))  # % — цифри без 0
# print('# numbers :', fake.bothify('+(380)67 ### ## ##'))         # # — цифри
# print('? letters :', fake.bothify('??????????????????????'))      # ? — букви
# print('phone :', fake.numerify(text='+##(###)###-##-##'))
# print('ISBN : ', fake.bothify(text='ISBN ????-%%%%-####-##-##'))

# # --------------------------------------
# # Генерація простого профілю
# p = fake.simple_profile()
# print('#' * 80)
# print(*p, sep=' : ')
# print('#' * 80)
# print(type(p), p)
#
# # Доступ до окремих елементів профілю
# print('username  :', p['username'])
# print('name      :', p['name'])
# print('sex       :', p['sex'])
# print('address   :', p['address'])
# print('mail      :', p['mail'])
# print('birthdate :', p['birthdate'])
# print('='*80)
# #
# print('birthdate :', fake.simple_profile()['birthdate'])
#
# # --------------------------------------
# Генерація унікальних імен
fake = Faker(locale="uk_UA")
# name = []
# for i in range(187):  # кількість унікальних імен # 187(uk)  401(ru)   676(en)
#     name.append(fake.unique.first_name())
#
# print(*name)
# print('len list =', len(name))
# print('len set =', len(set(name)))  # перевірка унікальності

# --------------------------------------
# Запис випадкових даних у CSV
# with open('faker.csv', 'w', newline='', encoding='utf-8') as f:
# with open('faker.csv', 'w', newline='', encoding='utf-8-sig') as f:
# # with open('faker.csv', 'w', newline='') as f:
#     wr = csv.writer(f, delimiter=';')
#     # Заголовки колонок
#     wr.writerow(['Name',
#                  'Surname',
#                  'job',
#                  'address',
#                  'phone',
#                  'email',
#                  'credit_card_number',
#                  'credit_card_expire',
#                  'credit_card_security_code'])
#     for i in range(50):
#         # Розділення повного імені на ім'я та прізвище
#         f1 = fake.unique.name().split()
#         print(f1, type(f1))
#         fake_name = f1[0]
#         fake_surname = f1[1]
#         # Запис рядка у CSV
#         wr.writerow([fake_name,
#                      fake_surname,
#                      fake.job(),
#                      fake.unique.address(),
#                      fake.numerify(text='+##(###)###-##-##'),
#                      fake.unique.email(),
#                      fake.numerify(text='%%%% #### #### ####'),
#                      fake.credit_card_expire(),
#                      fake.credit_card_security_code()])
#

########################## END
# Memory

# import os
# import psutil
# import time
# import gc
#
# # Отримуємо об'єкт поточного процесу
# process = psutil.Process(os.getpid())
#
# def show_memory(stage):
#     """Функція для виведення використання пам'яті"""
#     mem = process.memory_info().rss / (10 ** 6)
#     print(stage, ":", round(mem,2), "MB")
#
# # Пам'ять на початку програми
# show_memory("Початкова пам'ять")
#
# time.sleep(2)
#
# # Створюємо великий список (виділяємо багато пам'яті)
# data = [i for i in range(15_000_000)]
#
# show_memory("Після створення великого списку")
#
# time.sleep(2)
#
# # Видаляємо список
# del data
#
# show_memory("Після видалення списку")
#
# time.sleep(2)
#
# # Примусовий запуск збирача сміття
# gc.collect()
#
# show_memory("Після виклику garbage collector")
#

#################################################

# import os
# import psutil
# import time
# import matplotlib.pyplot as plt
#
# # Отримуємо поточний процес
# process = psutil.Process(os.getpid())
#
# # Список для збереження значень пам'яті
# memory_values = []
#
# # Список для даних, які будуть поступово збільшувати пам'ять
# data = []
#
# plt.ion()  # режим інтерактивного графіка
#
# for i in range(30):
#
#     # Додаємо новий великий список (виділяємо пам'ять)
#     data.append([j for j in range(500000)])
#
#     # Отримуємо використання пам'яті
#     mem = process.memory_info().rss / (1024 * 1024)  # MB
#     memory_values.append(mem)
#
#     # Малюємо графік
#     plt.clf()
#     plt.plot(memory_values)
#     plt.xlabel("Крок програми")
#     plt.ylabel("Пам'ять (MB)")
#     plt.title("Зростання використання пам'яті Python")
#     plt.pause(0.5)
#
# plt.ioff()
# plt.show()


