# map-zip-lambda-filter-sort-sorted


def my_func(x):
    return abs(int(x))

#
# print(my_func(-465.9008))
#
# l1 = [2.324, '-3', -45, '67', '-99']
# print(l1, id(l1))
#
# l2 = []
# for i in l1:
#     l2.append(my_func(i))
#
# print(l1, id(l1))
# print(l2, id(l2))


################################ map

l1 = [2.234, '-3', -45, '67', '-99']

# l2 = map(int, l1)
# l2 = list(map(int, l1))
# l2 = list(map(my_func, range(-5, 10, 2)))
# l2 = list(map(my_func, l1))
#
#
# print(l1, id(l1))
# print(l2, id(l2))


# l2 = list(map(my_func, [1, "-2", -3, 5]))
# print(l2, id(l2))


def pwd(num):
    return num ** 2

# l = list(range(-5, 5))
# print(l)
#
# l2 = list(map(pwd, l))
# print(l2)



#
# l2 = list(map(lambda x: x ** 2, range(-5, 5)))
# print(l2, id(l2))


# print(l1)
# l2 = list(map(lambda x: abs(int(x)), l1))
# f1 = lambda x: abs(int(x))
# print(l2, id(l2))
# print(f1)
# l2 = list(map(f1, l1))
# print(l2, id(l2))


############################################## filter

l1 = [2.244, '-3', -45, '67', '-99', 1, 0, True]
# print(l1)

# print(list(filter(lambda x: int(x) > 0, l1)))

# def foo(num):
#     return int(num) > 0   # 0 -> False  "" -> False
#
# print(list(filter(foo, l1)))
#
# l2 = list(filter(lambda x: int(x) < 0, l1))
# l3 = list(filter(lambda x: type(x) == str, l1))
# l4 = list(filter(lambda x: type(x) == int, l1))
# l5 = list(filter(lambda x: type(x) == str and int(x) < 0, l1))
# l6 = list(filter(lambda x: x, l1))
# l6a = list(filter(lambda x: x == True, l1))
# l7 = set(filter(lambda x: x % 2, range(10)))
# print('l1=', l1, id(l1))
# print('l2=', l2, id(l2))
# print('l3=', l3, id(l3))
# print('l4=', l4, id(l4))
# print('l5=', l5, id(l5))
# print('l6=', l6, id(l6))
# print('l6a=', l6a, id(l6a))
# print('l7=', l7, id(l7))
#
# print(1 == True)
# print(1 == 1.0)
# print(True == 1.0)
#
# print(0 == False)
# print(0 == 0.0)
# print(False == 0.0)
#
# print((2<3) * 5)
# print((2>3) * 5)

# ................................

# webs = [
#     'google.com',
#     'sport.ua',
#     'mail.ru',
#     'snn.com',
#     'yandex.ru',
#     'duan.edu.ua',
#     'pisem.net'
# ]
#
# stop = [
#     'mail.ru',
#     'yandex.ru'
# ]
#
# print(webs)
# symbols = '.ru'
# # my_webs = list(filter(lambda x: not x.endswith(symbols), webs))
# # my_webs = list(filter(lambda x: x.endswith('.ua') or x.endswith('.com'), webs))
# my_webs = list(filter(lambda x: not (x in stop), webs))
#
# print(my_webs)

####################################### ZIP

# text = 'Hello'
#
# l1 = list(text)
# l2 = list(range(5, 100))
#
# l3 = list(zip(l2, l1))
#
# print(l1)
# print(l2)
# print(l3)
#
# print(list(enumerate(l1, 5)))

############################################ reduce ##################

from functools import reduce

# def foo(x, y):
#     print('x=', x, '* y=', y)
#     return x*y


# l1 = [2, 3, 4, 5]
# print('reduce =', reduce(foo, l1))

# print('\nreduce =', reduce(lambda x, y: x * y, l1))

################################################


# ................................................ sort


# l3 = [422, '373', 195, '867', '18899']
# print('l3 ->', l3, id(l3))

# l3 = list(map(int, l3))
# l3 = list(map(str, l3))
# print('map ->', l3)

# l3.sort()
# l3.sort(key=lambda x: int(x), reverse=True)
# l3.sort(reverse=True)
# print(l1)
# print('sort ->', l3, id(l3))

############################ sorted()

# t = 'Hello'
# print(t)
# l1 = sorted(t, reverse=True)
# l1 = sorted(map(str, range(19)), reverse=False)
# l2 = sorted(range(19), key=lambda x: str(x),  reverse=False)
# print(l1, type(l1))
# print(l2, type(l2))

# l = [-2.45, '234', 456, '-67.998']
# ll = sorted(l, key=lambda x: abs(float(x)))
# print(ll)




# .........................................

#
# city = ['Dnipro', 'Kiev', 'Lviv', 'Odessa', 'Rivno']
# population = [1000000, '4500000', 900000, '850000', 200000]
#
# popul = list(map(int, population))
# print('population = ', population)
# print('popul = ', popul)
#
# population = list(map(lambda x: int(x/1000), popul))
# print(population)
#
# res = list(zip(city, population))
# # res = list(zip(range(1, 30), city, population))
# print(res)
#
# res.sort(key=lambda x: x[1], reverse=True)
# print(res)
#
# res = list(filter(lambda x: x[1] > 800, res))
# print(res)
#
# print(*res, sep='\n')
# print()
# print()
# for i in res:
#     print(*i, sep='\t')


################### НАГАДУЮ!!!! ##################################
# a = ' '   # False - 0 0.0 '' [] () {} False      True -
# if a:
#     print(a, 'YES!!!')
# else:
#     print('NNNNNNNOOOOO!')

####################################################

# dict1 = {
#     'Lviv': 900,
#     'Dnipro': 1000,
#     'Kyiv': 4500,
#     'Rivno': 250
# }
#
# # res = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
# res = sorted(dict1.items())
# print(*res, sep='\n')

#####################################################

############################################## Напоминание! #### END ##############


# l1 = range(97, 108)
# l2 = [chr(i) for i in range(97, 108)]
# print(l1)
# print(l2)
# l3 = list(zip(l1, l2))
# print(*l3, sep='\n')
#
# for key, vol in l3:
#     print(key, vol, sep=' ->\t')

# .................................


# l1 = [2, '-3', -45, '67', '-99']   #  ''
# # l2 = list(filter(str, l1))
# l2 = list(filter(lambda x: type(x) == str, l1))
# print('l2 =', l2)
#
#
# l2 = list(filter(lambda x: type(x) == str, l1))
# l3 = list(map(lambda x: (int(x)+2) ** 2, l1))
# l4 = list(map(int, l1))
# print('l1 =', l1)
# print('l2 =', l2)
# print('l3 =', l3)
# print('l4 =', l4)
# print('max =', max(l4))
#
#
#
# l1 = list(range(7))   # 0, 1, 2, 3, 4, 5, 6
# l2 = list(range(5, 20)) # 5,6,7,8,9,10,11,12,13,14,15,16....
# l3 = list(range(15, 100)) # 15,16, 17,,,....
#
# l4 = list(zip(l1, l2, l3, range(3, 6))) # 3,4,5
# print(l1)
# print(l2)
# print(l3)
# print(l4)
# print(len(l4))



# l1 = 'Hello, world!'
# print(l1)
# l2 = list(zip(range(len(l1)), l1))
# print(l2)
#
# print(list(enumerate(l1)))

#############################################
