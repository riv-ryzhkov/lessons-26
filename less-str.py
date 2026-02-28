# a = 'Hello, world!'
# print(a)

# Незмінна послідовність символів!!!!!!!!!!!!!!!!!!!!!!!

################################################

# a = 'What's your name?'
# a = "What's your name?"
#
# print(a)

##################################################


# text = '''
# Before we can fix any bugs or add any features,
# we need to get the source code onto your computer.
# These instructions are for Ubuntu Linux,
# which is the easiest environment to configure
# for OpenShot development. If you are using another OS,
# I suggest running a virtual machine with
# Ubuntu LTS before continuing any further.
# '''
#
# print(text)
###############################################

# text = """
# Before we can fix any bugs or add any features,
# we need to get the source code onto your computer.
# These instructions are for Ubuntu Linux,
# which's is the easiest environment to configure
# for OpenShot development. If you are using another OS,
# I suggest running a virtual machine
# with Ubuntu LTS before continuing any further.
# """
#
# print(text)

######################################################

# text = 'How are you!'
# print(text[-12])
# print(text[0])
# print(text[4:7])
# print(text[4:])
# print(text[:7])
# print(text[:])
# print(text[::2])
# print(text[::-1])
# print(text[-1:-10:-3])

############################################
# print('Hello, ' + 'world!')
# print('Hello' + 'Hello' + 'Hello')
# print('Hello' * 3)
# print('*' * 80)
# print('.' * 80)

##########################
# text = 'How are you!'
# # text[0] = 'W'
# #
# text1 = text
# print('text :', text, id(text))
# print('text1 :', text1, id(text1))
# text = 'W' + text[1:]
# print('text :', text, id(text))
# print('text1 :', text1, id(text1))

###################################

# text = 'How are you!'
# print(len(text))
# for i in range(len(text)): # 0,1,2,3....11
#     print(i, text[i], sep='->', end='    ')
# print()
# print()
# for key, vol in enumerate(text):
#     print(key, vol,  sep='->', end='    ')


############################################

# a = r"C:\temp\new.txt"
# print(a)

# print('hjg\t567')
# print('h\t457')
# print('hj\t547')
# print('hj\t45')



# print(r'C:\temp\new.txt')

##############################################

# a = 'How Are You!'
a = 'duan.edu.ua'


# for i in range(256):
#     print(i, '->', chr(i), '\t', hex(i))



# for i in a:
#     print(i, '->', ord(i))

# print('Temperature is ' + chr(177) +'2' + chr(176) + 'C')

# print(a.startswith('How Are'))
# print(a.endswith('.ua') or a.endswith('.com'))
# print(a)

######################################

# a = 'How are You!'
#
# b = a.split()
#
# print(a, type(a), id(a))
# print(b, type(b))
# #
# a = ' '.join(b)
# print(a, type(a), id(a))

##########################################
# a = '------Hel------lo!-----'
# a = '      Hello     '
# print(a)
# print(a.strip())
# print(a.strip('-'))
# print(a.rstrip('-'))
# print(a.lstrip('-'))

# a = 'Hello!                     '.strip()
# print(a, len(a))
#
# a = 'Hello'.strip()
# b = '   Hello          '.strip()
# print(a, b, a == b)

# print('=========================')
# b = a.lstrip('-')
# print(a)
# print(b)

############################################
# a = 'How are You!'
#
# n = 80
# print('=' * n)
# print(a.center(n))
# print(' '*int((n/2-len(a)/2)) + a)
# print(a.center(n, '*'))
# print((a*2).center(n, '.'))
# print((a*5).center(n, '$'))
# print('=' * n)

####################################################



# a = 'How are Yooooooooooooou!'
# print(a, id(a))
# b = a.replace('o', 'O', 5)
# # a = a.replace('o', 'O', 5)
# print(a.replace('H', 'W'))
# print(a, id(a))
# print(b, id(b))
# # ................................

# a = 'How are You!'
# print(a, id(a))
#
# print(a.replace('H', 'W'))
# a = a.replace('H', 'W')
#
# print(a, id(a))

#######################################
# a = 'University'
# b = 'Ukraine'
# c = 'Dnipro'

# print('I love {0}, {1}, and {0}'.format(a, b, c))
# print('I love {str3}, {str2}, and {str2}'.format(str0=a+b, str1=a, str2='Victory', str3=c))

# print(f'I love {a}, {b} and {c+a}')
#
# name = 'Vasya'
# surname = 'Koval'
# age = 25
#
# print(f'My name is {name}, surname is {surname}.')
# print(f'I am {age} years old.')

###############################
# a = 'How are You!'
# print(a.find('ooo'))
# t = a.find('YYY')
# print(a[t])
# print(a.rfind('o'))
#
# print(a.index('YY'))
# print(a.rindex('o'))


#################################

# a = 'How are You!.ua'
#
#
# # print(a.startswith('How'))
# print(a.endswith('.ua') or a.endswith('.com'))

###################################
#
############################################
# line_size = 80 # it is line size
#
# # symbol_mark = chr(176) # это символ для строки
# symbol_mark = '=' # это символ для строки
#
# symbol_space = ' '
#
# text_our = 'Happy new year!'*3
#
# # text_your = input('Input your text : ')
#
#
# print(symbol_mark * line_size)
# print(text_our.center(line_size, symbol_space))
# # print(text_your.center(line_size, symbol_space))
# print('Hello, word!'.center(line_size, ' '))
# print(symbol_mark * line_size)

####################################################



# a = 'hello'
# b = 'helLo............'
# c = 'Hello, world!'
#
# print(a > b)
# # print(a > c)
# # print(b > c)
# print(a, a[3], ord(a[3]))
# print(b, b[3], ord(b[3]))

#
# print(len(a))
# print(len(b))
# print(len(c))
#
# print(ord(c[5]))



# for i in range(256):
#     print(i, '->', chr(i))


# print('w ->', ord('w'))
# print('H ->', ord('H'))
#
# print('. ->', ord('.'))
# print(', ->', ord(','))


############################################


# a = 'Hello! How are you!'
# print(a.count('x')) # 0  False
#
# if a.count('x'):
#     print('Літера існує!')
# else:
#     print('Літера не існує!')

#
#
#
#
# symbol = 'o'
# print(a[a.find(symbol)+3]*5 if a.count(symbol) else 'No symbol!')
#
#
# #
# print(a[a.find('x')])
# print(a[a.index('x')])
#
#
#
# symbol = input('Inp symbol :')
#
# # if a.count(symbol):
# if symbol in a:
#     print('YES!')
# else:
#     print('No!')


########################################

# a = 'How are You!'
# print(a, id(a))
# # a = a.upper()
# # a = a.lower()
# # a = a.title()
# # a = a.capitalize()
# a = a.swapcase()
# print(a, id(a))

###############################################

a = '34'

# print(a, 'a.isalpha() ', a.isalpha())
# print(a, 'a.isdigit()', a.isdigit())
# print(a, 'a.isalnum()', a.isalnum())
# print(a, 'a.islower()', a.islower()) # !!!!!!!
# print(a, 'a.isupper()', a.isupper())
# print(a, 'a.istitle()', a.istitle())
# print(a, 'a.isspace()', a.isspace())
# print(a, 'a.isprintable()', a.isprintable())
#
# b = a + chr(188)
# print(chr(188))
# print(b)
# # print(float(b))
# print(b, 'isnumeric ->', b.isnumeric())
# print(b, 'isdigit ->', b.isdigit())

######################################


# a = '5667786x3TYKJb cbcKJHKLJ 8\n2HKLJLJLbc\t ({}}0&&5..$$$cb hdfmf8472ic 329'
# res = ''
# digit = ''
# text = ''
#
# for i in a:
#     if i.isupper() or i.isdigit():
#     # if not i.isspace():
#     # if i.isdigit():
#         digit += i
#     elif i.isalpha():
#         text += i
#     else:
#         res += i
#
# print('digit : ', digit)
# print('text  : ', text)
# print('res   : ', res)

#####################################


# for i in 'Vasya', 'Petya', 'Gideon Alexandrovich':
#     # text = 'Hi, {}! Happy birthday!'
#     # print(text.format(i))
#     print(f'Hi, {i}! Happy birthday!')

#########################################

# my_name = input('Input your name, please : ')
# my_country = input('Where are you from? ')
# text = "Hi {1}, let's go to {0}!".format(my_country, my_name)
# print(text)
#
#
# text = "Hi {name}, let's go to {country}!".format(country=my_country, name=my_name)
# print(text)
#
#
# print(f"Hi {my_name}! You are from {my_country}, aren't you?")

########################################################

# ???????????????????????????????????????????
#  Поміняйте місцями два слова, що введені через пробіл

# a, b = input("Введіть два слова через пробіл : ").split()
# b = input("Введіть два слова через пробіл : ").split()
# print(b, a)
# print(b)



#######################################


# a = 'Ukraine, Dnipro'
# b = 'University'
# c = 'my friends'
#
# print(f'I love {a + ' ' + b}, my {b} and {c} of the {b}!')
#
# print(f'\nI live in {a[9:]} ({a[:8]}). '
#       f'\n\tI study in the {b}. '
#       f'\n\t\t So do {c}.')



##################################### END #############################

# text = 'How are you!'
# l = text.split()
# print(text, type(text))
# print(l, type(l))
#
# t1 = ' <=> '.join(l)
# print(t1, type(t1))








############################################# PPT EXAMPLES #############
# a = 'Hello'
# b = 'world'
# c = 'Ukraine'
# name = input("What's your name? ")
#
# d = 'Hi, {3} and {2}!'.format(a, b, c, name)
# d = 'Hi, ' + name + ' and ' + c
# print(d)
# print(a)
# print('W' + a[1:])
# print(a)

# # print()
# # print(a[-3] * 3 + a[-5] + a[-4] + a[-2])
# print(a)
# a = 'h' + a[1:]
# print(a)

#  uyt
#  u yry
#  u rty
#  u ryu y
#  uyu
#  ytu"""
# print(a, len(a))




# a = 'world'
# b = 'Ukraine'
# c = 'University'
# print('Hello, {}!'.format(a))
# print('Hello, {1}!'.format(a, b))
# print('I love {1} and {2}!'.format(a, b, c))
# print('I love {0}, {2} and {1}!'.format(a, b, c))
# print('I love {3}, {3} and {3}!'.format(a, b, c, 'learning'))
# print('I love {str1}, {str3} and {str2}!'.format(str1='You',
#                                                  str2='my friends',
#                                                  str3='my University'))
#


# a = 'How are you!'
#
# for val in enumerate(a):
#     print(val, type(val))



# print(len(a))

# for i in range(len(a)):
#     print(i, '-', a[i], sep='', end='  ')
# print()
# for i, k in enumerate(a):
#     print(i, '-', k, sep='', end='  ')
# print()
# for i in range(len(a)):
#     print(a[-1-i], end='')


# a = 'How are you!'
# # a[0] = 'W'
# a = 'W' + a[1:]
# print(a)


# print(len(a))
# print(a[1])
# print(a[8:11] + a[3:8] + 'the best!')
# print(a[::4])
# print(a[::-1])





# print(a[::-1])

#
# b = "What's your name?"
# c = ''' In Python 3.10,
#     the old parser will be deleted
#     and so will all functionality
#     that depends on it
#     (primarily the parser module,
#     which has long been deprecated).'''




# s = 'Thkjkj Tjhkjhkj jk'
#
# t = s.split()
# print(t)
#
# r = '*'.join(t)
# print(r)







# S = "s\np\ta\nbbb"
# S = r"C:\temp\new"
# print(S)
# print(S.find('e', 5))
# print(S.index('e'))
# print(S.replace('e', 'E'))
# K = S.replace('t', 'T')
# print('S=', S)
# print('K=', K)
# d = S.split('\\')
# print(d)
# print('5765a657'.isdigit())
#
# print('Dfdg Fh'.istitle())
# h = 'Hello!'
# print(h)
# print(':'.join(h))
# print('gh\tjhjk\t\thj\t'.expandtabs(11))
# print('111   ghj   jkh   hkj   1111'.strip('2231'),'=======')


# first_word, second_word = input('Input 2 words with space : ').split()
#
# print(first_word, second_word)
# print(second_word, first_word)