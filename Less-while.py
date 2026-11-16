
# n = int(input('Input number of steps in cycle : '))
# sum_ = 0
#
# for i in range(n):
#     num = int(input('input number : '))
#     if num == 0:
#         break
#     sum_ += num
#     print('step No.', i, sum_)
# else:
#     print('number of the cycle over')
#
# print('===== Sum =', sum_, 'Finish!!!!')

# sum_ = 0
# n = int(input("n="))
# while n != 0:
#     sum_ += n
#     n = int(input("n="))
# print("sum = ", sum_)




#################################################
##### Нескінченна послідовність #################

# sum_ = 0
# step = 0
# num = "ghj"
# # while True:                          # 0  0.0    False  ''  []  ()
# # while num:                          # 0  0.0    False  ''  []  ()
# while step < 10 and num:                          # 0  0.0    False  ''  []  ()
#     num = int(input('input number : '))
#     # if not num:
#     # if num == 0:
#     #     print('Finish!!!!!!!!!!!!!!!')
#     #     break
#     sum_ += num
#     step += 1
#     print('step =', step, 'number =', num, 'summa =', sum_)
#
# print('sum =', sum_)




#################################################
########### while as for ########################

# n = int(input('Input number of steps in cycle : '))
# a = n
#
# while a:
#     print('step No.', n - a + 1)
#     a -= 1
#
# print('Finish!!!!   a =', a)

#################################################

text = 'Hello, world!'
# for i in text:
#     if i != 'l':
#         print(i, end=' -> ')
#
# print()
#
# for i in range(len(text)):
#     if i % 3 == 0:
#         print(i, '->', text[i])
#     if text[i] != 'l':
#         print(text[i], end=' -> ')





# step = 0
# while step < len(text):
#     if text[step] != 'l':
#         print(step, '->', text[step])
#     step += 1
#
# print('\nFINISH!!!!!!!!!!!!!!')



##########################################################
# text = 'Hello, world!'
# i = -1
# symbol = input('Введіть символ :')
#
# while i < len(text):
#     i += 1
#     if i % 2:
#         print('_', end=' ')
#         continue
#     print(text[i], end=' ')
#     if text[i] == symbol:
#         print('\n\nbreak in position No.', i)
#         break
# else:
#     print('\n\nNo break! No symbol!')
#
# print('!!!!!!!!!!FINISH!!!!!!!!!')

##########################################################
############ password ####################################

# import time
#
# password = "123"
# attempts_limit = 3 # кількість спроб до паузи
# pause = 7 # пауза в секундах
#
# attempts = attempts_limit
# user_input = ""
#
# while user_input != password:
#     user_input = input("Введіть пароль: ")
#     attempts -= 1
#     if attempts <= 0:
#         print('Чекайте...')
#         time.sleep(pause)
#         attempts = attempts_limit
#
# print("Доступ відкрито.")

#########################################################
###########################################################
############## найменший ділільник ##########################

# n = int(input('Введіть будь-яке число : '))
# i = 2
# mark = True
# # while n % i != 0 and i < (n//2 + 1):
# #     i += 1
# #
# # if i != n//2 + 1:
# #     mark = False
#
#
# for i in range(2, n//2 + 1):
#     # print(i)
#     if n % i == 0:
#         mark = False
#         break
#
# if mark:
#     print(f'{n} - просте число!', i)
# else:
#     print(f'{n} - НЕ просте число!', i)
#
# print(f'Найменший ділільник для {n} дорівнює {i}.')





#######################################################
########### Перетворення у двоїчний код ##############

# n = int(input('Введіть будь-яке ціле число : '))
# binary = ''
# d = 2
# while n > 0:
#     b = n % d
#     binary = str(b) + binary
#     n = n // d
#     # print(binary)
# print(binary)



########### Перетворення у шістнадцятирічний код ##############

# n = int(input('Введіть будь-яке ціле число : '))
# binary = ''
# d = 16
# while n > 0:
#     b = n % d
#     if b == 10:
#         b = 'A'
#     elif b == 11:
#         b = 'B'
#     elif b == 12:
#         b = 'C'
#     elif b == 13:
#         b = 'D'
#     elif b == 14:
#         b = 'E'
#     elif b == 15:
#         b = 'F'
#
#     binary = str(b) + binary
#     n //= d
#
# print(binary)

################################################
##### Вгадай літеру   ##########################


# text = input('Input word, please : ')
# attempt = len(text)
# n = 80
# while attempt:
#     symbol = input('Input a symbol, please: ')
#     # if text.count(symbol):
#     if symbol in text:
#         print('\n' * 3)
#         print('!' * n)
#         print('You win!!!'.center(n, ' '))
#         print(('The symbol "' + symbol + '" is in the text !').center(n, ' '))
#         print('!' * n)
#         break
#     print()
#     attempt -= 1
#     print('No symbol "' + symbol + '" in the word!')
#     print('Try again, please! You have', attempt, 'attempts.')
# else:
#     print('=' * n)
#     print("Sorry, You don't have any attempt...")
#     print('=' * n)

############################################ KH-26!!!!!!!!!!!!!!!!!!!!!


#########################################################
################# random ################################
# import random
#
# # print(dir(random))
# # print(*dir(random), sep='\n')
#
# for i in range(10):
#     # print(random.random())
#     print(random.randint(0, 10), end=' ')
#     # print(int(random.random() * 100) - 50, end=' ')
#
#
# # text = 'abcdefg'   #
# # # text = '0123456789'
# # for i in range(30):
#     # print(text[random.randint(0, len(text))-1], end=' ')
#     # print(random.choice(text), end=' ')
#     # print(int(random.random()*11), end=' ')
#     # print(random.random(), end=' ')
#     # print(random.randint(0, 10), end=' ')
#
# # l = ['dog', 'cat', 'Ukraine', 'University']
# #
# # for i in range(10):
# #     word = random.choice(l)
# #     print(word, end=' ')


##################################################
################### Вгадай число #######################
# import random
#
#
# number = random.randint(0, 9)
# attempts = 0
# guess = -5
# # while True:
# #     attempts += 1
# #     guess = int(input("Вгадай число від 0 до 9: "))
# #     if guess == number:
# #         print(f"Вітаю! Ви вгадали число {guess}. Кількість Ваших спроб {attempts}.")
# #         break
# #     else:
# #         print(f"Помилка. Спробуй ще раз. Кількість Ваших спроб {attempts}.")
# # print('FINISH!!!!!!!!!!!!!!!!')
#
# while guess != number:
#     attempts += 1
#     guess = int(input("Вгадай число від 0 до 9: "))
#     print(f"Помилка. Спробуй ще раз. Кількість Ваших спроб {attempts}.")
#
#
# print('FINISH!!!!!!!!!!!!!!!!')
# print(f"Вітаю! Ви вгадали число {guess}. Кількість Ваших спроб {attempts}.")
#

#####################################################
##################### 21 ############################
#####################################################
# import random
#
#
# total = 0
# total_fr = 0
# cont = 'y'
# # a = random.randint(1, 11)
# screen = 20
#
# while cont.lower() == 'y':
#     a = random.randint(1, 11)
#     total += a
#     print('cart =', a, 'Total =', total)
#     if total > 21:
#         print(':-( ' * screen)
#         print(f'You lost! Total sum is {total}. Sorry...'.center(screen * 4, ' '))
#         print(':-( ' * screen)
#         break
#
#     cont = input('play? (y/n) :')
# else:
#     while total_fr < 15:
#         a_fr = random.randint(1, 11)
#         total_fr += a_fr
#         if total_fr > 21:
#             print('!' * screen * 4)
#             print('You win! I am loser....'.center(screen*4, ))
#             print(f'I take {a_fr} and as a result I have {total_fr}...(((('.center(screen*4, ' '))
#             print('!' * screen * 4)
#             break
#     else:
#         if total > total_fr:
#             print('!' * screen * 4)
#             print(f'You win! Total sum is less than 21 and more then my score.'.center(screen*4, ' '))
#             print(f'You have {total}! But I have {total_fr}...'.center(screen*4, ' '))
#             print('!' * screen * 4)
#         elif total == total_fr:
#             print('?'*screen*4)
#             print('No any winner!'.center(screen*4, ' '))
#             print('We have the same result!!!'.center(screen*4, ' '))
#             print(f'You have {total}! And I have {total_fr}...'.center(screen*4, ' '))
#             print('?' * screen * 4)
#         else:
#             print(':-( ' * screen)
#             print(f'You lost! I have more. Sorry... '.center(screen*4, ' '))
#             print(f'You have {total}. I have {total_fr}. Sorry... '.center(screen*4, ' '))
#             print(':-( ' * screen)

##############################################################

# Завдання
# Надрукуйте таблицю множення за допомогою циклу while

# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# .....
# 9 * 9 = 81







# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i, "*", j, "=", i*j)
#         j += 1
#     print('-'*80)
#     i += 1

###########################################



# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")
#         # print(i, "*", j, "=", i*j)
#     print('-'*80)




########################## END ######################


#  0 1 1 2 3 5 8 13 21 44 65 109


# a = 3
# b = 5
# print(a, b)
#
# a, b = b, a+b
# print(a, b)
#
# a, b = b, a+b
# print(a, b)