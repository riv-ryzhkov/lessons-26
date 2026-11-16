# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:53:05 2025

@author: 1
"""

########################################################
# Exercice 1    Calcul d'intégrale avec la méthode des rectangles

import numpy as np
import matplotlib.pyplot as plt



def f(x):
    y = np.exp(x)
    # y = np.cos(x)
    # y = x**2
    return y

# # # # ...........
# # x = np.linspace(-0.5, 1.5)
# # plt.plot(x, f(x))
# # plt.show()

# # # # ....................

# exacte = np.e - 1                      #  exp(x)
# # exacte = np.sin(1)                   #  cos(x)
# # exacte = 1 / 3                          # x^2

# a, b = 0, 1
# n = 30


# # #########################################


# def rect_g(a, b, n, f):
#     dx = (b - a) / n
#     result = 0
#     for i in range(n):
#         x = a + i * dx
#         result += f(x) * dx
#     return result


# # # Paramètres


# # Calcul
# gauche = rect_g(a, b, n, f)



# # Résultats
# print(f"Nombre d'iterations             \t: {n}")
# print(f"Valeur exacte                   \t: {exacte}")
# print(f"Méthode des rectangles à gauche \t: {gauche}")



# # ..................................................


# def rect_d(a, b, n, f):
#     dx = (b - a) / n
#     result = 0
#     for i in range(n):
#         x = a + (i+1) * dx
#         result += f(x) * dx
#     return result



# # # Calcul
# droite = rect_d(a, b, n, f)


# # Résultats
# print(f"Méthode des rectangles à droite \t: {droite}")


# # ..................................................



# def rect_PMil(a, b, n, f):
#     dx = (b - a) / n
#     result = 0
#     for i in range(n):
#         x = a + (i+0.5) * dx
#         result += f(x) * dx
#     return result


# Exemple d'utilisation


# # Calcul
# point_m = rect_PMil(a, b, n, f)


# # Résultats
# print(f"Méthode des rect. des points milieux: {point_m}")



# ########################################################

# # Exercice 2    Calcul d'intégrale avec la méthode des trapèzes



# def trapez(a, b, n, f):
#     """
#     Méthode des trapèzes pour calculer une intégrale définie.

#     Paramètres :
#     - f : fonction à intégrer,
#     - a : borne inférieure,
#     - b : borne supérieure,
#     - n : nombre de sous-intervalles.

#     Retourne :
#     - La valeur approximative de l'intégrale.
#     """
    
    # dx = (b - a) / n  # Largeur des sous-intervalles
    # result = (f(a) + f(b))/2  # Termes aux bornes

    # for i in range(1, n):
    #     x = a + i * dx
    #     result += f(x)

    # return result * dx

# Exemple d'utilisation



# Calcul de l'intégrale
# trap = trapez(a, b, n, f)

# print(f"Méthode des trapèzes   \t\t\t: {trap}")



# # # # # #### Méthode de Simpson ####


# def Simps(a, b, n, f):
    
#     dx = (b-a)/n
#     res = f(a) + f(b) + 4 * f(a+dx/2)
#     for i in range(1, n):
#         res = res + 2*f(a+i*dx) + 4*f(a+i*dx+dx/2)
#     res = res * (dx/6)
#     return res


# print('Méthode de Simpson \t\t\t\t:', Simps(a, b, n, f))


################## 
# # # #### Les Erreurs et la Vitesse de convergence :

############ Les Erreurs

# err_Rect = np.zeros(n)
# err_Trapz = np.zeros(n)
# err_Simps = np.zeros(n)

# print(np.zeros(5))



# for i in range(n):
#     err_Rect[i] = np.abs(rect_g(a, b, i+1, f) - exacte)
#     err_Trapz[i] = np.abs(trapez(a, b, i+1, f) - exacte)
#     err_Simps[i] = np.abs(Simps(a, b, i+1, f) - exacte)
 
    
 
# x=[k+1 for k in range(n)]
# plt.plot(x, err_Rect, color='blue')
# plt.plot(x, err_Trapz, color='green')
# plt.plot(x, err_Simps, color='black')

# plt.title("Les Erreurs")
# plt.show()



# ############## Vitesse de convergence

# plt.plot(np.log(x), np.log(err_Rect), color='blue')
# plt.plot(np.log(x), -1*np.log(x), '+', color='b')

# plt.plot(np.log(x), np.log(err_Trapz), color='green')
# plt.plot(np.log(x), -2*np.log(x), '+', color='g')

# plt.plot(np.log(x), np.log(err_Simps), color='black')
# plt.plot(np.log(x), -4*np.log(x), '+', color='black')

# plt.title("Vitesse de convergence")
# plt.show()

