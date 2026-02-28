# змінний неупорядкований(?) набір даних у форматі "ключ-значення"

# l = [ 'a', 'c', 'd', 'c']
# d = {1: 'fghf', (1, 2): {'d': 34}, 1.0: 'hjgj', True: 'a', 'key1': ['b', 1, 2], 'key2': 777, 3.14: 'c'}

# print(l[3])
# print(d['key2'])
# print(d[(1, 2)]['d'])
# print(d)

d1 = {'name': 'Ivan', 33: 3244, 'surname': 'Pupkin', 5: {1: 'jhlkkk'}}
d1 = {
    'name': 'Ivan',
    33: 3244,
    'surname': 'Pupkin',
    5: {1: 'jhlkkk'}
}

d2 = dict([('a', 'A'), ['UK', 'London'], [1, 'C'], 'UA'])

d3 = dict(['UA', '34', 'j4'])




# print(d1)
# print(d2)
# print(d3)
#
# t = list(enumerate('Hello'))
# print('t=', t)
#
# d2 = dict(t)
# d2[-1] = 'Xa-Xa!'
# print('d2=', d2)
# print(d2[-1])  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# d3 = dict(name='Ivan', surname='Petrov', nation='Ukrainian', age=18)
#
# # print('d1=', d1, id(d1))
# print('d2=', d2, id(d2))
# print('d3=', d3, id(d3))
#
# d4 = {
#     'key1': 23452,
#     'key2': 456.7668,
#     'key21': 0,
#     'key22': 456.7668,
#     'key23': 456.7668,
#     'key24': 456.7668,
#     'key246': 456.7668,
#     'key3': 456.7668
# }
#
# print(d4)



# print(d1)

# print(d1['name1'])
# print(d1.get('name1'))
# print(d1.get('name1', 'Oooops! No key name1!'))


# d2['foo'] = 'Function'
# d2[0] = 'Function'
# print('d2=', d2, id(d2))
#
# d2['foo1'] = [1, 2, 3]
# print('d2=', d2, id(d2))
#
# d2['foo'] = dict(enumerate('Hello'))
# print('d2=', d2, id(d2))

#
#
#
# print('d1=', d1, id(d1))
# # d5 = d1
# # d5 = d1.copy()
# d5 = dict(d1)
# print('d5=', d5, id(d5))
# d5['name'] = 'Gosha'
# print('d1=', d1, id(d1))
# print('d5=', d5, id(d5))


# d = {}
# d = dict()
# print(d, type(d), id(d))



#############################################

d1 = {'name': 'Ivan', 33: 3244, 'surname': 'Pupkin', 5: {1: 'jhlkkk'}}
#..........................................

#................................
# print(d1.keys())
# print(list(d1))
#
# l = list(d1.keys())
# print(l, type(l))
#
# # # # # #................................
# print(d1.values())
# print(list(d1.values()))

# print(d1)
# print(list(d1))  # !!!!!!!!!!!!!!!!!!
# #................................
# print(d1.items())
# print(list(d1.items()))
#
# for key, value in d1.items():   #   a, b = 1, 2
#     print(key, value, sep='\t-> ')



# for k in d1.items():
#     key, value = k
#     print(k, key, value)



#................................
# print('d1=', id(d1), d1)
# val = d1.pop('name')
# # val = d1.pop('name346', 'No key!!!!!!')
# print('d1=', id(d1), d1)
# print('val=', val)
# # #
# d1['name'] = val
# d1['n'] = 999
# print('d1=', id(d1), d1)
# dd = d1.popitem()
# dd = d1.popitem()
# print('d1=', id(d1), d1)
# print(dd, type(dd))

##################################
# d = {}
# for i in range(5):
#     d[i] = input(f'{i+1}-й елемент = ')
#
# print(d)
# print(d.popitem()[1])
# print(d)
# print(d.popitem()[1])
# print(d)
# print(d.popitem()[1])
# print(d)
# print(d.popitem()[1])
# print(d)
# print(d.popitem()[1])
# print(d)
# print(d.popitem()[1])
# print(d)
# print(d.popitem()[1])
# print(d.popitem()[1])
# print(d.popitem()[1])
# print(d)
# print(d1)
#
# it = d1.popitem()
# print('d1=', id(d1), d1)
# print(it)
# it = d1.popitem()
# print('d1=', id(d1), d1)
# print(it)
# key, val = it
# print(key)
# print(val[1])
#
# it = d1.popitem()
# print('d1=', id(d1), d1)
# print(it)

#................................
# print(d1)
# v = d1['name']
# v = d1.get('name1', 'Oooops! No key!')

# d1['name'] = 'KH-25'

# v = d1.setdefault('name1', 'NoName')
# v = d1.setdefault('Petrov', '100')
# print('v=', v)
# print('d1=', d1)

# d11 = {'name 1': 'a', 4: 'b', 6: 'c'}
# d11 = {}
# for i in range(1, 9):
#     d11.setdefault(f'name {i}', 'NoName')
#
# d11['name 3'] = 'Mykola'
# print('d11=', id(d11), d11)
#
# #................................
# d11.clear()
# # d11 = {}
# # d11 = dict()
# print('d11=', id(d11), d11)


#................................
# l1 = ('rt', (4, 99))
# print(dict(l1))
# # l1 = ['ab', 'ht']
# l1 = [('He', 'llo')]
# print(dict(l1))


# #................................
#
# d4 = {1: 2, 'peace': 'future', 99: {0: 5, 't': 'text'}}
# print('d4=', id(d4), d4)
# print(d4[99])
# print(d4[99]['t'])

##########################################

#................................


# txt = 'Hello'
# d1 = dict(enumerate(txt))
# d2 = dict(enumerate(txt, 3))
# print(d1)
# print(d2)
#
# d1.update(d2)
# print(d1)
#................................


#................................
# print(d1)
# print('name' in d1.keys())
# print('Pupkin' in d1.values())
############################################# KH-25-1 KH-25-2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# print('name' in d1)
# print('KH-24' in d1)
#
# for i in d1.items():
#     print(i)

#
# lst = ['a', 'b', 'c', 'd']
# # d3 = dict.fromkeys(lst, 'NoValue!')
#
# # d3 = dict.fromkeys(range(1, 6), input(' value : '))
# d3 = dict.fromkeys([chr(i) for i in range(97, 110)], input(' value : '))
#
# d3['b'] = '50x50'
# print('d3', d3, id(d3))

###########################


# d3 = {}
# for i in range(int(input('number of students = '))):
#     d3[input('surname : ')] = input('name = ')
# print('d3', d3, id(d3))


###################################

#
# d5 = {}
# d5[1] = 'aaaaaaaaaa'
# d5[0] = 'xxxxxxxxx'
# d5['1'] = 'bbbbbb'
# d5['abc'] = '00000'
# d5[True] = '999999'
# d5[False] = 'AAAAAA'
# d5[1] = d5[0] = 0
# print('d5', d5, id(d5))

# ###################################
#
# # !!!!!!! MAP  ZIP !!!!!!!!!!!
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = ['a', 'b', 'c', 'd']
# # print('l1 =', l1)
#
# def foo(x):
#     return 2*x + 4 * x**2


# l1 = list(map(foo, l1))
# print('l1 =', l1)
# print('l2 =', l2)
#
#
#
#
# l3 = list(zip(l2, l1))
# l4 = dict(l3)
# print(l3)
# print(l4)
#
#
#
#
# print(l4.items())
#
# print(list(l4.items()))
#
# dd = dict(zip(l4.values(), l4.keys()))
# print('dd =', dd)
# #############################################
#
# print(d5)
# ddd = d5
# k = '1'
# s = d5.pop(k)  # LIFO    STACK
# print(s)
# print(d5)
# print(ddd is d5)
# d5[k] = s
# print(d5, id(d5))  # LIFO
#
# print(ddd == d5)
# print(ddd is d5)
#
#
# print(d5.popitem())
# print(d5, id(d5))  # LIFO
# print(d5.popitem())
# print(d5, id(d5))  # LIFO


##############################################
#
# d_stack = {}
# for i in range(7):
#     d_stack[i] = input(f'введи {i}-й елемент = ')
# for i in range(7):
#     print(f'{i}-й елемент = ', d_stack.popitem())



#######################################

# dd = {x: chr(x) for x in range(97, 115)}
#
# dd = {x: chr(x) for x in range(97, 115) if x % 2 == 0}
#
# dd1 = {x: chr(x) for x in range(97, 115) if x % 2}
# dd.update(dd1)
#
# print(dd)
# print(dd1)
# for k, v in dd.items():
#     print(k, v, sep=' -> ')
# print(dd[100])

############################



import random


# city = ['Kyiv', 'Poltava', 'Dnipro', 'Lviv']
# population = [4000, 700, 1000, 850]
# # dict_ua = {x: y for x in city for y in population}  #  ???????????
# # dict_ua = {city[i]: population[i] for i in range(4)}
# dict_ua = {x: y for x, y in zip(city, population)}
# dict_ua = dict(zip(city, population))

# print('dict_ua :', dict_ua)
#
# print('list(dict_ua.values()) :', list(dict_ua.values()))
# print('list(dict_ua.keys()) :', list(dict_ua.keys()))
# print('list(dict_ua) :', list(dict_ua))
# print('list(dict_ua.items()) :', list(dict_ua.items()))

# # ........................
# key = random.choice(list(dict_ua))
# print('key =', key)
# print(key, dict_ua[key])

# # #***************** Сортировка по населению
# l1 = list(dict_ua.items())
# print('items : ', l1)
# # l1.sort()
# l1.sort(key=lambda x: x[1], reverse=True)
#
# for i in l1:
#     print(*i, sep='\t')

#################################
# def foo(x):
#     return x**2
#
# print(foo(5))
#
#
# print((lambda x: x**2)(5))
#
# foo1 = lambda x: x**2
#
# print(foo1(5))

# ############################################
# ........... QUIZ
# key = random.choice(list(dict_ua.keys()))
#
# question, answer = key, dict_ua[key]
#
# print("What's population in", question, '?')
# a = int(input('population?  = '))
#
# if a == answer:
#     print('You are right!')
# else:
#     print('You are wrong!')
#
# print('right answer :', answer)



#######################################################
#******* Сортировка букв любого введенного текста
# symbols = set(['ON ', 'THE', 'TO ', 'AND'])
# print('Перелік символів:\n', *symbols)
#
# # text = input('Input any text : ').upper()
# text = '''
# Bring on advanced features like asset
# and configuration management to support ITSM practices.
# Minimize distractions with expanded, personalized support,
# and empower your admins with added controls and security
# safeguards. See value quickly with faster deployments
# compared to legacy tools.
# '''.upper()
# print('Введений текст:\n', text)
#
# set_count = dict(zip(list(symbols), list(map(text.count, symbols))))
# print('\nОбчислений текст множиною:\n', set_count)
#
# list_count = list(set_count.items())
# print('\nОбчислений текст списком:\n', list_count)
#
# list_count.sort(key=lambda x: x[1], reverse=True)
# print('\nВідсортирований список:\n', list_count)
#
# for element in list_count:
#     print(*element, sep='\t')

###################################################
######################################################
#******* Сортировка букв любого введенного текста


# text = input('Input any text : ').upper()
# text = '''
# Bring on advanced features like asset
# and configuration management to support ITSM practices.
# Minimize distractions with expanded, personalized support,
# and empower your admins with added controls and security
# safeguards. See value quickly with faster deployments
# compared to legacy tools.
# '''.upper()
# print('Введений текст:\n', text)
#
# t = []
# for i in text:
#     if i != ',' and i != '.':
#         t.append(i)
#
# text = ''.join(t)
#
#
# symbols = set(text.split())
# print('Перелік символів:\n', *symbols)
#
# set_count = dict(zip(list(symbols), list(map(text.count, symbols))))
# print('\nОбчислений текст множиною:\n', set_count)
#
# list_count = list(set_count.items())
# print('\nОбчислений текст списком:\n', list_count)
#
# list_count.sort(key=lambda x: x[1], reverse=True)
# print('\nВідсортирований список:\n', list_count)
#
# for element in list_count:
#     print(*element, sep='\t')

###################################################





# text = 'Hello, world!'
#
# a = dict(enumerate(text))
# # a = dict(zip(range(len(text)), text))
# print(a)
# # del a[5]
# # a[5.55] = 'W'
# for key, val in a.items():
#     print(key, '-', val, sep='', end='  ')
# print()

# !!!!!!!!!!!!!!!!!!!!!!!!! END



############# ФОРМИРОВАНИЕ СЛОВАРЯ ПО СПИСКУ #############
# keys = 'ten, one, five, two, three, four'
# keys = keys.split(', ')
# # values = ['номер ' + str(i) + ' в строке' for i in range(1, len(keys)+1)]
# # dic = dict(zip(keys, values))
# dic = {}
# for i in range(len(keys)):
#     dic[keys[i]] = 'номер ' + str(i + 1) + ' в строке'
# print(dic)