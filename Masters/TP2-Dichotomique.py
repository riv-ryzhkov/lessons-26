# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 18:51:22 2025

@author: Igor Ryzhkov (INSA)
"""
from matplotlib.pyplot import *
from numpy import *


########################################################

# Graph


#
# x = linspace(1, 3, 100)
# # y = x**2 - 2
# y = x**3 - 2*x - 5
# # y = sin(x)-x/2
#
#
# print(type(x), x)
# print(type(y), y)
#
# plot(x,y)
#
# z = 0*x
# plot(x,z)
# show()
##############################################


#
# def f(x):
#     # Définir ici la fonction f(x)
#     # return x**2 - 2
#     return x**3 - 2*x - 5
#     # return 2*cos(x)-sin(2*x)-1



# def my_iteration(f, a, b, eps):
#     if f(a) * f(b) >= 0:
#         raise ValueError("La condition f(a) * f(b) < 0 n'est pas respectée.")
#
#     x = a
#     n = 0
#     while f(x) * f(x+eps) > 0 and x <= b:
#         x += eps
#         n += 1
#
#         w1 = [x, x]
#         w2 = [0, -6]
#         plot(w1, w2)
#
#     return x, f(x), n


#
#
# # # Test de la fonction
# a, b = 0, 3
# eps = 1e-3
#
# solution, res, nombre = my_iteration(f, a, b, eps)
# print(f"Solution approchée : {solution}")
# print(f'Fonction f(x) : {res}')
# print(f"Nombre d'itérations : {nombre}")
#
# xx = linspace(a, b, int((b-a)/eps))
#
# yy = f(xx)
#
# plot(xx, yy)
#
# zz = 0 * xx
# plot(xx,zz)
#
# show()


# #######################################################
# # Exercice 1    Résolution d'équation f(x)=0. Méthode dichotomie.
#
# def f(x):
#     # return x**2 - 2
#     return x**3 - 2*x - 5
#     # return 2*cos(x)-sin(2*x)-1
#
#
# def dichotomie(f, a, b, eps):
#
#     if f(a) * f(b) >= 0:
#         raise ValueError("La condition f(a) * f(b) < 0 n'est pas respectée.")
#
#     iteration = 0
#     while abs(b - a) > eps:
#         iteration += 1
#         m = (a + b) / 2
#         if f(m) == 0:  # Solution exacte trouvée
#             return m, iteration
#         elif f(a) * f(m) < 0:
#             b = m
#         else:
#             a = m
#
#         w1 = [m, m]
#         w2 = [0, -6]
#         plot(w1, w2)
#
#     return (a + b) / 2, f(m), iteration
#
#
#
#
# # Test de la fonction
# a, b = 0, 3
# eps = 1e-1
# solution, res, iterations = dichotomie(f, a, b, eps)
# print(f"Solution approchée : {solution}")
# print(f'Fonction f(x) : {res}')
# print(f"Nombre d'itérations : {iterations}")
#
#
# xx = linspace(a, b, int((b-a)/eps))
# yy = f(xx)
# plot(xx, yy)
#
# zz = 0 * xx
# plot(xx,zz)
#
# show()
# ###########################################################
# ###################################

# # Exercice 2        Les Matrices.

# M=[[1,2,3,4],[5,6,7,8]]
#
# N=[[9,1,8,2],[7,3,6,4]]
#
#
# # # print(M)
# # print("len(M)=", len(M))
# # print("len(M[0])=", len(M[0]))
# # print()
# print(*M, sep='\n')
# print()
# print(*N, sep='\n')
# print()





# Somme de deux matrices
##################### riv
# S=[]
# for i in range(len(M)):
#     S.append([])
#     for j in range(len(M[0])):
#         S[i].append(M[i][j]+N[i][j])
    



# S = [[M[i][j]+N[i][j] for j in range(len(M[0]))] for i in range(len(M))]
#
# print(*S, sep='\n')



###################################### 2 list

# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [9, 0, 1, 2, 8], [3, 4, 8, 9, 0]]

# # # # ##########################################
# print('len =', len(a))
# print('a =', a)
# print()


# print(*a, sep='\n')
# print()


# print('a[0] =', a[0], type(a[0]))
# print('a[2][1:3] =', a[2][1:3])
# print('a[0][1] =', a[0][1])
# print('a[1][1:3] =', a[1][1:3])





#######################################

# n, m = 3, 4

# # a = [[0] * m] * n # ---------------------
# a = [[0] * m for i in range(n)] # ++++++++
# print(*a, sep='\n')


# a[0][0] = 9
# a[2][1] = 8
# print()
# print(*a, sep='\n')


####################################################################


from random import randint


def rand_mat(n, m):
    matrice = []
    for i in range(n):
        matrice.append([randint(0, 9) for j in range(m)])
    return matrice


def afficher_matrice(matrice):
    for ligne in matrice:
        print(*ligne, sep='\t')


afficher_matrice(rand_mat(5, 4))





def multiplier_matrices(matrice1, matrice2):
    """
    Multiplie deux matrices.

    Paramètres:
        matrice1: Première matrice (liste de listes).
        matrice2: Deuxième matrice (liste de listes).

    Retourne:
        Le produit des matrices (liste de listes) ou None si les dimensions ne sont pas compatibles.
    """

    # Vérification des dimensions
    colonnes_matrice1 = len(matrice1[0])
    lignes_matrice2 = len(matrice2)


    if colonnes_matrice1 != lignes_matrice2:
        print("\nErreur: Les dimensions des matrices ne sont pas compatibles.")
        print("\nMatrice 1:")
        afficher_matrice(matrice1)

        print("\nMatrice 2:")
        afficher_matrice(matrice2)
        return None

    lignes_matrice1 = len(matrice1)
    colonnes_matrice2 = len(matrice2[0])

    # Initialisation de la matrice résultante
    resultat = [[0 for _ in range(colonnes_matrice2)] for _ in range(lignes_matrice1)]

    # Multiplication des matrices
    for i in range(lignes_matrice1):
        for j in range(colonnes_matrice2):
            for k in range(colonnes_matrice1):
                resultat[i][j] += matrice1[i][k] * matrice2[k][j]

    return resultat



# Exemples de matrices
matrice1 = [[1, 2], [3, 4]]
matrice2 = [[5, 6], [7, 8]]

afficher_matrice(matrice1)
print()
afficher_matrice(matrice2)

matrice1 = rand_mat(2, 3)
matrice2 = rand_mat(3, 4)

print()
afficher_matrice(matrice1)
print()
afficher_matrice(matrice2)

# Multiplication et affichage
resultat = multiplier_matrices(matrice1, matrice2)


 # Exemple avec des dimensions non compatibles
matrice1 = [[1, 2], [4, 5]]
matrice2 = [[7, 8, 5], [9, 10, 8]]

resultat = multiplier_matrices(matrice1, matrice2)



if resultat is not None:
    print("Matrice 1:")
    afficher_matrice(matrice1)

    print("\nMatrice 2:")
    afficher_matrice(matrice2)

    print("\nRésultat de la multiplication:")
    afficher_matrice(resultat)
    print('-'*40)
    



