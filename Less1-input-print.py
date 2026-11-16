# print('Hello, world!')




# print(1234)

# print('hello!', 345)

# print(2+2)
# print('2'+'2')

# print(2 + '45')

########### # ##############################


# a = 7               # int
# b = 3.14159         # float   PEP-8
# c = '123gdgwf'      # str
# d = True            # bool
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))

# a = 4.123456789123456789
# print(a)
import math


# a = 0.1
# b = 0.2
# c = a + b
# print(c == 0.3)
# print(isclose(a + b, c))


#############################################
#
# print('Hello, world!')
#
# c1 = "I'm a student"
# print(c1, type(c1))
#
# c2 = "Ім'я"
# print(c2, type(c2))
#
# c3 = ''' Всім привіт!
# Я радий вас бачити!
# Я радий вас бачити!
# Я радий вас бачити!
# Я радий вас бачити!
# Я радий вас бачити!
# Слава Україні!'''
# print(c3, type(c3))
#






#############################################

a = 33
b = 567.234

# print(a + b, a, 3*a, 'Hello!')
# print(a + b, a, 3*a, 'Hello!', sep='<=====>')
# print(a + b, a, 3*a, 'Hello!', sep=' ', end='\n')
# print(a + b, a, 3*a, 'Hello!', sep='\t', end='=====')
# print(a + b, a, 3*a, 'Hello!', sep='\t', end='=====')



# print(a + b, a, 3*a, 'Hello!', sep='**', end='\n\n\n')
# print(a + b, a, 3*a, 'Hello!', sep='**********', end='\n')
# print(a + b, a, 3*a, 'Hello!', sep='**', end='\n')

# print('hello\nworld\n!')
# print('hello', 'world', '!', sep='\n')
# print('hello \t world\n !')

# print(a, 'Hello\n\t=====', a+b, '\ngfhjgj')


################################################################

################################################################

# a = input()    # Hello   34   3.14159   True
#
# a = int(a)
# print(a)
# print(type(a))

# a = int(a)
# print(a)
# print(type(a))


###############################################

# a = input()
# b = input()
# print(a + b)


########################################
# a = int(input())  # int()
# b = int(input())
#
# print(a, type(a))
# print(b, type(b))
# print(a + b)
#
# a = float(input())
# b = float(input())
# print(a, type(a))
# print(b, type(b))
#
# print(a + b)

# a = 5.
# print(a, type(a))

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# a = bool(input())    # ''  ' '     -2314 78  0   0.0
# b = bool(input())



# print(a, type(a))



# print(b, type(b))

# a = int(True)
# b = int(False)
# print(a, type(a))
# print(b, type(b))
# print(a * b)




# a = 5
# b = 22
#
# print((a>b) * 3 + (-b>a) * 5**2)




# a = 5
# b = 88
# print(a, b)
#
# c = a
# a = b
# b = c
# print(a, b)


# a, b = b, a
#
# print(a, b)


##########################################

# d = int(input('Введіть число d = '))
# print(d, type(d))
# d1 = int(input('Введіть число d1 = '))
# print(d1, type(d1))
#
# print(d, '+', d1, '=', d+d1)
# print(str(d)+' + '+str(d1)+' = '+str(d+d1))
#
#
# print('Сума числа ' + str(d) + ' та числа ' + str(d1) + ' дорівнює ' + str(d+d1))
#
# print('Сума числа', d, 'та числа', d1, 'дорівнює', d+d1)
#
# print(f'Сума числа {d} та числа {d1} дорівнює {d+d1}')


#####################################################################
#
# name = input("Ввведіть своє ім'я : ")
# print('Дуже приємно,', name, '!')
# print('Дуже приємно, ' + name + ' !')

########################################################

# a = 5
# b = 2
# c = a % b     #  + - * / ** // %
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))

# print(32 / 3)
# print(32 // 3)
# print(32 % 3)
# #
# a = 4**(1/2)
# print(a, type(a))


##############################################################
# print('=' + '=' + '=')
# print('='*30)
#
# t = 'Hello! '
# print('>' * 80)
# print(' '*10, t * 5)
# print('*' * 80)

################################################################

# !!!!!!!!!!!!!!!!! Print

# a = 5
# b = 12
# c = 'Hello'
# t = 'world'


##########
# print(a, b, c, t, end='\n'+'*'*80+'\n')
# print(a, b, c, t, sep=' -> ', end='\n'+'*'*80+'\n')
# print(a*100, b, c, t, sep='\t\t', end='\n'+'*'*80+'\n')
# print(a*100, b, c, t, sep='\t\t')
# print(a*1, b, c, t, sep='\t\t')
# print(a*10, b, c, t, sep='\t\t')
# print(a, b, c, t, sep='\n', end='\n'+'*'*80+'\n')
#
# print(a+b)
# print(c+t)

# format  ####################################
#  pg 1 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = 57
# b = 3.1415934345355
# v = 'Vasya'
# c = 'Alex'
# t = 'See you next'
#
#
# print('Hello, {}! And {}! {} time.)'.format(v, c, t))
# print('Hello, {0}, {4}! And {0}'.format(v, c, a, b, t))

####################################################################
# print('{:15f}+{:10.2f}={:20.5f}'.format(a, b, a+b))
# print('{:15}+{:10.2f}={:20.5f}'.format(a, b*2, a+b))
# print('{:15}+{:10.2f}={:20.5f}'.format(a, b*20, a+b))
# print('{:15}+{:10.2f}={:20.5f}'.format(a, b*200, a+b))
# print('{:15}*{:10}={:20}'.format(a, a*a, a*a*a))
# print('{:15.2f}'.format(b*10000))
# print('{:15.3e}'.format(b*1000))
# print(b*1000)
# print('{:15.4e}'.format(b*200))

################################################
# print('C:\test\name.txt')
# print(r'C:\test\name.txt')

##########################################   1010 - 10   101 - 5     10100 - 20   10 * 2
# t = 'Hello'
# name = input("Введіть ім'я ")
# print(f'{t}, {name}! {name} is my friend! {t}')


#########################################
# name = 'Vasya'
# b = input(f'Would You be so kind \nto input b for {name} :')
# print('b =', b, type(b))

###############################################


# !!!!!!!!!!!!!!!!!!!!!!!! others


# print(abs(-4.78))
# print(min(3, 5, 7.099879, -7))
# print(max(3, 5, 17, -7))
# print(sum([3, 5, 7, -7]))

# pg 2!!!!!!!!!!!!!!!!!!!!!!!!!!



# a = -4.999999999500001
# # print('round =', round(a))
#
# print('int =', int(a))


# print(1/3)
# import math
#
#
# a = 0.1
# b = 0.2
# c = 0.300000000000000000004
# print(a + b == c)
# print(c)
# print(math.isclose(c, a+b, rel_tol=1e-15))


# a = 1+1e-16
# a = 3.553574654654865675765975976798
# print(a)





# END
