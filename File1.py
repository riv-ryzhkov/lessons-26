# print(-7 % 3)
# import copy
# n = 5
# l1 = [[0] * n for i in range(n)]
# l2 = copy.deepcopy(l1)
# l2[2][2] = 999
#
# for row in l1:
#     print(*row)
# print()
# for row in l2:
#     print(*row)
# try:
#     x = int('abc')
# except:
#     print('A')
#

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i * j:3}", end=" ")
#     print()

# def fib(n):
#     if n < 0:
#         raise ValueError("n має бути >= 0")
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# print(fib(0))
# print(fib(1))
# print(fib(2))
# print(fib(3))
# for i in range(10):
#     print(fib(i))
#




# a = int(input())
# b = int(input())
# c = int(input())
# print(a+b+c)


# from functools import reduce
#
# l1 = [1, 2, 3, 4]
#
#
# def foo(x, y):
#     print(x, y)
#     return x*y
#
#
# print(reduce(foo, l1))
#
# print(reduce(lambda x, y: x * y, l1))






