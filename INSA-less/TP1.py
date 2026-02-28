
# a = 1.1234567890123456789012
# print(a)
#
# a = 1+1e-16
# print(a)
#
# print(a-1)
#
# b = 1+1e-15
# # b = 1+1e-16
# print(b)
# print(b-1)

###################################

# from math import *
#
#
# print(sin(1))
# print(cos(pi))
# print(e)
# print(exp(1))
# print(exp(3))
#
# # !!!!!!!!!!!!!!!!
# # print(e**3)
# # print(exp(3))
# # print(exp(3)-e**3)


##################################
# from math import *
#
# tolerance = 1e-14
# print(exp(3)-e**3)
#
# if abs(exp(3) - e**3) <= tolerance:
#     print("Pratiquement égaux")
# else:
#     print("Différents")
#
#
#
# # print(isclose(exp(3), e**3))                #  1е-9
# # print(isclose(exp(3), e**3, rel_tol=1e-16))


# ###################### GRAPH & NUMPY
from matplotlib.pyplot import *
from numpy import *


# a = [2,4,6,2]
# b = [2,4,2,2]
# plot(a,b)
# fill(a,b, color="red") # red, green. blue, ...
# show()

# ........................................

# a = [2,2,4,4,6,4,4,2]
# b = [4,6,6,7,5,3,4,4]
# plot(a,b)
# fill(a,b, color="C0")  # C0-9
# # fill(a,b, color=(0.1, 0.2, 0.5, 0.9))  # RGBA
# # fill(a,b, color="#FF0000")  # HEX RGB
# show()


#
# x = linspace(0, 2*pi)
# # x = linspace(0, 2*pi, 75)
# print(len(x))
# print(type(x))
#
# # print(x)
#
#
# y = cos(2*x) - sin(x/2)
# print(len(y))
# print(type(y))
#
# # print(y)
#
#
# plot(x, y)
# show()

########################################
# Exercice Graf 2

# On trace le graphe de la fonction et on ajoute l'axe des abscisses.
# On localise ainsi la racine recerchée et on modifie ensutie les
# bornes de x pour améliorer la précision.
#
# x = linspace(1, 2, 100)
# y = x**2 - 2
#
# # print(type(x), x)
# # print(type(y), y)
#
# plot(x,y)
#
# z = 0*x
# plot(x,z)
# show()


###################################

# Exercice M+N (classique)

# M = [[1,2,3,4],[5,6,7,8]]
# N = [[9,1,8,2],[7,3,6,4]]


# print(M)
# print("len(M)=", len(M))
# print("len(M[0])=", len(M[0]))
# print()
#
# print(*M, sep='\n')
# print()
# print(*N, sep='\n')
# print()

# # Somme de deux matrices M+N

# S = []
# for i in range(len(M)):
#     S.append([])
#     for j in range(len(M[0])):
#         S[i].append(M[i][j]+N[i][j])
#
# print(*S, sep='\n')


# # S = [[M[i][j]+N[i][j] for j in range(len(M[0]))] for i in range(len(M))]
#

# # print(*S, sep='\n')


# (cont. TP4-riv+)
####################################################################












##################### riv
# print(2>3)
# print(2<3)
# y = 2 > 3
# print(y)

# # print(pi)

# ################## riv 

# x = linspace(0, 4, 100)
# y = (x<2)*2 + (x>=2)*4 + (x>=3)*(-1)
# plot(x,y)
############################################


# x = linspace(0.000001,3,100)

# # y = (x>1)*(1/x)
# y = (x<1)*(1+sin(pi*x)/pi) + (x>=1)*(1/x)


# plot(x,y)

# On constate que la fonction est au moins de classe C1, 
# le recollement en 1 est continu et semble dérivable.




###################################

# Exercice 3

# x = linspace(-pi, pi, 100)
# y = cos(x)
# y = exp(x)
# y = sin(x)+cos(2*x)

# On calcule les taux d'accroissement du vecteur Y.
# Ce vecteur est de taille 100 mais nous ne pourrons calculer que 99 
# taux d'accroissements. C'est pourquoi on extrait de Y les 99 premiers
# éléments et les 99 derniers.




########### riv

# d = []
# for i in range(99):
#     d.append((y[i+1]-y[i])/(x[i+1]-x[i]))

# plot(d)

#####################

# derivee = (y[1:100]-y[0:99])/(x[1:100]-x[0:99])

# z = -sin(x)

# plot(x[0:99],derivee)
# plot(x[0:99], z[0:99])

# plot(d)
# On reconnaît le graphe de -sin entre -2 et 2









