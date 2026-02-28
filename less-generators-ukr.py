# # ########### ГЕНЕРАТОРИ: LIST-TUPLE-SET-DICT #############
#
# # Вивід символів ASCII від 0 до 255
# for i in range(256):
#     print(i, '->', chr(i))
#
# # Порівняння рядків у Python
# print('a'>'A')
#
# # --------------------------------------
# # Генерація списку символів від 'a' до 'm'
# list1 = [chr(i) for i in range(97, 110)]
# print(type(list1), list1)
#
# # --------------------------------------
# # Генерація кортежу чисел від 15 до 1
# tuple1 = tuple(i for i in range(15, 0, -1))
# print(type(tuple1), tuple1)
#
# # --------------------------------------
# # Генерація множини символів
# set1 = {chr(i) for i in range(97, 110)}
# print(type(set1), set1)
#
# # --------------------------------------
# # Генерація словника шляхом об'єднання списку та кортежу
# dict1 = {x: y for x, y in zip(list1, tuple1)}
# print(type(dict1), dict1)
#
# # --------------------------------------
# # Генератор символів від 'a' до 'm'
# gn = (chr(i) for i in range(97, 110))
# print(type(gn), gn)
#
# # Використання next() для отримання елементів генератора
# print(next(gn))
# print(next(gn))
# print(next(gn))
# print(list(gn))
# gn = (chr(i) for i in range(97, 110))
# print(list(gn))
# gn = (chr(i) for i in range(97, 110))
# print(next(gn))
#
# # --------------------------------------
# gn = (chr(i) for i in range(97, 110))
# var = next(gn)
# print('var=', var)
# print('var=', var)
# print('var=', var)
# print('var=', var)
# print(next(gn))
# print(next(gn))
# print(next(gn))
# print(list(gn))
# print(list(gn))
#
# # --------------------------------------
# gn = (i for i in range(97, 110))
# print(sum(gn))
# print(sum(gn))
# print(sum(i for i in range(97, 110)))
# print(sum(i for i in range(97, 110)))
# print(sum(i for i in range(97, 110)))
#
# # --------------------------------------
# l = []
# gen = (i for i in range(15, 0, -1))
# print(gen, type(gen))
# l.append(next(gen))
# l.append(next(gen))
# l.append(next(gen))
# print(l)
# l = list(gen)
# print(l)
# l = list(gen)
# print(l)
# gen = (i for i in range(15, 0, -1))
# print(list(gen))
#
# # --------------------------------------
# # Приклади генераторних функцій
# def even_numbers(n):
#     for i in range(2, n):
#         print('yield:')
#         yield i ** 2
#         print('!!!!!!!', i)
#         print('yield:')
#         yield i ** 3
#         print('**********', i)
#         print(':-)', 'i >>>', i)
#
# gen1 = even_numbers(7)
# print('1 step =', next(gen1))
# print('2 step =', next(gen1))
# print('3 step =', next(gen1))
# print('4 step =', next(gen1))
# print('last number :', next(gen1))
# print(next(gen1))
#
# # --------------------------------------
# # Генератор чисел Фібоначчі
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# n = 10
# fib = fibonacci(n)
# numbers = fibonacci(n)
# print(fib)
# print(numbers)
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# # print(list(fib))
# print('fib:', next(fib))
# print('fib:', next(fib))
# print('fib:', next(fib))
# print('fib:', next(fib))
# print('numbers:', next(numbers))
# print('numbers:', next(numbers))
# print('numbers:', next(numbers))
# print('numbers:', next(numbers))
# print('numbers:', next(numbers))
# print('fib:', next(fib))
# print('numbers:', next(numbers))
# print('fib:', next(fib))
# print('numbers:', next(numbers))
#
# for num in numbers:
#     print(num)
#
# for i in range(n):
#     print(i, '->', 'numbers =', next(numbers), 'fib =', next(fib))
#
# # --------------------------------------
# # Генератор чисел, кратних певному числу
# def divisible_by(divisor, n):
#     for i in range(1, n+1):
#         if i % divisor == 0:
#             yield i
#
# m, n = 5, 50
# numbers = divisible_by(m, n)
# print(numbers)
# while True:
#     try:
#         print(next(numbers))
#         input()
#     except StopIteration:
#         print('The Generation is over!')
#         break
#
# # --------------------------------------
# # Генератор факторіала
# def factorial(n: int):
#     res = i = 1
#     while i <= n:
#         res *= i
#         i += 1
#         yield res
#     return res
#
# print(factorial(5))
# print(factorial)
#
# fact = factorial(7)
# print(fact, type(fact))
# print(next(fact))
# print(next(fact))
# print(next(fact))
# print(next(fact))
# print(next(fact))
# print(next(fact))
# print(next(fact))
# print(list(fact))
#
# fact = factorial(9)
# print(list(fact))
# print(next(fact))
#
# fact = factorial(7)
# print(fact)
# print('1: ', next(fact))
# print('2: ', next(fact))
# print('3: ', next(fact))
# print('4: ', next(fact))
# fact1 = list(fact)
# print('fact1 = ', fact1, type(fact1))
# fact = factorial(7)
# fact5 = tuple(factorial(8))
# fact2 = list(fact)
# print('fact = ', fact, type(fact))
# print('fact2 = ', fact2, type(fact2))
# print('fact5 = ', fact5, type(fact5))
#
# # Вивід факторіалів через цикл
# n = 7
# fact = factorial(n)
# for i in range(1, n+1):
#     print(i, '! =', next(fact))
#
# # --------------------------------------
# n = 5
# fact = factorial(n)
# f = factorial(n)
# print(id(fact), list(fact))
# print(id(f), list(f))
# f = factorial(n)
# print(id(f), list(f))
#
# # --------------------------------------
# ############################################################
# # Генератори: MAP-ZIP-ENUMERATE-RANGE-ITEMS
#
# l1 = [str(i) for i in range(10)]
# gen = (i for i in range(10))
# print(l1)
#
# m = map(int, l1)
# print(m, type(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(tuple(m))
# print(next(m))
# print(list(m))
#
# en = range(100)
# z = zip(en, l1)
# print(z, type(z))
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
# print(list(z))
# print(next(z))
# print(list(z))
#
# e = enumerate(l1)
# print(e, type(e))
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))
# print(list(e))
# print(next(e))
# print(list(e))
#
# r = range(10)
# print(r, type(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(list(r))
# print(list(r))
# print(list(r))
# print(tuple(r))
# print(set(r))
#
# r = range(10)
# for i in r:
#     print(i, end=' ')
# print(list(r))
# for i in r:
#     print(i, end=' ')
# for i in r:
#     print(i, end=' ')
#
# print(dict1)
# d = (i for i in dict1.items())
# d = dict1.items()
# print(type(d), d)
# print(isinstance(d, list))
# # print(d[2])  # не працює, items() не підтримує індексування
# d = dict1.keys()
# d = dict1.values()
# print(next(d))
# print(next(d))
# print(list(d))
# print(list(d))
#
# # --------------------------------------
# import sys
#
# print('map : ', sys.getsizeof(m), m)
# print('zip : ', sys.getsizeof(z), z)
# print('enumerate : ', sys.getsizeof(e), e)
# print('range : ', sys.getsizeof(r), r)
# print('gen : ', sys.getsizeof(gen), gen)
#
# # --------------------------------------
# ###################################################################
# # Порівняння генераторів і списків за пам’яттю та швидкістю
# import time
#
# n = 10000000
#
# start = time.time()
# g = (i * 2 for i in range(n))
# print('Memory of generator =', sys.getsizeof(g))
# print('time of creating GENERATOR = ', time.time() - start)
#
# start = time.time()
# l = [i * 2 for i in range(n)]
# print('Memory of list = ', sys.getsizeof(l))
# print('time of creating LIST = ', time.time() - start)
#
# start = time.time()
# i = next(g)
# print('time of "NEXT" = ', time.time() - start)
#
# start = time.time()
# h = l[0]
# print('time of "List[0]" = ', time.time() - start)
#
# start = time.time()
# for i in g:
#     h = i
# print('time of "ALL GENERATOR" = ', time.time() - start)
#
# start = time.time()
# for i in l:
#     h = i
# print('time of "i in List" = ', time.time() - start)
#
# start = time.time()
# for i in range(len(l)):
#     h = l[i]
# print('time of "RANGE(LEN(List))" = ', time.time() - start)
