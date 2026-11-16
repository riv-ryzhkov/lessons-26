import statistics
import time
import random

#
# def run_time(func, num):
#
#     def wrapper(num):
#         res = 0
#         r = 1000
#         for i in range(r):
#             start = time.monotonic_ns()
#             func(num)
#             res += time.monotonic_ns() - start
#         # print(func.__name__, 'time =', res)
#         return res
#
#     return wrapper(num)
#
#
#
# def fact1(n):  # 1*2*3*4*5 -> 5!
#     result = 1
#     for i in range(n):
#         result *= (i+1)
#     return result
#
#
# def fact2(n):  # 5*4*3*2*1 -> 5!
#     if n <= 1:
#         return 1
#     else:
#         return n * fact2(n-1)
#
#
#
# x = 300
# print('='*50)
# print(f"! func1          ! func2          !")
# print('='*50)
# for i in range(20):
#     res1 = run_time(fact1, x)
#     res2 = run_time(fact2, x)
#     print(f"! {res1}       ! {res2}       !", "<<<<<<<" if res1 >= res2 else ">>>>>>")
#     # if res1 < res2:
#     #     print('time of func1 <<<<<<<<<<<<< time of func2\n')
#     # else:
#     #     print('time of func1 >>>>>>>>>>>>> time of func2\n')
#

# ===============================================================================
#                O(1)
# ===============================================================================
import matplotlib.pyplot as plt


def my_plot(x, y):
    print('x :', x)
    print('y :', y)
    plt.plot(x, y)
    # plt.plot(x, y, 'g+')
    # plt.plot(x, y, 'b-o')
    # plt.plot(x, y, 'rx')
    # plt.plot(x, y, 'r-x')
    # plt.plot(x, y, 'yo')
    # plt.plot(x, y, 'b')

    plt.xlabel('Inputs')
    plt.ylabel('Steps')
    plt.title('Function O()')

    plt.show()

#
# def big_o1(data: list, count=0):
#     result = data[-1] # якась операція, що не залежить від довжини data
#     count += 1
#     return count
#
#
# y = []
# n = 10 #  кількість даних
# for i in range(n):
#     count = 0
#     y.append(big_o1([el for el in range(n)]))
#     print(y)
#
# x = [el for el in range(n)] #  кількість даних
# my_plot(x, y)
#
#

# ================================================================
#                    O(n)
# ================================================================
#
# def big_on(data: list):
#     global count
#     for i in data:
#         result = i
#         count += 1
#     return count
#
#
# y = []
# n = 80
#
# for i in range(n):
#     count = 0
#     y.append(big_on([el for el in range(i)]))
#
# x = [el for el in range(n)] #  кількість даних
#
# my_plot(x, y)






# # =======================================================================
# #                        O(2n)   (при n->нескінченність O(n))
# # =======================================================================
#
# def big_on(data: list):
#     global count
#
#     for i in range(len(data)):
#         result = data[i]
#         count += 1
#
#     for i in range(len(data)):
#         result = data[i]
#         count += 1
#
#     return count
#
#
# y = []
# n = 20
# for i in range(n):
#     count = 0
#     y.append(big_on([el for el in range(i)]))
# x = [el for el in range(n)] #  кількість даних
# my_plot(x, y)
#




# =======================================================
#                   O(n^2)
# =======================================================
# def big_on2(data: list):
#     global count
#
#     for i in range(len(data)):
#         for j in range(len(data)):
#             result = data[j]
#             count += 1
#     return count
#
#
# y = []
# n = 20 #  кількість даних
# for i in range(n):
#     count = 0
#     y.append(big_on2([el for el in range(i)]))
# x = [el for el in range(n)]
# my_plot(x, y)
#




# ==================================================================
#                            O(1/n)  вимишлений і не реальний  (пошук карти / спроби)
# ==================================================================

#
# def big_o2_n(data: list):
#     global count
#     for i in range(len(data)):
#         result = data[i]
#         count += 1
#     return count
#
#
# y = []
# n = 20
# for i in range(n):
#     count = 0
#     y.append(big_o2_n([el for el in range(n-i)]))
# x = [el for el in range(n)] #  кількість даних
# my_plot(x, y)
#






# ==================================================================
#                            O(1/n^2)  вимишлений і не реальний (досвід/помилка)
# ==================================================================
# def big_on2(data: list):
#     global count
#
#     for i in range(len(data)):
#         for j in range(len(data)):
#             result = data[j]
#             count += 1
#     return count
#
#
# y = []
# n = 8
# for i in range(n):
#     count = 0
#     y.append(big_on2([el for el in range(n-i)]))
# x = [el for el in range(n)] #  кількість даних
# my_plot(x, y)





# ==========================================================
#                   O(log(n))
# ==========================================================
# import random
#
#
# def func(num):
#     count = 0
#     my_list = []
#     for i in range(num):
#         el = random.randint(1, 100)
#         if el not in my_list:
#             my_list.append(el)
#             count += 1
#     # print(*my_list)
#     return count
#
#
# y = []
# n = 1000
# x = [el for el in range(n)]
# for i in range(n):
#     y.append(func(i))
# my_plot(x, y)
# #

# ========================================================
#  Складні комплексні алгоритми
# ========================================================
# def big_on_cmpl(data: list):
#     global count
#
#     for i in range(3): #   O(3)
#         result = i
#         count += 1
#
#     for i in range(len(data)): #   O(n)
#         result = data[i]
#         count += 1
#
#
#     for i in range(len(data)): #   O(2n)
#         result = data[i]
#         count += 1
#     for i in range(len(data)):
#         result = data[i]
#         count += 1
#
#
#     for i in range(len(data)):  #   O(n^2)
#         for j in range(len(data)):
#             result = data[j]  #   O(3) + O(n) + O(2n) + O(n^2) = O(n^2)
#             count += 1
#
#     return count
#
#
# y = []
# n = 10
# for i in range(n):
#     count = 0
#     y.append(big_on_cmpl([el for el in range(i)]))
# x = [el for el in range(n)] #  кількість даних
# my_plot(x, y)
#




# '''
# O(?) = O(3) + O(n) + O(2n) + O(n^2) = O(n^2 + 3n + 3) ---> O(n^2)
# '''


# ==============================================================
#      Найкращій і найгірший
# ==============================================================
# def my_search(number: int, data: list):
#     global count
#     while data:
#         el = data.pop(random.randint(0, len(data)-1))
#         count += 1
#         print(el, number)
#         if el == number:
#             return count
#     return count
#
#
# data_run = [el for el in range(36)]
# n = 4 # Найкращій результат О(1), найгірший О(n), середньовипадковий O(n/2) -> O(n)
# y = []
# x = [el for el in range(len(data_run))]
# for i in x:
#     count = 0
#     data = data_run.copy()
#     y.append(my_search(n, data))
#
# print('min =', min(y))
# print('max =', max(y))
# print('range/2 =', (max(y) - min(y))/2)
# print('median =', statistics.median(y))            #   50% <= median >= 50%
# print('mean =', sum(y)/len(y))
# my_plot(x, y)


# ==============================================================
#      Просторова складність алгоритму
# ==============================================================
# '''
# Просторова складність харектиризує задіяність пям'яті та нових змінних
# Наприклад, якщо для виконання алгоритму вам прийдеться створити 1 нову змінну,
# то така просторова складність буде О(1).
# Якщо вам потрібно дублювати всі вхідні дані, то це вже буде O(n).
# Дивись приклад:
# '''


###########################################################
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
#     print(stage, ":", round(mem, 2), "MB")
#
# # Пам'ять на початку програми
# show_memory("Початкова пам'ять")
#
# time.sleep(1)
#
# # Створюємо великий список (виділяємо багато пам'яті)
# data = [i for i in range(15_000_000)]
#
# show_memory("Після створення великого списку")
#
# time.sleep(1)
#
# # Видаляємо список
# del data
#
# show_memory("Після видалення списку")
#
# time.sleep(1)
#
# data = (i for i in range(15_000_000))
#
# show_memory("Після генератор")
# # Примусовий запуск збирача сміття
# gc.collect()
#
# show_memory("Після виклику garbage collector")
#



# # ##################################    @profile
# # Рядок №   Використання пам'яті   Приріст   Кількість випадків   Зміст рядка

import sys
import os, psutil
from memory_profiler import memory_usage, profile

@profile
def my_func(data: list):
    result = []
    for el in data:
        result.append(el * el)
    print('my_func :', sys.getsizeof(my_func) + sys.getsizeof(el) + sys.getsizeof(result) + sys.getsizeof(data))
    return result

@profile
def my_func1(data: list):
    result = []
    for i in range(len(data)):
        result.append(data[i] * data[i])
    print('my_func1 :', sys.getsizeof(my_func1) + sys.getsizeof(i) + sys.getsizeof(data) + sys.getsizeof(result))
    return result

@profile
def my_func2(data: list):
    print('my_func2 :', sys.getsizeof(my_func2))
    return (el * el for el in range(n1, n2, step))


# data = [2, 4, 6, 8, 10]
n1, n2, step = 2, 500_000, 2
data = [i for i in range(n1, n2, step)]
# process = psutil.Process(os.getpid())
# ps_mem = []
# ps_mem.append(process.memory_info().rss)

my_func(data)
# ps_mem.append(process.memory_info().rss)
my_func1(data)
# ps_mem.append(process.memory_info().rss)
my_func2([])
# ps_mem.append(process.memory_info().rss)

# print(ps_mem[0], '=== Start')
# for i in range(len(ps_mem)-1):
#     print(ps_mem[i], '==> +', ps_mem[i+1] - ps_mem[i])
# print(ps_mem[-1], '=== END')





################# END ##############
#################################################

# import psutil
# import os
# import matplotlib.pyplot as plt
#
#
# process = psutil.Process(os.getpid())
#
# # O(1)
# def constant_space(n):
#     arr = []
#     a = 1
#     b = 2
#     c = a + b
#     return arr
#
#
# # O(log n)
# def logarithmic_space(n):
#     arr = []
#     k = n
#     while k > 1:
#         arr.append(k) #       100000000000
#         k //= 2
#     return arr
#
#
# # O(n)
# def linear_space(n):
#     arr = []
#     for i in range(n):
#         arr.append(i)
#     return arr
#
#
# # O(n^2)
# def quadratic_space(n):
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append(i+j)
#         matrix.append(row)
#     return matrix
#
#
# sizes = []
# mem_o1 = []
# mem_log = []
# mem_n = []
# mem_n2 = []
# m_o1 = []
# m_log = []
# m_n = []
# m_n2 = []
#
#
# for n in range(1, 1000, 20):
#
#     sizes.append(n)
#
#     # O(1)
#     before = process.memory_info().rss
#     a = constant_space(n)
#     mem_o1.append(process.memory_info().rss - before)
#     m_o1.append(len(a))
#
#     # O(log n)
#     before = process.memory_info().rss
#     a = logarithmic_space(n)
#     mem_log.append(process.memory_info().rss - before)
#     m_log.append(len(a))
#
#     # O(n)
#     before = process.memory_info().rss
#     a = linear_space(n)
#     mem_n.append(process.memory_info().rss - before)
#     m_n.append(len(a))
#
#     # O(n^2)
#     before = process.memory_info().rss
#     a = quadratic_space(n)
#     # mem_n2.append(process.memory_info().rss - before)
#     m_n2.append(len(a)*len(a[0]))
#
#
# plt.figure(figsize=(9,6))
#
# plt.plot(mem_o1, label="O(1)")
# plt.plot(mem_log, 'o', label="O(log n)")
# plt.plot(mem_n, label="O(n)")
# plt.plot(mem_n2, label="O(n²)")
#
# plt.yscale("log")
#
# plt.plot(sizes, m_o1, label="O(1)")
# plt.plot(sizes, m_log, label="O(log n)")
# plt.plot(sizes, m_n, label="O(n)")
# plt.plot(sizes, m_n2, label="O(n²)")

# plt.xlabel("Input size (n)")
# plt.ylabel("Memory usage (bytes)")
# plt.title("Space Complexity of Algorithms")
#
# plt.legend()
# plt.grid()
#
# plt.show()
