#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:51:36 2021

@author: jrh & riv
"""

from matplotlib.pyplot import *
from numpy import *
from time import sleep


#################    if    random()
from random import *



# r = random()
# print(r)
# if r < 1/3:
#     print('pierre')
# elif r < 2/3:
#     print('feuille')
# else:
#     print('ciseaux')

# #####################   for 
# n = 0
# L = [4, 9, 2, 7]
# for i in L:
#     # n = n + i
#     n += i
# print(n)




# mot=''
# for lettre in 'bonjour':
#     mot=lettre+mot
# print(mot)



# for i in range(5, 15, 2):

#     print(i, end=' ')




# n = int(input('n = '))
# fact = 1
# for k in range(1, n+1):
#     fact = fact * k
#     # fact *= k
#     print(k, '! =', fact)
# print(n, '! =', fact)


########################     while
############ password ####################################

# import time


# password = "123"
# user_input = ""
# n = 3
# attempts = n
# while user_input != password:
#     user_input = input("Entrez le mot de passe : ")
#     attempts -= 1
#     if attempts <= 0:
#         attempts = n
#         print('Attendez...')
#         time.sleep(5)

# print("L'accès est ouvert.")

###############################
# a = 321
# b = 43
# q = 0
# r = a-b*q
# while r >= b:
#     q += 1
#     r = a-b*q
# print(q)
# print(r)




# print(a//b)
# print(a%b)









#########################################
# Exercice 1

# print(sqrt(2), '--> sqrt(2)')

# u = 2
# for i in range(20):
#     u = u + 4/3 - 2 * u**2 / 3
# print(u)




# # Modification pour construire la suite des premiers termes.
# v = 2
# sq = sqrt(v)

# L = [2]
# X = [sq]
# for i in range(50):
#     v = v + 4/3 - 2*v**2 / 3
#     L.append(v)
#     X.append(sq)
    
# print('L[-1] =\t ', L[-1])

# print('sqrt(2) =', sqrt(2))
# plot(L) 
# plot(X)

######################
# Calcul de la suite jusqu'à obtention du critère |u**2-2|<2epsislon
# On ajoute un compteur n pour savoir quand la précision est atteinte.
# eps = 1e-15
# w = 2
# n = 0
# L1 = [2]   #   riv
# while abs(w**2-2) > 2*eps:
#     w = w + 4/3 - 2*w**2 / 3
#     n += 1
#     L1.append(w)   #   riv
# print('res =\t\t', w, n) 
# print('sqrt(2) =\t', sqrt(2))
# plot(L1)   #   riv
                   



# # Même travail avec l'autre suite.

# eps = 1e-15
# x = 2
# m = 0   
# L2 = [2]   #   riv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
# while abs(x**2-2) > 2*eps:
#     x = x/2 + 1/x
#     m += 1
#     L2.append(x)   #   riv

# print('res =\t\t', x, m)
# print('sqrt(2) =\t', sqrt(2))
# plot(L2)   #   riv

# On a obtenu n=184 dans le premier cas et m=4 dans le second. 
# La seconde sutie converge bien plus vite vers racine de 2.
    


########################################
# Exercice 2

# U = 0.1
# L1 = [U]
# for i in range(100):
#     if U < 1/3:
#         U = 3*U
#     elif U < 2/3:
#         U = 3*U-1
#     else:
#         U = 3*U-2
#     L1.append(U)

# # plot(L1)



# U = 0.1 + 1e-10
# L2 = [U]
# for i in range(100):
#     if U < 1/3:
#         U = 3*U
#     elif U < 2/3:
#         U = 3*U-1
#     else:
#         U = 3*U-2
#     L2.append(U)

# plot(L2)


###################### riv
# differences = [u1 - u2 for u1, u2 in zip(L1, L2)]
# differences = [abs(u1 - u2) for u1, u2 in zip(L1, L2)]
# plot(differences)



# On observe que les deux graphes sont quasi identiques au début
# puis deviennent très différents.
# Ainsi le petit écart initial entre les deux valeurs de u0 provoque
# au bout d'un certain nombre de termes de grandes différences entre
# les deux suites.



#########################################
# Exercice 3
    
# La programmation de la sutie est analogue à ce qui a été fait avant.
# On observe qu'en fonction de a, le comportement de la suite varie.
# Elle peut converger, ou osciller asymptotiquement entre plusieurs valeurs.
# Le code ci-dessous permet de faire varier a et de représenter pour chaque valeur
# les valeurs limites (approchées) de la suite. 
# On observe un phénomène de bifurcation : à partir de certains seuil,
# le comprotement change. On passe d'une valeur limite à 2 puis à 4, etc.
# C'est le diagramme de Feigenbaum.    


#############   1)
# liste = []
# n = 50
# a = 3.5   # 2.5  3  3.5  4
# u = 0.5
# for k in range(n):
#     u = a * u * (1 - u)
#     liste.append(u)

# plot(liste)



#################   2)  et   3)
# liste = []
# n = 51
# # for i in range(0, 300):
# for i in range(0, 400):
#     a = i / 100
#     x = 0.5
#     for k in range(n):
#         x = a * x * (1 - x)
#     liste.append(x)
# plot(liste)




#################   4)
liste = []
# liste_a = []
# a = 0
# x = 0

# n = 100
# eps = 0.01

# while (x <= eps):
#     x = 0.5
#     for k in range(n):
#         x = a * x * (1 - x)

#     liste_a.append(a)
#     liste.append(x)
#     a += 0.01
    
# a -= 0.02
# print('a=', a)
# plot(liste_a, liste)
# plot(liste_a, [eps]*len(liste))
# plot([a, a], [0, eps])





#################   5)

# a = 0
# step = 0.01
# x = 0
# liste = [x, x]
# liste_a = [a, a]
# n = 100
# eps = 0.01

# while (abs(liste[-1]-liste[-2])<=eps and a<4):
#     x = 0.5
#     for k in range(n):
#         x = a * x * (1 - x)

#     liste_a.append(a)
#     liste.append(x)
#     a += step
# a -= 2*step
# print('a=', a)
# plot(liste_a, liste)
# plot(liste_a, [liste[-1] for i in range(len(liste_a))])
# plot(liste_a, [liste[-2] for i in range(len(liste_a))])
# plot([a, a], [0, liste[-1]])




# #############################     6)

    
liste = []
n = 100
for k in range(400):
    a = k/100
    v = 0.5
    liste.append([])
    for i in range(n):
        v = a*v*(1-v)
        liste[k].append(v)
for j in range(16):
    limites = [liste[k][100-j-1] for k in range(400)] 
    title('limite #'+str(100-j)+' for a [0...4]', fontsize=16)  #  riv срезы последних 16 значений (точек схождения) в зависимости от а.
    plot(linspace(0,4,400),limites)
    input('=')    # riv
    sleep(0.5)    # riv
    show()       # riv

    
    
