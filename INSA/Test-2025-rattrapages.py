# def ma_fonction(a, b=10):
#     return a + b
#
# print(ma_fonction(5, 5))
###########################################
# print([ i for i in range(10) if i % 2 == 0 ])
###########################################
# lst1 = [1, 3, 2]
# lst1.sort(reverse=True)
# print(lst1)
#################################
# n, i = 25, 2
# while n % i != 0:
#     i += 1
# print(i)
#######################
# a = '1234567890'
# print(a[::-2])
#######################
# a = [1, 2, 3, 4, 'Hello', 1, 2, 3, 4]
# b = set(a)
# print(len(b))
#######################
# print (True and not False or False)
#######################
# text = 'How are you!'
# a = text.split()
# print(a[1])
#######################
# x = 3
# y = (x<5)*2 + (x<-5)*3 + (-x>-5)*4
# print(y)
#######################
# c = 2 * 2.0
# print(c, type(c))
#######################

# a = 3
# b = '4'
# print(a + b)
#######################

#######################

#######################

#######################
# a = 2
# b = 1
# c = 4
# d = c ** (b/a)
# print(d, type(d))
#######################

#######################
# a = 7.5
# print(int(a), round(a), bool(a))
#######################
# p = [i**2 for i in range(1, 3)]
# print(p)
#######################
# a = 12345678
# print(a//(10**2) % 10)
#######################
# a = 'Hello'
# b = 'Hi'
# c = 'Bonjour'
# print(f'Dire {c}, {a} ou {b}!')
#######################
# x = 5
# y = (x<2) * 2 + (x>=2) * 4 + (x>4) * (-1)
# print(y)
#######################
# a = (5.3)
# b = (5,3)
# c = (5.3,)
# print(type(a), type(b), type(c))
#######################
#######################
#######################
#######################
#######################


# d = {0: 24, 1: 'Hello', True: 56, False: None}
# print(d[0], d[1])

# variable = 'Wi Fi'
# variable = variable.split()
# print(dict(variable))


# l1 = [1, 2, 3, 4]
# l2 = l1
# l3 = l1[:]
# l4 = list[l1]
# print(l1 is l2, l1 is l3, l1 is l4, l3 is l4)

# def factorial(n=1):                  # 5 * (4 * (3 * (2 * (1)))) = res
#     print(n, end='')
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)     #(  5 * 4! # (4 * 3! # (3 * 2! #(2 * 1! #
#                                         # 120     24      6        2        1
#
# factorial(5)

# print((lambda a, b: a / b if b != 0 else '2')(2, 0), end='')
# print((lambda a, b: a / b if b != 0 else '2')(2, 2), end='')
# print((lambda a, b: a / b if b != 0 else '2')(0, 2), end='')
# print((lambda a, b: a / b if b != 0 else '2')(0, 0), end='')



# a = [[0] * 5] * 5
# a[0][0] = 3
# for i in range(5):
#     print(a[i][0], end='')


# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {4, 5, 6, 7, 8, 9}
# s3 = s1 - s2
# print(s3)


# s1 = {1, 2, 3, 4}
# s1.add(3)
# s1.add('3')
# s1.add(True)
# print(s1)


# t1 = (True, -1, 1, 2, [4, 5])
# t1[-1].append(3)
# print(len(t1))


# a = [-1, 0, 1, 2, 3]
# a[-1] = 5
# print(a)


# d = dict(enumerate('Hello'))
# a, b = d.popitem()
# d[a*3] = b*2
# print(''.join(d.values()))

