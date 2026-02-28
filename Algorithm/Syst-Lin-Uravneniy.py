# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 23:11:04 2025

@author: jrh & riv
"""

import numpy as np
import math
import random


# # Résolution d'un système d'équations linéaires Ax = b
# # où A est une matrice triangulaire inférieure.


def matrice(n):
    M = [[0] * n for i in range(n)]
    for i in range(n): # ligne
        for j in range(i+1):  # colonne
            M[i][j] = int(input(f"A[{i}][{j}]="))
            # M[i][j] = random.randint(1, 9)
    return M


# A = matrice(3)
#
# print(*A, sep='\n')


def vector(n):
    V = []
    for i in range(n):
        V.append(int(input(f"b[{i}]=")))
    return V


def afficher_matrice(matrice):
    print()
    for ligne in matrice:
        print(ligne)

# # n = 4
# # A = matrice(n)
# # afficher_matrice(A)
# #
# # print()
# # print(*A, sep='\n')
#
#
# def resolution(A, b):
#     """
#     Résout le système Ax = b par la méthode de substitution avant.
#
#     Paramètres :
#     - A : liste de listes (matrice triangulaire inférieure)
#     - b : liste (vecteur colonne)
#
#     Retourne :
#     - x : liste (solution du système)
#     """
#     n = len(b)  # Taille du système
#     x = [0] * n  # Initialisation du vecteur solution avec des zéros
#
#     # Parcours des lignes de la matrice
#     for i in range(n):
#         # Vérification que le coefficient diagonal n'est pas nul
#         if A[i][i] == 0:
#             raise ValueError(f"Le coefficient diagonal A[{i}][{i}] est nul, résolution impossible.")
#
#         # Calcul de x[i] en utilisant la formule de substitution avant
#         somme = 0
#         for j in range(i):  # Somme des termes connus
#             somme += A[i][j] * x[j]
#
#         # Formule de substitution avant
#         x[i] = (b[i] - somme) / A[i][i]
#
#     return x
#
#
# # # # Exemple d'utilisation
#
# n = int(input("taille du système d'équations = "))
#
# A = matrice(n)
# b = vector(n)
# afficher_matrice(A)
# afficher_matrice(b)
#
#
# # Résolution du système
# try:
#     solution = resolution(A, b)
#     print("\nLa solution du système est :")
#     afficher_matrice(solution)
# except ValueError as e:
#     print("Erreur :", e)
#
#
# #  # Verification !!!!!!!!!!!!!!!!!!
# print('='*40)
# for i in range(n):
#     s = 0
#     for j in range(n):
#         s += A[i][j]*solution[j]
#     print(f'test de ligne {i}', s, '=', b[i], math.isclose(s, b[i]))
#

#####################################################
# Méthode avec NumPy


def solve_linear_system(A, B):
    """
    Résout un système linéaire A * X = B.

    Paramètres :
    - A : matrice des coefficients (numpy array).
    - B : vecteur des constantes (numpy array).

    Retourne :
    - X : vecteur solution.
    """
    try:
        X = np.linalg.solve(A, B)
        return X
    except np.linalg.LinAlgError:
        return "Le système n'a pas de solution unique (matrice singulière)."


# Exemple d'utilisation
if __name__ == "__main__":
    # Définir la matrice A et le vecteur B

    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]])

    b = np.array([8, -11, -3])

    # Résolution
    solution = solve_linear_system(A, b)

    afficher_matrice(A)
    afficher_matrice(b)
    print('.'*40)
    print("Solutions :", solution)


 #  Verification !!!!!!!!!!!!!!!!!!

    n = len(b)
    print('='*40)
    for i in range(n):
        s = 0
        for j in range(n):
            s += A[i][j]*solution[j]

        print(f'test de ligne {i}    {round(s)}\t= {b[i]} \t{round(s) == b[i]}')





