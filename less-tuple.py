# str незмінна послідовність символів
# list змінна послідовність об'єктів
# tuple незмінна послідовність об'єктів




# l1 = (33, 555, 'sdd', [34, 45], 33.45)
#
# print(l1, type(l1))
# print(*dir(l1), sep='\n')


# l1 = ()
# l1 = tuple()
# l1 = tuple(range(5))
# l1[0] = 9
# print(l1[2])
# l1 = tuple('adsafsdf')
# l1 = (3,)
# print(l1, type(l1), id(l1))
# print(l1, type(l1), id(l1), len(l1))


# t = (1, 2, 3, 4.23, 99, 'Hello!', [2, 3, 4], (5, 6, 4), True)
# print(t, type(t), id(t))
# print(t[2:7])
# print(len(t))

# print(*dir(t), sep='\n')
#############################################

# t = tuple(range(10))
# t1 = t[2:5]
# print(t, type(t), id(t))
# print(t1, type(t1), id(t1))
#
# print(t[2:7], type(t[2:7]), id(t[2:7]))
###########################################
######## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# t1 = (1, 2, 3, 4)
# t2 = tuple(t1)
# t3 = t2
# t4 = (1, 2, 3, 4)
# t5 = t4[:]
# t6 = t5 + tuple()
# t7 = (1,) + t6
# t8 = t7[1:]
# print('t1 =', t1, type(t1), id(t1))
# print('t2 =', t2, type(t2), id(t2))
# print('t3 =', t3, type(t3), id(t3))
# print('t4 =', t4, type(t4), id(t4))
# print('t5 =', t5, type(t5), id(t5))
# print('t6 =', t6, type(t6), id(t6))
# print('t7 =', t7, type(t7), id(t7))
# print('t8 =', t8, type(t8), id(t8))


#############################################

# text = 'Hello, world!'
# t = tuple(text)
# print(text, type(text), id(text))
# print(t, type(t), id(t))

###################################
####  t[0] #######################
#
# l = [1, 2, 3, 4]
# print(l, type(l), id(l))
# l[0] = 999
# print(l, type(l), id(l))

# t = (1, 2, 3, 4)
# print(t, type(t), id(t))
# print(t[0])
# t = list(t)
# t[0] = 999   #  !!!!!!!!!!!!!!!!!!!!!!!!!!!
# t = tuple(t)
# print(t, type(t), id(t))

###################################################
########  +   *   ################################

# t1 = (1, 2, 3, 4)
# print('t1 =', t1, type(t1), id(t1))
#
# t1 += (99, 88, 77)
# print('t1 =', t1, type(t1), id(t1))
#
# t1 *= 3
# print('t1 =', t1, type(t1), id(t1))
#
# t2 = t1[:3] + ('world',)
# print('t2 =', t2, type(t2), id(t2))

#################################################
######## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# t1 = (3)
# t2 = (3,)
# print(t1, type(t1), id(t1))
# print(t2, type(t2), id(t2))


###################################################
######## generator tuple ##########################
#
# l1 = tuple(i for i in range(5))
# # l1 = tuple(l1)
# print(l1, type(l1))
#
# # l1 = list(i for i in range(5))
# l1 = [i for i in range(5)]
# print(l1, type(l1))
#
#
#
# t = tuple(i for i in range(5))
# print(t, type(t))
#
# t = (i for i in range(5))   ################## GENERATOR!!!!!!!!!!!!!
# print(t, type(t))

#####################################

# t0 = (2, 9, -34, 67.5676)
# print(t0)
# print('max =', max(t0))
# print('min =', min(t0))
# print('sum', sum(t0))
# print('len =', len(t0))
# print('.' * 80)

####################
# t1 = ('Hello,', 'world!', [1, 2, 3], 78, 4545.54)
# print(t1, id(t1))
# print(t1[2], id(t1[2]))
# t1[2][1] = 999
# print(t1, id(t1))
# print(t1[2], id(t1[2]))
##################################

# print(t1[2], id(t1[2]))
# print(len(t1))
# print('.' * 80)
#
# for i in t1:
#     print(i)

#####################################################
############ join ###################################



# t1 = ['Hello,', 'world!']
# t1 = ('Hello,', 'world!')
# text1 = ' '.join(t1)
# print(text1, type(text1))

#################################################
######### count / index #########################


# t2 = (15, 0, 0, 0, 'abc', 44, 56, 77, 0, 0, 0, 44, 8, 44, 0, 34)
# print(t2, id(t2))
# symbol = 44
#
# print('count :', t2.count(symbol))
# print('index :', t2.index(symbol, 6))


#########################################


# a, b = (777, 888)
# print(a, b)


# a, b, c, d = range(3, 7)
# print(a, b, d, c)




t1 = 'Hello!'
# t1 = range(5)
# for num, el in enumerate(t1):
#     print(num, type(num), '->', el, type(el))


#
# for element in enumerate(t1):
#     print(element, type(element))




###################################################


# t1 = (222, 333, 2, 3, 6, 9, 0, -24)
# print(t1, type(t1), id(t1))
#
# n = int(input('index = '))
# number = int(input('number for insert = '))
# # t1 = t1[:n] + (number,) + t1[n:]
#
#
# l1 = list(t1)
#
# l1.insert(n, number)
# l1.sort()
# #
# t1 = tuple(l1)
#
# print(t1, type(t1), id(t1))


###########################################
##### tuple->list-> insert/sort ->tuple ###

# t1 = (222, 333, 2, 3, 6, 9, 0, -24)
# print(t1, type(t1), id(t1))
#
# l1 = list(t1)
# print(l1, type(l1), id(l1))
#
# l1.insert(5, 3333333)
# l1.sort()
# print(l1, '<<< insert/sort >>>', type(l1), id(l1))
#
# t1 = tuple(l1)
# print(t1, type(t1), id(t1))


########################################################
##### tuple->list-> append/sort ->tuple-> join -> str ###


# t1 = ('World!',)
# print('\ntuple ->', t1, id(t1), type(t1))
#
# l1 = list(t1)
# print('\nto list ->', l1, id(l1), type(l1))
#
# l1.append('Hello')
# print('\nappend ->', l1, id(l1), type(l1))
#
# l1.sort()
# print('\nsort ->', l1, id(l1), type(l1))
#
# t1 = tuple(l1)
# print('\nto tuple ->', t1, id(t1), type(t1))
#
# text = ', '.join(t1)
# print('\nafter join ->', text, id(text), type(text))

#####################################################

# t1 = (1, 2, (4, 5), 88)
# print(t1, id(t1), len(t1))
# t1 = (8,) + t1[1:]
# print(t1, id(t1), len(t1))



# t1 = (1, 2, [4, [9, 'Hello']], 88)
# print(t1, id(t1), len(t1))
#
# for el in enumerate(t1):
#     print(el)
#
# print(t1[2][1][1] + ', world!')

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# print(t1[2][1][1])
# t1[2][1][1] += ', world!'
# print(t1[2][1][1])
# print(t1, id(t1), len(t1))
#
#
# t = (1, 2, 3, [4, 5])
# print(t, id(t))
# w = t[3][0]
# print(id(w))
# t[3][0] = 1
# w = t[3][0]
# print(id(w))
# print(t, id(t))