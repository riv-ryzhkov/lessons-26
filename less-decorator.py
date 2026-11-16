def list0():
    l = [x for x in range(10)]
    print('l0 : ', *l)


def list1():
    l = [x for x in range(15)]
    print('l1 : ', *l)


list0()
list1()


# print('=' * 40)
# list0()
# print('+' * 40)
#
# print('=' * 40)
# list1()
# print('+' * 40)




####################### Decorator with def ###########
import time

#
# def pr_run(func):
#
#     def wrapper():
#         print('.' * 40)
#         start = time.monotonic()
#         print('name of function :', func.__name__)
#         func()
#         print('time of running :', time.monotonic() - start, 'seconds')
#         print('=' * 40, '\n')
#
#     return wrapper()
#
#
#
# def pr_run1(func):
#
#     def wrapper():
#         print('-' * 40)
#         print('name of function :', func.__name__)
#         func()
#         print('+' * 40, '\n')
#
#     return wrapper()
#
#
# def list0():
#     l = [x for x in range(10)]
#     time.sleep(1)
#     print('l0 : ', *l)
#
#
# def list1():
#     l = [x for x in range(15)]
#     time.sleep(2)
#     print('l1 : ', *l)
#
#
# # list0()
# # list1()
#
# # pr_run(list0)
# # pr_run(list1)
#
# pr_run1(list0)
# pr_run1(list1)


############## with args #################################


# def pr_run(func, n=10, k=40, s='*', m='='):
#
#     def wrapper():
#         print(s * k)
#         print('name of function :', func.__name__)
#         func(n)
#         print(m * k)
#
#     return wrapper()
#
#
# def list0(n):
#     l = [x for x in range(n)]
#     print('l0 : ', *l)
#
#
# list0(7)
#
#
#
# print()
# pr_run(list0)
# pr_run(list0, 15, 60, '+', '-')




##################################################################
##### Decorator with  @.....  ###################################

# def pr_run(func):
#
#     def wrapper(n):
#         print('*' * 50)
#         print('name of function :', func.__name__)
#         func(n)
#         print('.' * 50)
#
#     return wrapper
#
# @pr_run
# def list1(n):
#     l = [x for x in range(n)]
#     print('l1 : ', *l)
#
#
# @pr_run
# def list2(n):
#     l = [x for x in range(n)]
#     print('l2 : ', *l)
#
#
# list1(5)
# print()
# list2(7)
# list2(17)
# list2(20)

####### With 2nd args ########
#
# def pr_run(func):
#
#     def wrapper(n, k=30, s='#'):
#         print('*' * k)
#         print('name of function :', func.__name__)
#         func(n, k, s)
#         print(s * k)
#
#     return wrapper
#
#
# @pr_run
# def list0(n, k, s):
#     l = [x for x in range(n)]
#     print('l0 : ', *l)
#
# @pr_run
# def list1(n, k, s):
#     l = [x for x in range(n)]
#     print('l1 : ', *l)
#
#
# list0(7)
# list1(5, 70)
# list1(5, 70, "$")


#######################################################
######### time ########################################
#######################################################
import time

#
# def pr_run(func):
#
#     def wrapper(n, k=30):
#         print('*' * k)
#         print('name of function :', func.__name__)
#         func(n)
#         print('*' * k)
#
#     return wrapper
#
#
# def run_time(func):
#
#     def wrapper(n):
#         start = time.time()
#         func(n)
#         print(func.__name__, time.time() - start)
#
#     return wrapper


# @pr_run
# @run_time
# def list1(n):
#     l = []
#     for i in range(n*2):
#         l.append(i)
#     print('l1 append:')


# @pr_run
# @run_time
# def list2(n):
#     l = [x for x in range(n*2)]
#     print('l2 generator:')
#
#
# @pr_run
# @run_time
# def list3(n):
#     l1 = []
#     l2 = []
#     for i in range(n*2):
#         if i % 2:
#             l1.append(i)
#         else:
#             l2.append(i)
#     l = l1 + l2
#     print('l3 append+append:')
#
#
# # n = int(input('n = ')) # 10_000_000
# n = 10_000_000
# print(n)
# list1(n)
# list2(n)
# list3(n)

# # ...........................................

# @pr_run
# @pr_run
# @run_time
# def count_(n, k=40):
#     s = [x**2 - x*4 + 7 for x in range(n*2)]
#     print('sum of  x**2-x*4+7=', sum(s))
#
# count_(1_000_000)
# ############################################################
#
# def func(*args, **kwargs):
#     print(type(args), args)
#     print(type(kwargs), kwargs)
#     print('=' * 80)
#     for i in args:
#         print(i)
#     print('='*80)
#     for key, vol in kwargs.items():
#         print(key, '->', vol)
#
#
# func(3, 5, 6, 7, 89, 565, x=5, y= 7, age= 8)

# ############################################################

#
# from datetime import datetime
#
#
# def time_run(func):
#
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         print(args)
#         print(kwargs)
#         func(*args, **kwargs)
#         result = datetime.now() - start
#         return result
#
#     return wrapper
#
# @time_run
# def list_app(n):
#     l = []
#     for i in range(n):
#         l.append(i)
#     return l
#
# @time_run
# def list_gen(n, *args, **kwargs):
#     l = [x for x in range(n)]
#     return l
#
# print(list_app(10_000_000))
# print(list_gen(10**7))
# print(list_gen(10**7, 5, 7, 3, 1, 34, 56, d=35, m=2, t=6, r=7))

########################################################################



