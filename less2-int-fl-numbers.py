# a = 9
# b = 2
# print(a*b)
# print(a/b)  # 4.5
# print(9//2)  # 4  div
# print(a % b)  # 1  mod


# a = 4
# b = 2
# c = a + b
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))

# print(type(4**(1/2)))


# ()
# **
# * / //  %
# + -

# print((7 - 4 )/ (2 * (7 - 5) * 3 / 2))
# print(7 - 4 / 2 * 2 * 3 / 2)
# print(7 - 2 * 2 * 3 / 2)
# print(7 - 4 * 3 / 2)
# print(7 - 12 / 2)
# print(7 - 6)

# print(5 * 6 - 2 ** 3 / 2 + 3 / 2 + 2)


# a = 2
# b = 2.0
# print(id(a))
# print(id(b))
# print(id(a) == id(b))
# print(type(a) == type(b))
# print(a == b)
# print(a is b)




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(9//2, 9 % 2)  #  a*b+c ->
# print(-9//2, -9 % 2)  # -5 1
# print(-9//2)  # -5 1
# a = 9 #             -----(-5)-------(-4.5)----------(-4)------------------->
# b = 2
# a1 = a//b # 4   -5
# a2 = a%b # 1     1
# # print(a1)
# # print(a2)
# c = a1*b + a2
#
# print(a, c)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# #  (a // b) * b + (a % b)= a
#
# a = -9
# b = 2
# print((a // b) * b + (a % b))
#
#       # -5   -10        1
# # (-9 // 2) * 2 + (-9 % 2) = -9
# print((-9 // 2) * 2 + (-9 % 2))
# ==================================================

# a  = abs(-9)
# print(a//2)
#
# a = -9
# print(abs(a//2))
#
# a = -9
# print(abs(a)//2)
# #######################################################


import math


# print(dir(math))
# print(*dir(math), sep='\n')


# a = 2
# print(math.sqrt(a))
# print(a ** (1/2))
# print(math.e)
# print(math.pi)
# print(math.e ** 3)
# print(math.exp(3))

######################################
# import math
# from math import *
# from math import sin, pi, e, cos
# from math import sin as math_sin
# from numpy import sin as num_sin
#
#

# import numpy
#
# print(*dir(numpy), sep='\n')

# print(math_sin(3))
# print(num_sin(3))






# print(*dir(math))
# print(*dir(math), sep='\n')

# print(math.sin(4.5467))
# print(math.cos(1.23))
# print(cos(1.23))
# print(sin(1.23))
# print(pi)
# print(e)
# print(sinus(1.24))
# print(numsin(1.24))


# print(sinus(2))
# print(numsin(2))


#
# print(sinus(2))


#
# print(cos(3.6))
#
# print(sin(3.2))
# print(pi)
# print(e)
# print(cos(4))


#
# print(sinus(3.4))
# print(sin(3.4))
# print(cos(3.4))
# print(pi)
# print(e)


# print(sin(pi/2))
# print(cosh(pi/2))
# print(tan(pi/4))



# print(math.sin(234))
# print(math.cos(234))


# print(sin(546))
# print(cos(546))
# print(tan(546))

# import math
#
# # print(*dir(math), sep='\n')
# #
#
# print(math.floor(-32.9999975869879))
# print(math.ceil(-32.00000000000079))

# # -----------------------32---*--------------------------------->
#
# print(math.floor(-32.9999975869879))
# print(math.ceil(-32.0000009999975869879))


# from math import floor, ceil
# from math import *
# from math import sin as s1

# a = 1/3+1/3
# print(a)


from math import *


# print(sin(radians(45)))
# print(radians(45)*4)
# print(degrees(2*pi))
# print(sin(radians(degrees(pi/4))))
# print(log(100, 2))
# print(pi)
# print(e)

# for i in range(256):
#     print(i, '=>', chr(i))
##############################################################
# 11111111 0...127 LAT   128...255 NAT  1010 1101

# 1 2 4 8 16 32 64 128 256 512  1024  10000000000
# a = 201 #  10010111  01101011  1101 0110 = 13:06 1011010101101101111101011110101101110  13:04
# b = bin(a) # 2**8 = 256  0...255
# c = oct(a) # 1101 1011 = DB   AE = 10 14 = 1010 1110  c8 -> 12 8 -> 1100 1000
# d = hex(a)  #  1011 0101 = 11 05  10->A  11->B  12->C  13->D  14->E  15->F   = B5   11:05
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))

#     1111 1111  0...127 128...255   255 -> 11111111  ->  FF



# print(bin(200))  # 0110 0100 = 8 4  1100 1000 = 12 8 = C8  1111 1111 = FF  1100 0100 = C4
# 10 - A  11 - B  12 - C   13 - D   14 - E   15 - F
# a = 218
# b = bin(a)
# c = oct(a)
# d = hex(a) # 2D   0010 1101 = 2 13        2 D       1101 1010 = D A  1111 - F 0111 1110 = 7E
# print(a)
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))

##########################################################

# a = int(input('input number : '))
# if a % 2:
#     print('Непарне!')
# else:
#     print('Парне!')


a = 123456789
# n =int(input('n='))
# res = a // 10**(n) % 100
# print(res)




#
# for n in range(9):
#     print(a % 10, end='->')
#     a = a // 10


# print(7//2)
# print(8 % 2 == 0)


# print(a // 1000)
# n = 6
# print(a // 1000 % 10)



# Завдання! Зробити програму, яка виводить бажану цифру на екран

# a = 123456789012345
# n = int(input('Введіть яку цифру сзаду потрібно вивести n = '))
#
# print(a // (10**(n-1)) % 10)


# print(a // 10**(n-1) % 10)


# !!!!!!!!!!!!!!!!!!!!! 0.30000000000000004.com !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# print(1/3)

# a = 0.1 + 0.2
# print(a)
# print(a==0.3)





# print(round((0.1 + 0.2)*10)/10)
#
# print(round((0.1 + 0.2), 17))


# print(0.1 + 0.2)
# print((0.1 + 0.2) == 0.3)
# #
# print(0.1 + 0.2 == 0.3)
# print(0.1 + 0.2 - 0.3)
# res = 0.1 + 0.2
# print(format(res, '.15f'))
# print(round(0.1 + 0.2, 15))



# import math
# #
# print(0.1 + 0.2 == 0.3)
# # print(0.1 + 0.2)
# # print(0.2)
# # print(0.3)
# print(math.isclose(0.1 + 0.2, 0.3))  # скругляє до 1е-9
#
# print(1/3)
# print(1/3*3)






















# 1=====================================
# x = float(input())
# print(int((x * 10) % 10))

# print(int((float(input()) * 10) % 10))


# 2======================================
# n = int(input())
# print(n // 100 + (n % 100) // 10 + (n % 10))



#3======================================
# n = int(input())
# m = int(input())
# print((m+n-1)//n)


# n = int(input())
# m = int(input())
# if m % n == 0:
#     print(m // n)
# else:
#     print(m // n + 1)



#3===========================
# import math
#
# n = int(input())
# m = int(input())
# print(math.ceil(m / n))



#4=====================================
# a = int(input())
# a = a*45 + (a//2)*5 + ((a+1)//2-1)*15
# print(a//60 + 9,  ':', a%60)



#5=====================================
# print(float(input()) % 30 * 12)
#
#
#
# alpha = float(input())
# print(alpha % 30 * 12)



#6=====================================
# a = 10
# b = 3
# c = a//b
# d = a%b
# print('a= ', a, '  b= ', b, '   a//b= ', c, '  a%b= ', d,'   ', '    a//b + a%b = ', c*b+d)
# a = 10
# b = -3
# c = a//b
# d = a%b
# print('a= ', a, '  b=', b, '   a//b=', c, '  a%b=', d,'   ', '    a//b + a%b = ', c*b+d)
# a = -10
# b = 3
# c = a//b
# d = a%b
# print('a=', a, '  b= ', b, '   a//b=', c, '  a%b= ', d,'   ', '    a//b + a%b =', c*b+d)
# a = -10
# b = -3
# c = a//b
# d = a%b
# print('a=', a, '  b=', b, '   a//b= ', c, '  a%b=', d,'   ', '    a//b + a%b =', c*b+d)


#6!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# v = int(input())
# t = int(input())
# print((v * t) % 109)



#7================================
# h = int(input())
# a = int(input())
# b = int(input())
# k = (h - a)//(a - b)
# if h <= a:
#     k = 1
# elif (h - a) % (a - b) == 0:
#     k += 1
# else:
#     k += 2
# print(k)



#7!!!!!!!!!!!!!!!!!!!!!!!
#
# import math
#
#
# h = int(input())
# a = int(input())
# b = int(input())
# print(math.ceil((h-a)/(a-b))+1)

