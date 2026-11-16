# print(123 + '567')
# print('123' + 567)


# print(10/0)




# try:
#     for i in range(1, 5):
#         print(10*'2'/i)
# except (ZeroDivisionError, KeyError):
#     print('Zero!!')
# except TypeError:
#     print('Error by type!!!!!!!!!')
# except:
#     print("Divide by 0")
#     print("The exception was handled")
# else:
#     print('Hello! OK!')
# finally:
#     print('FIN!!!!!')
#
#
# print('Hello!')
# print('Hello!')
# print('Hello!')
# print('Hello!')
#
#
#


#################
# a, b = 1, 0
# try:
#     # print(a/b)
#     # print(m)
#     print("This will not be printed")
#     print('10' + 10)
# except TypeError:
#     print('10' + '10')
#     print("You have added values of incompatible types")
# except ZeroDivisionError:
#     print("Divide by 0")
# except:
#     print('Xa!!!!!!')





############################
#######################
# try:
#     # print('10'+10)
#     # print(1/0)
#     print(a)
# # except :
# except (TypeError, ZeroDivisionError):
#     print("Invalid input")




####################
######################
# raise KeyError("My error message")



# try:
#     a = int(input('a = '))
#     if a == 0:
#         raise ValueError
#     else:
#         print(1 / a)
# except (KeyError, TypeError, ValueError):
#     print("Exception caught")
# else:
#     print('Everything OK!!!!!')
# finally:
#     print("Okay")
#     print("Bye")




# #########################
# try:
#     print(1/0)
# except (ValueError, ZeroDivisionError):
# # except ZeroDivisionError:
#     print("This is a value error")
# else:
#     print('Will this text be printed?')
# finally:
#     print("This will be printed anyway.")






# ######################
# raise ZeroDivisionError('WAW!!!')
# raise KeyError('XA!XA!XA!!!!')
# raise NameError('Glory to Ukraine!!!!')


# ######################
# a, b = int(input()), int(input()) # enter 1 then 0
# # a, b = 1, 0 # enter 1 then 0
# if b == 0:
#     raise ZeroDivisionError('b = 0!!!!!!!!!!!')
# c = a / b


############################
# a, b = int(input()), int(input())
# a, b = 1, 0
# try:
#     if b == 0:
#         raise ZeroDivisionError
# except:
#     print("Divide by 0")
# else:
#     print("Will this be printed?")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!


# ######################
# try:
#     print(10/0)
#     print('1' + 1)
#     print(a)
# except :
#     raise KeyError('Ha-Ha-Ha!!!!')


# ###########
# raise ValueError("Incorrecte value")
# ######################




################################################## ##############
# def func(a, b):
#     return a * b
#
# assert 1 + 2 == 3, "You're making a mistake in the algorithm!"
# assert 2 + 2 == 4, "You're making a mistake in the algorithm!"
# assert 3 + 2 == 5, "You're making a mistake in the algorithm!"
# assert 4 + 2 == 6, "You're making a mistake in the algorithm!"
# assert func(2, 2) == 4, "You're making a mistake in the algorithm!"
# assert func(3, 2) == 6, "You're making a mistake in the algorithm!"
# assert func(2, -2) == -4, "You're making a mistake in the algorithm!"
# assert func(2, 22) == 44, "You're making a mistake in the algorithm!"


################################################## ##############

# number = ''
# while not number:
#     try:
#         symbol = input('Enter your card number without spaces: ')
#         assert symbol.isdigit(), "You've got your money's worth! The culprit is deprived of the NUMBER!"
#         assert len(symbol) > 15, "You've been spoiled for money! Too SHORT number!"
#         assert len(symbol) < 17, "You've got your money's worth! The numbers are more than 16!"
#         number = symbol
#     except AssertionError as err:
#         print(err)
#     print(
#         '\nGood! Your card number :',
#         number[:4], number[4:8], number[8:12],number[12:]
#             )
##############################################################

# def validation(symbol):
#     try:
#         assert symbol.isdigit(), "You've got your money's worth! The culprit is deprived of the NUMBER!"
#         assert len(symbol) > 15, "You've been spoiled for money! Too SHORT number!"
#         assert len(symbol) < 17, "You've got your money's worth! The numbers are more than 16!"
#         assert symbol.startswith('53'), "You've got your money's worth! It's not PrivatBank!"
#         return True
#     except AssertionError as err:
#         print(err)
#         return False
#
#
# number = input('Enter your card number without spaces: ')
# while not validation(number):
#     number = input('Enter your card number without spaces: ')

#
# print(
#     '\nGood! Your card number :',
#     number[:4], number[4:8], number[8:12],number[12:]
#             )




######################## KH-25-1 13/02/2026 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def foo(*args):
#     if args:
#         return 'Yes'
#     else:
#         return 'No'
#
#
# assert (foo(5, 7, 9, -34) == 'Yes')
# assert (2 + 2 == 4), 'Really?!!!!!!!!!!!'
# assert (foo(-5) == 'Yes')
# assert (foo() == 'No'), 'Assert Error'
# assert (foo(8) == 'Yes'), 'Assert Error'
#
# print('ok!!!!!!!!!!!!')





# # ###################################
# try:
#     print(1)
#     assert 2 + 2 == 4
#     print(2)
#     assert 2 + 2 == 5, "It's impossible!"
#     print(3)
# except:
#     print("assert False.")
#     raise
# finally:
#     print("Good!")
# print("Hi!")




# ############################
# assert False, "It's a problem"
# #############################
#






########################################################################
####################################
# Exception with file
####################################

# try:
#     f = open("newfile.txt", 'w')
#     text = input('text = ')
#     if len(text) > 5:
#         raise ValueError
#     f.write(text)
# except:
#     print('Error of the INPUT!!!')
#     print("Length of the text must be les than 5 symbols!")
#     print("Text can not be added!")
# else:
#     print("Nothing went wrong")
# finally:
#     f.close()
#     print("The 'try except' is finished")






# ############################
# class MyError(Exception):
#     def __init__(self, data):
#         self.data = data
#         print('MyError works!!!!!!!!!!!!!!!!!')
#
#     def __str__(self):
#         return repr(self.data)
#
#
# try:
#     f = open("newfile.txt", 'w')
#     text = input('text = ')
#     if len(text) > 5:
#         raise MyError("Text must be less than 5 symbols!")
#     f.write(text)
# except MyError as err:
#     print('INPUT Error!!!!!!!!')
#     print(err)
#     print(err.data)
# else:
#     print("Nothing went wrong")
# finally:
#     f.close()
#     print("The file is closed.")
#     print("The 'try except' is finished")

######################################## END

