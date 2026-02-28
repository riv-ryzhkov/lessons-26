# import numpy as np
#
# def f(x):
#     y = np.exp(x)
#     return y
#
#
# def rect_droite(a, b, n):
#     dx = (b-a) / n
#     res = 0
#     for i in range(n):
#         res = res + f(a+(i+1)*dx)
#     res = res * dx
#     return res, a+(i+1)*dx
#
# a = 0
# b = 1
# n = 30
#
# print(rect_droite(a, b, n))



# def power(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * power(a,n-1)
#
# n = float(input("n = "))
# a = int(input("a = "))
# print(power(a, n))


n = int(input())
somme = 0
for i in range(1, n + 1):
    somme += i
for i in range(n-1):
    somme -= int(input())
print(somme)