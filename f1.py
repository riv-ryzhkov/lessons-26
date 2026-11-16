# def pgcd(u : int,v : int)-> int :
#     u = abs(u)
#     v = abs(v)
#     while v != 0 :
#         # temp = u
#         # u = v
#         # v = temp % v
#         u, v = v, u % v
#     return u
#
# print(pgcd(3,4)

from math import *


# print((2.5*pi)%(2*pi))
# print((2.5*pi))
# print((2*pi))
# print(3%2.4)


# def f1(n : int)-> int :
#     if n == 0 :
#         res = 1
#     else :
#         res = n * f1(n-1)
#     return res
#
#
# def main()-> None :
#     n = 2;
#     r = f1(5);
#     print(f"r = {r}")
#
# main()


# def ft(t1 : list[int],t2 : list)-> None :
#     if t1[0] == 0 :
#         t2[1] = 3
#     else :
#         t2[0] = t2[0]- 1
#         ft(t2,t1)
# def mainFt()-> None :
#     t = [1,1]
#     ft(t, t)
#     print(f"t = {t}")

# mainFt()


# class Homme:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
# d = Homme("Homme", 5)
# print(d.age)
# print(d._age)
#
# class Rationnel:
#
#     @property
#     def num(self)-> int :
#         return self._num
#
#     @property
#     def denom(self)-> int :
#         return self.__denom
#
#     @num.setter
#     def num(self, num: int) -> None:
#         self._num = num
#
#     @denom.setter
#     def denom(self, denom: int) -> None:
#         self.__denom = denom
#
#
#     def __init__(self, num: int = 0, denom: int = 1):
#         if denom == 0:
#             raise ZeroDivisionError()
#         self._num = num
#         self.__denom = denom
#
#
# a = Rationnel(num=3, denom=5)
# print(a.num)
# print(a.denom)
# a.num = 9
# print(a.num)
# print(a.denom)
# a.denom = 17
# print(a.num)
# print(a.denom)


# a = 2000
# b = 345
# print(a+b)
# print('a and b', a or b)

# print(0.1 + 0.2 == 0.3)
# print(0.1 + 0.2)

l1 = list(range(10))
b = l1[1:3]
print(b)
l1[1:3] = [11, 12, 13, 14]
print(l1)
