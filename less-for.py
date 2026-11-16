
# for i in 0, 1.2314, 'Hello', 3+5, True:
# for i in range(10, 20, 3):
#     print(i, end=" " )
#
# print('\nEND of cycle')



# for i in 2, 5, 78, 'Hello', 89-3:
#     print(i, i*2)
#     print(i, i*2, sep=' ', end='\n')
#     print(i, i*2, sep='->', end=' === ')



# for i in range(8, 15, 2):   #  [30:45)
#     print(i, end='\t\t')
#     print(i*2, end='\t')
#     print(i*3, end='\t\t')
#     print(i*10)



# i = 100
# for i in range(3):
#     for j in range(7):
#         print(i+1, j+1, sep='', end='\t')
#     print()
# print('i =', i)




# a = 5
# b = 7
# print(a, b)
# a, b = b, a
# # temp = a
# # a = b
# # b = temp
# print(a, b)





# a, b, c, d = 2, 7.68, 'Hello', 4
# print(a, b, c, d)


# a = 2
# b = 7.68
# c = 'Hello'
# d = 4
# print(a, b, c, d)

# a, b = b, a







# print(range(5))
# a, b, c, d = range(4)   # [0;4)

# a, b, c, d = range(-4, -8, -1)
# print(a, b, c, d)

# a1, a2, a3, a4 = range(30, 34)
# print(a1, a2, a3, a4)



# 5! = 1 * 2 * 3 * 4 * 5

# a = int(input('a = '))
# result = 1
# for i in range(1, a+1):
#     # result = result * i
#     result *= i
# print(result)



 # sum = 0 + 1 + 2 + 3 + 4 + 5
# num = int(input('num= '))
#
# sum_ = 0
# for i in range(1, num+1):
#     sum_ += i
# print("Сумма чисел до: ", num, "=", sum_)
#
# print(sum(range(num+1)))


#
# for _ in range(3):
#     print('****************')
#     print('................')







# for i in range(7):
#     if i % 2:
#         continue
#     print(i, '!!!!')
#     if i == 4:
#         continue
#     for j in range(10):
#         if j % 2:  # j%2=0    j%2=1
#             print(i, '->', j, end='\t')  # 6 * 5 = 30
#     print('\t\t', i)





# for i in range(5):
#     a = int(input('a='))
#     if a > 0:
#         continue
#     print(a, a, a, a, a)





# for i in range(10):
#     if i % 2 == 0:
#         print(i, 'Super!')
#         continue
#     elif i % 15 == 0:
#         print(i, 'Stop!')
#         break
#     print(i)
# else:
#     print('No 15 )))))))))')
#
# print('END')
# print('END')
# print('END')

# n = int(input('n = '))
# count = 0
# for i in range(2, n//2+1):
#     count += 1
#     if n % i == 0:
#         print(n, ' НЕ просте! Бо ділеться на', i)
#         break
# else:
#     print(n, ' просте число!')
#
# print('Кількість виконаних циклів ', count)



# ================ ELSE in for !!!! ===============

# a = 'How are You!'
# print(len(a))
# for i in a:
#     print(i)
#     if i == 'o':
#         print(i * 3, end='')
#         continue
#     elif i == 'y':
#         print(i * 5)
#         break
#     print(i, end='')
# else:
#     print('\nNo symbol y!!!')



# for i in "Hello World":
#     print(i)


# a = [i for i in 'Hello']
# a = [i for i in range(15) if i % 2]
# a = [i for i in 'Hello' if i != 'l']
# print(a, type(a))
