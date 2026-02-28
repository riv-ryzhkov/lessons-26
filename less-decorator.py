def list0():
    l = [x for x in range(10)]
    print('l0 : ', *l)


def list1():
    l = [x for x in range(15)]
    print('l1 : ', *l)


# list0()
# list1()


# print('*' * 50)
# list0()
# print('+' * 30)
#
# print('*' * 50)
# list1()
# print('+' * 30)




####################### Decorator with def ###########
import time


def pr_run(func):

    def wrapper():
        print('+' * 80)
        start = time.monotonic()
        print('name of function :', func.__name__)
        func()
        print('time of running :', time.monotonic() - start)
        print('*' * 30, '\n'*2)

    return wrapper()



def pr_run1(func):

    def wrapper():
        print('-' * 40)
        print('name of function :', func.__name__)
        func()
        print('+' * 40, '\n'*2)

    return wrapper()


def list0():
    l = [x for x in range(10)]
    time.sleep(1)
    print('l0 : ', *l)


def list1():
    l = [x for x in range(15)]
    time.sleep(2)
    print('l1 : ', *l)


# list0()
# list1()
#
# pr_run(list0)
# pr_run(list1)

# pr_run1(list0)
# pr_run1(list1)


############## with args #################################


# def pr_run(func, n, k, s, m):
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
# print()
# pr_run(list0, 15, 80, '$', '&')
# pr_run(list0, 10, 60, '+', '-')




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
#
#
# @pr_run
# def list1(n):
#     l = [x for x in range(n)]
#     print('l1 : ', *l)
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

####### With 2nd args ########

# def pr_run(func):
#
#     def wrapper(n, k=30):
#         print('*' * k)
#         print('name of function :', func.__name__)
#         func(n, k)
#         print('*' * k)
#
#     return wrapper
#
#
# @pr_run
# def list0(n, k):
#     l = [x for x in range(n)]
#     print('l0 : ', *l)
#
# @pr_run
# def list1(n, k):
#     l = [x for x in range(n)]
#     print('l1 : ', *l)
#
#
# list0(7)
# list1(5, 70)


#######################################################
######### time ########################################
#######################################################
import time


def pr_run(func):

    def wrapper(n, k=30):
        print('*' * k)
        print('name of function :', func.__name__)
        func(n)
        print('*' * k)

    return wrapper


def run_time(func):

    def wrapper(n):
        start = time.time()
        func(n)
        print(func.__name__, time.time() - start)

    return wrapper

#
# @pr_run
# @run_time
# def list1(n):
#     l = []
#     for i in range(n*2):
#         l.append(i)
#     print('l1 append:')
#
#
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
# n = int(input('n = '))
# list1(n)
# list2(n)
# list3(n)

# # ...........................................

# @pr_run
# @pr_run
# @run_time
# def count_(n, k=40):
#     s = [x*4-x**2+7 for x in range(n*2)]
#     print('sum of  x*4-x*2+x*7 =', sum(s))
#
# count_(10000)
# ############################################################












#
# from datetime import datetime
#
# def time_run(func):
#
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
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
# print(list_app(100000))
# print(list_gen(10**5))
# print(list_gen(3, 5, 7, 3, 1, m=2, t=6, r=7))

########################################################################



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
# func(3, 5, 6, 7, a=5, b= 7, c= 8)