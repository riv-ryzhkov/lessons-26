# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:46:59 2025

@author: Igor Ryzhkov (INSA)
"""


from matplotlib.pyplot import *
from numpy import *
import numpy
import math

# print(*dir(numpy), sep='\n')


# a = [2, 4, 6, 2]
# b = [2, 4, 2, 2]
# plot(a,b)
# fill(a,b, color="red")


#
# a = [2, 2, 4, 4, 6, 4, 4, 2]
# b = [4, 6, 6, 7, 5, 3, 4, 4]
# plot(a,b)
# fill(a,b, color="C2")
# show()

# x = linspace(-2, 8, 100)
# print(x, type(x))
# y = sin(x)
# print(y, type(y))
#
# plot(x, y)
# # show()
#
# y1 = cos(2*x)
# z = zeros(100)
# z1 = ones(100)
#
# plot(x, y1)
# plot(x, z)
# plot(x, z1)
#
# show()

########################################################
# Exercice 1    Racine carrée de 2

####################################################################


# On trace le graphe de la fonction et on ajoute l'axe des abscisses.
# On localise ainsi la racine recerchée et on modifie ensutie les 
# bornes de x pour améliorer la précision. 

# x = linspace(-pi, pi, 100)
#
# # y = x**2 - 2
# y = 2*x**3-12*x**2+4*x-150
#
# # print(type(x), x)
# # # print(type(y), y)
#
# plot(x,y)
#
# z = 0 * x
# plot(x,z)
#
# show()
######################################################
#########################################
# # Exercice 1






#
# print(sqrt(2), '--> sqrt(2)')
#
# u = 2
# for i in range(20):
#     u = u + 4/3 - 2 * u**2 / 3
# print(u)


# a = 1
# b = 10**-15
# c = a + b
# print(c)
# print(2**(1/2))








# Modification pour construire la suite des premiers termes.
# v = 2
# sq = sqrt(v)
#
# l = [2]
# x = [sq]
# for i in range(150):
#     v = v + 4/3 - 2 * v**2 / 3
#     print(f'Iteration {i+1} = {v}')
#     l.append(v)
#     x.append(sq)
#
# print('\nResultat  =', l[-1])
# print('Diference =', v - 2**(1/2))
# print()
#
#
# print(2**(1/2))
# plot(l)
# plot(x)
# show()

###################### La convergence 
#
# v = 2
# sq = sqrt(v)
# n = 50
# l = [2]
# x = [sq]
# y = []
# err = []
# for i in range(n):
#     v = v + 4/3 - 2 * v**2 / 3
#     l.append(v)
#     x.append(sq)
#     err.append(abs(v - sq))
#     y.append(-0.122 * i -1)                   # 0.122
#
#
# # plot(err)
#
# plot(log(err))
# plot(y)
#
# show()

######################




# Calcul de la suite jusqu'à obtention du critère |u**2-2|<2epsislon
# On ajoute un compteur n pour savoir quand la précision est atteinte.
# eps = 1e-15
# sq = sqrt(2)
# w = 2
# n = 0
# l1 = [2]   #   riv
# while abs(w**2-2) >= 2*eps:
#
#     w = w + 4/3 -2 * w**2 / 3
#     n = n + 1
#     l1.append(w)   #   riv
# print(w, n)
# print(sq)
#
# plot(l1)   #   riv
#
# show()



# # # Même travail avec l'autre suite.

# eps = 1e-5
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
#
# show()

# On a obtenu n=184 dans le premier cas et m=4 dans le second. 
# La seconde sutie converge bien plus vite vers racine de 2.
    

###############################################
# Exercice 2 
# Calcul de la dérivée numérique d'une fonction





# x = linspace(-pi, pi, 100)  # Crée 100 points répartis entre -2 et 2

# y = 2*cos(2*x)+sin(3*x)
# y = cos(x)

# plot(y)
# show()

# d = []
# for i in range(99):
#     d.append((y[i+1]-y[i])/(x[i+1]-x[i]))
#
# plot(d)
# show()
  









# dy_dx = (y[1:]-y[:-1])/(x[1:]-x[:-1])      # Calcul de la dérivée
#
# plot(dy_dx, label="Dérivée numérique")
#
# plot(-sin(x), '+', label="Dérivée exacte (-sin(x))")
# legend()
# show()


# x = [i/50 for i in range(0,100)]
# print(x, type(x))
# y = list(map(math.sin, x))
# print(y, type(y))


x = linspace(0, 2, 100)
y = sin(x)

