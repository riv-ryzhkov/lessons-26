##########################################################
######## Використання вбудованих функцій #################

# variable = input('Введіть ціле число : ')
# print(variable)
# print('type   : ', type(variable))
# print('id     : ', id(variable))
# print('len    : ', len(variable))
# print('int    : ', int(variable))
# print('float  : ', float(variable))
# print('bool   : ', bool(variable))
# print('list   : ', list(variable))
# print('sum    : ', sum([1, 2, 3, 4, 5]))
# print('='*80)
# ................................

# .....................................
#
# print(*dir(variable), sep='\n')

#############################################################
######## Використання функцій зовнішніх модулів #############

import math
# from math import sin, cos
# from math import *
# from math import sin as sinus

#
#
# result = math.cos(3.14)
# result = sinh(3.14)
# result = sinh(3.14)
# result = sin(3.14)
#
# print(result)
#
# # pip install requests
# # pip install bs4


#########################################################################
########### Функції, що створені користувачем особисто ##################

# def say_hello():  # Процедура
#     print('Hello!')
#     return 'Hello, world!'
#
#
# print(say_hello())

# ???????????????
# say_hello()


###########################################

#
# def get_name():  # Функція
#     name = input('What is your name : ')
#     return name
#
#
# def say_hello(name):  # Процедура з аргументом
#     print(f'Hello, {name}!')
#
#
# my_name = get_name()
# # print('my_name =', my_name)
# say_hello(my_name)
#
# # ????????????????????????????????
# # print(say_hello('Mike'))
# #
# # # ...............................
# say_hello(get_name())


##########################################

# def my_sum(my_list):  # Функція з аргументом
#     summa = 0
#     for element in my_list:
#         summa += element
#     return summa
#
#
# my_list = [1, 2, 3, 4, 5]
# print('Result   : ', my_sum(my_list))



# !!!!!!!!!!!!!!!!!!! Зверніть увагу !!!!!!!!!!!!!!!!!!!!
# !!! ДОТРИМУЙТЕСЬ ВИМОГ РЕР-8 ПРИ РОБОТІ З ФУНКЦІЯМИ !!!
"""

PEP 8 - це стандартний документ Python,
який визначає рекомендації щодо оформлення коду в Python.
Дотримання цих вимог PEP 8 сприяє створенню чистого,
консистентного та легкозрозумілого коду,
що полегшує його розуміння, підтримку та співпрацю з іншими розробниками.

Основні правила РЕР8 для функцій:

1. Іменування функцій.
Імена функцій повинні бути написані малими літерами,
і слова мають бути розділені знаками підкреслення (_).
Наприклад, my_function(), а не MyFunction() або myfunction().

2. Вибір ім'я для функції.
Уникайте використання у назвах функцій зарезервованих слів,
це може привести до руйнування програми.
"""

# def my_sum(a, b):
#     return a + b
#
#
# a, b = 2, 3
# print('Result a + b =', my_sum(a, b))
#
# my_list = [1, 2, 3, 4, 5]
# print('Result sum()  = ', sum(my_list))


"""
3. Відокремлення функцій.
Функції повинні бути визначені та викликані з належним відокремленням
від інших функцій та коду. Використовуйте порожній рядок між функціями.

4. Уникайте зайвої складності.
Функції повинні бути невеликими і виконувати одну конкретну задачу.
Уникайте зайвої складності та занадто глибоких вкладень в функціях.

5. Документування функцій.
Кожна функція повинна бути документована за допомогою рядків документації (docstrings),
які починаються з потрійних подвійних лапок. Це дозволяє зрозуміти призначення функції,
типи її аргументів і поверненого значення.

тощо... (дивись документацію РЕР8).
# """

###########################################################
######### Псевдоніми та перевизначення функцій ############

# my_list = [1, 2, 3]
#
# summa = sum(my_list)  # function sum()
# print(type(summa))

# my_sum = sum
# print(my_sum(my_list))
# print(sum(my_list))

# .....................

# def foo():
#     return 'Працює функція foo()'
#
#
# result = foo()
# hello = foo()
# print('hello  ->', hello)
# print('result ->', result)
# print('foo()  ->', foo())

##########################################

# def foo(a, b):
#     res = a + b
#     return f'Працює функція foo() : {res}'
#
#
# result = foo
# hello = foo
# print('hello  ->', hello(5, 6))
# print('result ->', result(5, 6))
# print('foo()  ->', foo(5, 6))


###################################################################
######## Аргументи функцій (позиційні, ключові, за умовченням) ####

# def my_func(name, surname, age, city):
#     print('Данні про користувача :')
#     print("Ім'я       :", name)
#     print("Призвище   :", surname)
#     print("Вік        :", name)
#     print("Мешкання   :", city)
#     return [name, surname, age, city]


# personal_date = my_func('Max', 'Koval', '25', 'Kiev')
# personal_date = my_func('Max', 'Koval', '25')
# personal_date = my_func('Kiev', 'Max', 'Koval', '25')
# personal_date = my_func('Kiev')
# personal_date = my_func(city='Kiev')
# personal_date = my_func(city='Kiev', age=25, name='Max', surname='Koval')

# print('\n', *personal_date)

#####################################################################

# def my_func(name: str, surname: str, age: int, city: str) -> list:
#     """
#     The function outputs the information about user:
#     name, surname, age and city.
#     The function returns list with full information in list
#     """
#     print('Данні про користувача :')
#     print("Ім'я       :", name)
#     print("Призвище   :", surname)
#     print("Вік        :", name)
#     print("Мешкання   :", city)
#     return [name, surname, age, city]

#####################################################################

# def my_func(name='NoName', surname='NoSurname', age=18, city='NoCity') -> list:
#     """
#     The function outputs the information about user:
#     name, surname, age and city.
#     The function returns list with full information in list
#     """
#     print('Данні про користувача :')
#     print("Ім'я       :", name)
#     print("Призвище   :", surname)
#     print("Вік        :", name)
#     print("Мешкання   :", city)
#     return [name, surname, age, city]



##############################################################
######### Функції з необмеженною кількісттю аргументів #######

# def my_sum(a=0, b=0, c=0, d=0):
#     return a + b + c + d
#
#
# print('my_sum = ', my_sum(3, 4, 7, 2))
# print('my_sum = ', my_sum(3, 4))
# print('my_sum = ', my_sum(3, 4, 5))
#
# # ..............................
#
# # print('my_sum = ', my_sum(3, 4, 5, 6, 7, 8))
# # print('my_sum = ', my_sum(5, 6, 8, 9, 6, 7, 8, 9, 9, 0, 4, 6, 7, 9))

####################  *args  #######################


# def my_sum(*args):
#     result = 0
#     print(type(args), args)
#     for i in args:
#         result += i
#     return result
#
#
# print('my_sum = ', my_sum(5, 6, 8, 9, 6, 7, 8, 9, 9, 0, 4, 6, 7, 9))


####################  *kwargs  #######################

# def my_function(*args, **kwargs):
#
#     print(type(args), args)
#     print(type(kwargs), kwargs)
#
#     summa = 0
#     for i in args:
#         summa += i
#
#     result = {'summa': summa}
#
#     for key, val in kwargs.items():
#         result[key] = summa * val
#
#     return result
#
#
# print('my_function = ', my_function(5, 6, 4, 6, 7, 9, duble=2, triple=3, quatro=4))

##################################################################
###### Перевизначення змінних !!!!!!!!!!!!

# i = 100
# print('i before -> ', i)
#
# for i in range(5):
#     pass
#
# print('i after ->', i)


###################################################################
############## global ############################################


# def foo():
#     global i
#     # for i in range(5):
#     #     print('i =', i)
#     i = 0
#
#
# i = 100
# print('i before -> ', i)
# foo()
# print('i after ->', i)

#######  краще!!!  ####################

# def foo(i):
#     for i in range(5):
#         i += 1
#         print('i =', i)
#     return i
#
#
# i = 100
# print('i before -> ', i)
# i = foo(i)
# print('i after ->', i)


#################### globals()/locals() #######################

# variable = 'Hello, world'
# num = 3.14159
# my_list = [1, 2, 3]
# i = 100
#
# fix_globals = dict(globals())
# print(type(fix_globals))
# for key, val in fix_globals.items():
#     print(key, '--->', val)

###########################################

# def foo():
#     loc = 34
#     # global i
#     for i in range(5):
#         print('i =', i)
#
#     print('Globals() :')
#     fix_globals = dict(globals())
#     for key, val in fix_globals.items():
#         print(key, '--->', val)
#     print('='*80)
#
#     print('Locals() :')
#     fix_locals = dict(locals())
#     for key, val in fix_locals.items():
#         print(key, '--->', val)
#
#     return i
#
#
# i = 100
# a = 5
# b = 8
# print('i before -> ', i)
# foo()
# print('i after ->', i)


####################################################
############## global  nonlocal ####################

# def foo():
#     i = 70
#
#     def inner_foo():
#         # i = 50
#         # global i
#         nonlocal i
#         i += 25
#         print('in inner_foo() -->', i)
#
#     inner_foo()
#     print('in foo() -->', i)
#
# i = 100
# print('start ->', i)
# foo()
# print('end --->', i)

#############################################
# ?????????????????????????

# def foo():
#
#     def inner_func():
#         a = 0
#         print(a)
#
#     inner_func()
#     return 'Hello!'
#
# result = foo()
# print(result)
# inner_func()

#######################################



#########################################
############## LAMBDA ###################


# def sum_two(a, b):
#     return a + b
#
#
# print(sum_two(4, 5))
#
#
# my_func = lambda a, b: a + b
# print(my_func(4, 5))
#
# #################################
#
# print((lambda a, b: a + b)(4, 5))

#########################################

# say_hi = lambda name: f'Hi, {name}!'
# print(say_hi('Alex'))
#
# #########################################
# print(f'Hi, {input('name =')}!')
#########################################################

# 5! = 1 * 2 * 3 * 4 * 5

def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
        # print(i, '! = ', res)
    return res


# print(factorial(3))
# print(factorial(5))
# print(factorial(7))
# print(factorial(10))
# print(factorial(20))



# for i in range(1, int(input('n = '))+1):
#     print(f'factorial {i}=', factorial(i))



# !!!!!!!!!!!!!!! RECURTION !!!!!!!!!!!!!!!!!!!!!

# def short_story(i=0):
#
#     # print("У попа був собака, він його любив.")
#     # print("Той з'їв шматок м'яса, він його вбив,")
#     # print("В землю закопав та напис написав:")
#     print('Dog story...')
#     i += 1
#     if i < 5:
#         short_story(i)
#     # short_story(i)
#
#
# short_story()

###########################################

# def factorial(n: int): # 1 * 2 * 3 * 4 * 5 = res
#     res = 1
#     for i in range(2, n + 1):
#         print(i-1, '! =', res)
#         res *= i
#     return res
#
#
# def factorial1(n: int):                  # 5 * (4 * (3 * (2 * (1)))) = res
#     print('n = ', n)
#     if n == 1:
#         return 1
#     else:
#         return n * factorial1(n - 1)     #(  5 * 4! # (4 * 3! # (3 * 2! #(2 * 1! #
#     #                                     120     24      6        2        1
#
#
# n = int(input('n = '))
# print('factorial', n, '! =', factorial(n))
# print('factorial1', n, '! =', factorial1(n))

#############################################
########## sum_digits() #####################

# def sum_digits(number:int) -> int:
#     if number < 10:
#         return number
#     num = number // 10
#     result = number % 10
#     result += sum_digits(num)
#     return result
#
#
# print(sum_digits(12345656457485687))

######################################

# def print_bin(n):  # 9 4 2 1 0   #        1001
#     if n == 0:
#         return
#     print_bin(n//2)
#     print(n % 2, end="")
#
#
# print_bin(93426357635748486587786)
############################################



# !!!!!!!!!!!!!! HomeWork REVERS !!!!!!!!!!!!!!!!


def reverse():
    symbol = int(input('x= '))
    if symbol:
        reverse()    #  --> 1 ( --> 2 (--> 3 (--> 4 (--> 5 (--> 0)))))
    print(symbol)    #  0 5 4 3 2 1


reverse()


############################# END

