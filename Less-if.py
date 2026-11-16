############# print('1 or 1 and 0 = ', 1 or 1 and 0)

#  >    <     ==    <=    >=   !=  ')
# a = 1
# print(a == 2)
# print(2 > 0)
# print(2 > 4)
# print(2 == 4)
# print(2 != 4)
# print(2 <= 4)
# print(2 >= 4)

# print(bool("[0]"))


# print(int(2>0))
# print(int(2>4))



# a = 4
# print((a>3) * 2 + (a<5) * 5)



##############################################

# print('A' == 'a')
# print('Hello' == 'hello')

########################################################
# a = ""
# if a:
#     print('True')
#     print('True')
#     print('True')
#     print('True')
# else:
#     print('False')
#     print('False')
#     print('False')


########################################

# x = int(input('x = '))
#
# if 2 * x == 4:
#     print('2 *', x, '= 4', True)
# else:
#     print('2 *', x, '!= 4', False)


#####################################################


# Визначити чи знаходиться х в межах відрізка [0;4]
#  ---------------0-----------4---------->

# x = int(input('x = '))
#
# if x > 4:
#     print(x, '->   x > 4')
# else:
#     if x == 4:
#         print(x, '->   x = 4')
#     else:
#         if x > 0:
#             print(x, '->   0 < x < 4')
#         else:
#             if x == 0:
#                 print(x, '->   x = 0')
#             else:
#                 print(x, '->   x < 0')



#  ---------------0-----------4---------->


# if x > 4:
#     print(x, '->   x > 4')
# elif x == 4:
#     print(x, '->   x = 4')
# elif x == 0:
#     print(x, '->   x = 0')
# elif x > 0:
#     print(x, '->   0 < x < 4')
# else:
#     print(x, '->   x < 0')


# !!!!!!!!!!!!!!!!!!!!????
# 3000-> 20%   1000-> 10%   500-> 5%

# s = 5000
# if s >= 500:  #   500...999
#     p = '5%'
# elif s >= 1000:  #   1000...2999
#     p = '10%'
# elif s >= 3000:    # > 3000...
#     p = '20%'
# else:
#     p = '0%'   # < 500
# print(p)

#############################################

# s = 5000
#
# if s <= 500:  #   <= 500
#     p = '0%'
# elif s < 1000:  #   501...999
#     p = '5%'
# elif s < 3000:    # 1000...2999
#     p = '10%'
# else:
#     p = '20%'   # >2999
# print(p)

#################################################
#############################################

# a = 0

# print(a, type(a))
# print(bool(a))


# if a:
# # if bool(a) == True:   # 0 -> False 0.0 -> False  '' -> False  [] -> False {} -> False
#     print('True')
# else:
#     print('False')





###############################
# text = ''
# i = 0
# f = 0.0
# b = False
# l = []
# t = ()
# d = {}
# print(text, 'text ->', bool(text))
# print(i, 'i ->', bool(i))
# print(f, 'f ->', bool(f))
# print(b, 'b ->', bool(b))
# print(l, 'l ->', bool(l))
# print(t, 't ->', bool(t))
# print(d, 'd ->', bool(d))

#########################################
####################################################
# ????????????????????????????
# a = 1
# b = True # --->  1    False ---> 0
# c = 2 - 1
# print(id(a))
# print(id(c))
# print(id(int(b)))




# a = 3
# b = 3.
#
# print(id(a))
# print(id(b))
#
# print(type(a) == type(b))
# print(a == b)
# print(id(a) == id(b))
# print(a is b)



###########################
#????????????????????????????
# a = 1
# b = True
#
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)
#
# print(bool(1))
# print(int(True))
# print(int(22>3))
#
#
# print(3 * True)
#
# a = -3
# print(3 * (a>2) + 2 * (a<5) - 4 * (-a == 3))


#########################################
# x = int(input('x = '))
#
# # y = 'Hello!' if x<10 else 'Bye!'
# #
# # print(y)
#
#
# y = (x<10) * 'Hello' + (x>=10) * 'Bye'
#
# print(y)


#########################################

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(2>3)
# print(2<3)
# y=2>3
# print(y)
#
# x = int(input('x = '))
# y = (x<2) * 2 + (x>=2) * 4 + (x>4) * (-1)

# y = (x<12)*'morning'+(x>12 and x<20)*'day'+(x>20)*'night' + '!'
#
# x = int(input('x='))
# x1 = x<12
# x2 = x>12 and x<20
# x3 = x>20
#
# y = x1 * 'morning' + x2 * 'day' + x3 * 'night' + '!'
#
# print('y =', y)




#########################################

# a = 123
# b = 'Hello'
# print(a, b)
# a, b = b, a
# print(a, b)



# a = 45
# b = 138
#
# if a > b:
#     a, b = b, a
#
# print('max = ', b)
#
#
# print('max = ', a if a>b  else b)




# print('=' * 5, '  AND  ', '=' * 5)
# print('0 and 0 and 0 = ', 0 and 0 and 0)
# print('1 and 0 and 0 = ', 1 and 0 and 0)
# print('1 and 1 and 0 = ', 1 and 1 and 0)
# print('1 and 1 and 1 = ', 1 and 1 and 1)
#
# print('=' * 5, '  OR  ', '=' * 5)
# print('0 or 0 or 0 = ', 0 or 0 or 0)
# print('1 or 0 or 0 = ', 1 or 0 or 0)
# print('1 or 1 or 0 = ', 1 or 1 or 0)
# print('1 or 1 or 1 = ', 1 or 1 or 1)
# print('=' * 20)
#
#

# print(1 or 1 and 0)


# print(True)
# print(not True)


# print(1 and not 0 and 1 and 1 and 1 and not 0 and 1)  # -> 1
# print(0 or 0 or 0 or not 0 or 0)


# 1 * 1 * 1 = 1
# 1 * 1 * 0 = 0



# print('1 and 1 or 0 --->', bool(1 and 1 or 0))
# print('0 and 1 or 0 --->', bool(0 and 1 or 0))
# print('0 and 0 or 1 --->', bool(0 and 0 or 1))
# print('1 and 0 or 1 --->', bool(1 and 0 or 1))
# print('1 and 0 or 0 --->', bool(1 and 0 or 0))
# print('1 and 1 or 1 --->', bool(1 and 1 or 1))


#
# print()
# print()
# print('1 or 1 and 0 ---> ', bool(1 or 1 and 0))

################### !!!!!!!!!!!!!!!!!!!!!!!!!!

# print(1 or 1 and 0)

# if True or True and not False:
#     print(True)
# else:
#     print(False)

##########################################

# c = 0
# b = 0
# a = True
#
# if (a or c) and (b or a):
#     print('OK')
# elif 2 == 2:
#     print('*' * 20)
# elif 2 < 5:
#     print('@' * 20)
# elif 2 > 1:
#     print('!' * 20)
# else:
#     print('='*60)

##########################################

# --------- sensors ------------
# a = 1
# b = 1
# c = 1
# d = 1
# e = 0
#
# print(a and not b and not c and d and e) ##########
# print(not a or (b or c or not d) or not e)
# print(a or not b or not c or d or e)
# print(not a and b and c and not d and not e)


# a, b, c, d, e = 1, 0, 1, 0, 1
#
# if (a or b) and c and (d or e):
#     print('Alarm!')






# if a and b and c and d and e:
#     print('Works')
# elif a and not b and d and e:
#     print('Alarm!')
# else:
#     print('STOP!!!!!!!')




###########################################
# Тернарний оператор IF
###################################

# a = int(input('a='))
#
# result = 'Hello!' if a > 0 else 'Buy-buy!'
#
# print(result)

#
#

###############################################


# a = -7
# print('Hello!' if a > 0 else 'Bye!')



####################################################

########## match case

# a = input('Введіть значення :')
#
# match int(a):
#     case 1:
#         print('Один')
#     case 2:
#         print('Два')
#     case 3:
#         print('Три')
#     case _:
#         print('Інше число!')



############################################## END ############################


# l1 = []
#
# for i in range(10):
#     l1.append(i if i % 2 else 0)
# print(l1)



# l2 = [i for i in range(10) if i % 3]    # else не використовується, тому що існує в FOR
#
# print(l2)



#!!!!!!!!!!!!!!*********************** Others
# # (if_elem_is_false, if_elem_is_true)[elem]
# l3 = [(0, i)[i % 2] for i in range(10)]
# print(l3)
#


###################################################
