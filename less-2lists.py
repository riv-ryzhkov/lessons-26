
a = [[1, 2, -3, 4, -5], [6, 7, 18, 39, 0], [9, 0, -15, 2, 68], [3, 4, 8, 9, 0]]

###########################################
# print('len =', len(a))
# print('a =', a)
# print()
#
#
# print(*a, sep='\n')
# print()
# print(len(a[0]))
# print(a[3][2])

# print(len(a[0]))
# print(a[1][3])
#
#
# print(len(a))
# print(len(a[0]))
#
#
# for line in a:
#     print(*line, sep='\t')
#
#
#
#
#
# print('a[3] =', a[3], type(a[3]))
# print('a[3][1:3] =', a[3][1:3])
# print('a[0][1] =', a[0][1])
# print('a[1][1:3] =', a[1][1:3])

# a[1][1:3] = range(5,12)
# print(a)
#
# for line in a:
#     print(*line, sep='\t')
#########################################
# print('a =', a, id(a))
# print('.' * 20)
#
# a[0] = 5
# print('a =', a, id(a))
# print('.' * 20)
#
# a[0] = [9, 8, 7]
# print('a =', a, id(a))
# print('.' * 20)
#
# a[2][2] = [9] * 5
# print(*a, sep='\n')
# print('.' * 20)

##################################
# print('a =', a)
# a.append(a)
# print('a =', a)
# print('a[-1][-1] =', a[-1][-1][-1][-1][-1][-1][-1][-1])
# print()
# print(a == a[-1])
# print(a is a[-1])
# print(id(a))
# print(id(a[-1]))
# print(id(a[-1][-1]))
#
#
# print('------ *a -----------')
# print(*a, sep='\n')
# print()
# print('------ *a[-1][-1] -----------')
#
# print(*a[-1][-1], sep='\n')
#####################################################

a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [9, 0, 1, 2, 8], [3, 4, 8, 9, 0]]

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end='\t')
#     print()

#
# print()
# for row in a:
#     print(*row, sep='\t')


def my_prn(a):
    for row in a:
        print(*row, sep='\t')

# my_prn(a)

#######################################

a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [9, 0, 1, 2, 8], [3, 4, 8, 9, 0]]
######### Сума елементів матриці ##########
########### За індексом ####################
# sum_of_elements = 0
#
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         sum_of_elements += a[i][j]
#
# print(sum_of_elements)




######### За елементами ###################

# sum_of_elements = 0
#
# for row in a:
#     sum_of_elements += sum(row)
#     # for element in row:
#     #     sum_of_elements += element
# print('sum = ', sum_of_elements)

##############################################

# a = [[1, 2, 3, 42, 5], [6, 777, 8], [9, 0, 1, 2], [3, 4]]

###############################################

# l1 = [1, 2, 3]
# # l2 = l1
# # l2 = list(l1)
# # l2 = l1[:]
# # l2 = l1.copy()
# l2 = [i for i in l1]
#
# l2[0] = 999
# print('l1=', l1, id(l1))
# print('l2=', l2, id(l2))


############ Заповнення матриці ###################
# l1 = [1, 2, 3]
# l2 = [l1] * 3
# my_prn(l2)
# print('l1 =', l1, id(l1))
# print('l2 =', l2, id(l2[2]))
# print()
# l2[0][1] = 9
# my_prn(l2)
# print('l1 =', l1, id(l1))
# print('l2 =', l2, id(l2))
# print()
# print('l2[0] =', l2[0], id(l2[0]))
# print('l2[1] =', l2[1], id(l2[1]))
# print('l2[2] =', l2[2], id(l2[2]))
# my_prn(l2)

###################################################

# n, m = 5, 5
# # a = [[0] * m] * n
# a = [['.'] * m for i in range(n)]
# my_prn(a)
# a[0][0] = 9
# a[2][1] = 8
# print()
# my_prn(a)
# print()
# a[3][1] = 5
# a[2][2] = 98
# a[1][1] = 555
# my_prn(a)

########################################################
# Somme de deux matrices

m = [[1,2,3,4],[5,6,7,8]]
n = [[9,1,8,2],[7,3,6,4]]


# print(m)
# print("len(m)=", len(m))
# print("len(m[0])=", len(m[0]))
# print()
# print(*m, sep='\n')
# print()
# print(*n, sep='\n')
# print()



# s = []
# for i in range(len(m)):
#     s.append([])
#     for j in range(len(m[0])):
#         s[i].append(m[i][j]+n[i][j])





# s = [[m[i][j]+n[i][j] for j in range(len(m[0]))] for i in range(len(m))]
# print(*s, sep='\n')

# print(*[[m[i][j]+n[i][j] for j in range(len(m[0]))] for i in range(len(m))], sep='\n')
#
# my_prn([[m[i][j]+n[i][j] for j in range(len(m[0]))] for i in range(len(m))])
##########################################

# from random import randint
#
#
# def rand_mat(n, m):
#     matrice = []
#     for i in range(n):
#         matrice.append([randint(0, 9) for j in range(m)])
#     return matrice
#
#
# m1 = rand_mat(4, 3)
# my_prn(m1)
# print()
# m2 = rand_mat(3, 4)
# my_prn(m2)
#
# # my_prn(rand_mat(5, 7))
#
#
# def multiplier_matrices(matrice1, matrice2):
#     # Vérification des dimensions
#     colonnes_matrice1 = len(matrice1[0])
#     lignes_matrice2 = len(matrice2)
#
#     if colonnes_matrice1 != lignes_matrice2:
#         print("\nErreur: Les dimensions des matrices ne sont pas compatibles.")
#         print("\nMatrice 1:")
#         my_prn(matrice1)
#
#         print("\nMatrice 2:")
#         my_prn(matrice2)
#         return None
#
#     lignes_matrice1 = len(matrice1)
#     colonnes_matrice2 = len(matrice2[0])
#
#     # Initialisation de la matrice résultante
#     resultat = [[0 for _ in range(colonnes_matrice2)] for _ in range(lignes_matrice1)]
#
#     # Multiplication des matrices
#     for i in range(lignes_matrice1):
#         for j in range(colonnes_matrice2):
#             for k in range(colonnes_matrice1):
#                 resultat[i][j] += matrice1[i][k] * matrice2[k][j]
#
#     return resultat
#
# print()
# my_prn(multiplier_matrices(m1, m2))
#
#
# #

################################## X/0
# n, m = 3, 3
# # a = [['.'] * m] * n
# a = [['.'] * m for i in range(n)]
#
# my_prn(a)
# print()
#
# a[0][1] = 'X'
# a[2][2] = 'O'
# a[1][0] = 'X'
# a[2][0] = 'O'
#
# my_prn(a)
# print()
# for row in a:
#     print(row, id(row))
# print()

############# with MAP !!!!!!!!!!!!
# a = [['.'] * 3 for i in range(3)]
#
# my_prn(a)
# print()
#
# # for i in range(5):
# i = 0
# while i < 5:
#     k, l = map(int, input('input coord = ').split()) # 1 2  ['1', '2']   1, 2
#
#
#     # if i % 2:
#     #     a[k][l] = 'X'
#     # else:
#     #     a[k][l] = '0'
#     if a[k-1][l-1] == '.':
#         a[k-1][l-1] = '0' if i % 2 else 'X'
#     else:
#         print('Error!')
#         i -= 1
#
#     print()
#     i += 1
#     my_prn(a)
# # ##############
# print()
# a[2][2] = 'X'
# a[2][1] = '0'
# a[0][1] = 'X'
# print()
# my_prn(a)
# print(a, type(a))
# print()
# a[1][1] = 'X'
# a[0][2] = '0'
# a[0][0] = '0'
# print(*a)
#
# for row in a:
#     print(*row)
#
# print()
# my_prn(a)



############# Ввод довільного масиву ######################
# n = int(input('Number of rows = '))
# a = []
# for i in range(n):
#     # row = list(map(int, input().split()))
#     row = input(f'Input {i+1} row of numbers with spaces : ').split()
#     a.append(row)
# my_prn(a)




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
########### Теж саме в один рядок ##############
# my_prn([[j for j in input(f'Input {i+1} row of numbers with spaces : ').split()] for i in range(int(input('input number of rows = ')))])


################# Задачі із ДЗ ###############
###############################################
# 1 0 0 0
# 2 1 0 0
# 2 2 1 0
# 2 2 2 1
###############################################




############ version 1(full)
# n = int(input('n = '))
# l1 = [['.'] * n for i in range(n)]
# my_prn(l1)
# print()
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             l1[i][j] = 0
#         elif i > j:
#             l1[i][j] = 2
#         else:
#             l1[i][j] = 1
# for row in l1:
#     print(*row)


############ version 2(short)

#
# n = int(input('n = '))
# l1 = [[0] * n for i in range(n)]
# my_prn(l1)
# for i in range(n):
#     for j in range(i):
#         l1[i][j] = 2
#     l1[i][i] = 1
# for row in l1:
#     print(*row)


############ version 3(analitic)


n = int(input('n = '))
l1 = [[2] * i + [1] + [0] * (n - 1 - i) for i in range(n)]
my_prn(l1)



#
# l1[2][2] = 8
# l1[2][3] = 77
# print()
# my_print(l1)
########################################
# 0 0 0 0 1
# 0 0 0 1 2
# 0 0 1 2 2       СПРОБУЄМ?
# 0 1 2 2 2
# 1 2 2 2 2

#################################################### KH-25-1 & KH-25-2


#
# n =5
# ########################################
# l1 = [[0] * (n - 1 - i) + [1] + [2] * i for i in range(n)]
###################################################

# n = int(input('n = '))
# l1 = [[0] * n for i in range(n)]
#
# for i in range(n):
#     for j in range(n-i, n):
#         l1[i][j] = 2
#     l1[i][n-1-i] = 1
# for row in l1:
#     print(*row)




# n = int(input('n = '))
# # l1 = [[2] * i + [1] + [0] * (n - 1 - i) for i in range(n)]
# l1 = [[0] * (n - 1 - i) + [1] + [2] * i for i in range(n)]
# my_prn(l1)


########################################

# 0 1 2 3 4
# 1 0 1 2 3
# 2 1 0 1 2
# 3 2 1 0 1
# 4 3 2 1 0
############################

# n = int(input('n = '))
# l1 = [[0] * n for i in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         # l1[i][n-1-j] = n - 1 - j - i
#         l1[i][n-1-j] = abs(n - 1 - j - i)
#
# my_prn(l1)





################# Таж задача ##################
# n = int(input('n = '))
# l1 = [[abs(j - i) for j in range(n)] for i in range(n)]
# # l1 = [[-(i - j) for j in range(n)] for i in range(n)]
# my_prn(l1)



########################################
# Pifagor's
#    1	2	3	4	5	6	7	8	9
#    2	4	6	8	10	12	14	16	18
#    3	6	9	12	15	18	21	24	27
#    4	8	12	16	20	24	28	32	36
#    5	10	15	20	25	30	35	40	45
#    6	12	18	24	30	36	42	48	54
#    7	14	21	28	35	42	49	56	63
#    8	16	24	32	40	48	56	64	72
#    9	18	27	36	45	54	63	72	81

######  СПРОБУЄМ!!!!!!????????????????????????????


# n = int(input('n = '))
# p = [[0] * n for i in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         p[i][j] = (i+1)*(j+1)
#
# my_prn(p)


#########
# p = [[i * j for j in range(1, n+1)] for i in range(1, n+1)]
# my_prn(p)
# print()
# n = 10
#
# my_prn([[i * j for j in range(1, n+1)] for i in range(1, n+1)])





# my_prn([[i * j for j in range(1, 11)] for i in range(1, 11)])


# my_prn([[i * j for j in range(1, int(input(f'n{i}='))+1)] for i in range(1, int(input('m='))+1)])


########################### END






############ Задача SWAP #################
# def swap_columns(a, i, j):
#     for k in range(len(a)):
#         a[k][j], a[k][i] = a[k][i], a[k][j]
        # a, b = b, a
#
# n = int(input('n = '))
# a = [0] * n
# max_ = 0
# for i in range(n):
#     a[i] = input("elements with space : ").split()
# my_print(a)
# i, j = list(map(int, input('i j = ').split()))
# swap_columns(a, i, j)
# my_print(a)



#########  То же с заполнением нулями   ##########
# n = int(input('n = '))
# a = [0] * n
# max_ = 0
# for i in range(n):
#     a[i] = input("elements with space : ").split()
#     if len(a[i]) > max_:
#         max_ = len(a[i])
# for i in range(n):
#     while len(a[i]) < max_:
#         a[i].append(0)
# my_print(a)
# i, j = list(map(int, input('i j = ').split()))
# swap_columns(a, i, j)
# my_print(a)