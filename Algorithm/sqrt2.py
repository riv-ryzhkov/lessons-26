# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:46:59 2025

@author: Igor Ryzhkov (INSA)
"""

from matplotlib.pyplot import *
from numpy import *

# a = [2, 4, 6, 2]
# b = [2, 4, 2, 2]
# plot(a,b)
# fill(a,b, color="green")


# a = [2, 2, 4, 4, 6, 4, 4, 2]
# b = [4, 6, 6, 7, 5, 3, 4, 4]
# plot(a,b)
# fill(a,b, color="C5")


# x = linspace(-pi, pi, 100)
# print(type(x), x)
# y = sin(x)
# print(type(y), y)
# plot(x, y)


########################################################
# Exercice 1    Racine carrée de 2

####################################################################


# On trace le graphe de la fonction et on ajoute l'axe des abscisses.
# On localise ainsi la racine recerchée et on modifie ensutie les
# bornes de x pour améliorer la précision.

# x = linspace(1.4142125, 1.414215, 100)
#
# y = x**2-2
#
# # print(type(x), x)
# # print(type(y), y)
#
# plot(x,y)
#
# z = 0 * x
# plot(x,z)


######################################################


# print(sqrt(2), '--> sqrt(2)')
#
# u = 2
# for i in range(150):
#     u = u + 4/3 - 2 * u**2 / 3
# print(u)
#
#
# # Modification pour construire la suite des premiers termes.
# v = 2
# sq = sqrt(v)
#
# l = [2]
# x = [sq]
# for i in range(150):
#     v = v + 4/3 - 2 * v**2 / 3
#     l.append(v)
#     x.append(sq)

# print(l[-1])


# print(2**(1/2))
# print(sqrt(2))
# plot(l)
# plot(x)

######################


# Calcul de la suite jusqu'à obtention du critère |u**2-2|<2epsislon
# On ajoute un compteur n pour savoir quand la précision est atteinte.
# eps = 1e-15
# sq = sqrt(2)
# w = 2
# n = 0
# l1 = [2]   #   riv
# # for n in range(100000):
# while abs(w**2-2) > 2*eps:
#     # if abs(w**2-2) < 2*eps:
#         # break
#     w = w + 4/3 -2 * w**2 / 3
#     n = n + 1
#     l1.append(w)   #   riv
# print(w, n)
# print(sq)
#
# plot(l1)   #   riv


# # Même travail avec l'autre suite.

# eps = 1e-15
# sq = sqrt(2)
# x = 2
# m = 0
# l2 = [2]   #   riv
# while abs(x**2-2) > 2*eps:
#     x = x/2 + 1/x
#     # x = x + 4/3 - 2 * x**2 / 3
#     m = m + 1
#     l2.append(x)   #   riv
#
# print(x, m)
# print(sq)
# plot(l2)   #   riv

# On a obtenu n=184 dans le premier cas et m=4 dans le second.
# La seconde sutie converge bien plus vite vers racine de 2.


###############################################

# Exercice 2
# Calcul de la dérivée numérique d'une fonction


# x = linspace(-pi, pi, 100)  # Crée 100 points répartis entre -2 et 2
#
# y = cos(x)


# d = []
# for i in range(99):
#     d.append((y[i+1]-y[i])/(x[i+1]-x[i]))
#
# plot(x[:99], d)


# dy_dx = (y[1:]-y[:-1])/(x[1:]-x[:-1]) # Calcul de la dérivée
#
# plot(x[:-1], dy_dx, label="Dérivée numérique")
# plot(x, -sin(x), '+', label="Dérivée exacte (-sin(x))")
# legend()
#
# show()

