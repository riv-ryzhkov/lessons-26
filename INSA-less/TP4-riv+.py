#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:51:36 2021

@author: jrh & riv
"""

##################################################

from numpy import *
from numpy.linalg import *
from matplotlib.pyplot import *
import numpy as np

###################################################

M = [[1,2,3], [4,5,6]]
N = [[1,0], [2,1], [3,2]]


# print(*M, sep='\n')
# print()
# print(*N, sep='\n')
# print()


# print((M + N), sep='\n')

# print(N * M)

# print('='*40)

#################

# M = array(M)
# N = array(N)

# print(M)
# print(N)

# print(M + M)

# # print(M * N)

# # # print('.'*40)

# print(dot(M, N))
# print()

# print(dot(N, M))
# print('.'*40)

# ################################

# A = [[1, 2, 1], [1, 2, 1], [-1, -2, -1]]
# A = array(A)

# print(A)
# print()

# # print(A*3)
# # print()

# print(transpose(A))
# print()


# print(dot(A,dot(A,dot(A,A))))   # A*A*A*A
# print()

# print(matrix_power(A, 4))       # A^4


# ===================

# a0 = np.zeros(4)
# print(a0, type(a0))


# a1 = np.ones(4)
# print(a1, type(a1))


# a00 = np.zeros((4, 4))
# # print(a00, type(a00))


# a11 = np.ones((4, 4))
# # print(a11)

# ad0 = np.diag(a1)
# print(ad0)

# # ad1 = 2 * np.diag(a1)
# # print(ad1)

# ad0_ = np.diag(ad0)
# print(ad0_)


# ad1_ = np.diag(ad1)
# print(ad1_)


###################################


# n, p = 3, 4
# print(zeros((n, p)))
# print(ones((n, p)))


# a, b, c = 3, 4, 5
# print(diag([a ,b, c], -3))
# print(diag([a, b, c], 1))
# print(diag([a, b, c], -1))
# print(diag([a, b, c], 2))

# ==================================

###################################################



M1 = array([[5, 2], [2, 9]])
M2 = array([[1, 2, 1], [1, 2, 1], [-1, -2, -1]])
M3 = array([[5, 0, 8], [9, 7, 7], [14, 7, 15]])


# print(M1)
# print()
# print(M2)
# print()
# print(M3)




# # La première matrice

# result_det = np.linalg.det(M1)
# print('det(M1) =', result_det)
# print()
# M1_inv = inv(M1)
# print(M1_inv)
# print()
# print(dot(M1, M1_inv))  #Doit être approximativement la matrice identité
# print()




# # Deuxième matrice (en attendant une erreur)

# try:
#     result_det = np.linalg.det(M2)
#     print('det(M2) =', result_det)
#     print()
#     M2_inv = inv(M2)
# except:
#     print("La matrice M2 est irréversible.")
# print()




# La troisième matrice

# result_det = np.linalg.det(M3)
# print('det(M3) =', result_det)
# print()
# M3_inv = inv(M3)
# print(dot(M3, M3_inv))  # Vérification du résultat
# print()






######################################################
######   Exercice 1 : construction de matrices
######################################################

# def Matrice(n):
#     C = zeros((n, n))
#     for i in range(n):
#         C[i][n-1-i] = 1
#         # C[i, i] = 1
#     return C


# print(Matrice(5))











# print(eye(5))














# def Matrice(n):
#     C = zeros((n, n))
#     for i in range(n):
#         C[i][n-1-i] = 1
#     return C


# print(Matrice(5))

















# def Matrice(n):
#     C = zeros((n, n))
#     for i in range(n):
#         # C[i] = (i + 1) * ones((1, n))
#         C[i] = (i + 1) * ones(n)
#     return C


# print(Matrice(5))












# def Matrice(n):
#     C = zeros((n, n))
#     for i in range(n):
#             for j in range(n):
#                 C[i][j] = 1 + abs(i-j)
#     return C


# print(Matrice(5))













# def Matrice(n):
#     C = zeros((n, n))
#     for i in range(n):
#             for j in range(n):
#                 C[i][j] = n - abs(i-j)
#     return C


# print(Matrice(5))













# def Matrice(n):
#     d = [-2 for i in range(n)]
#     up = [1 for i in range(n-1)]
#     C = diag(d) + diag(up, 1) + diag(up, -1)
#     return C







# def Matrice(n):
#     d = -2 * ones(n)
#     up = ones(n-1)
#     C = diag(d) + diag(up, 1) + diag(up, -1)
#     return C

# print(Matrice(5))

















# #Resolution du systeme. 

# def Matrice(n):
#     d = [-2 for i in range(n)]
#     up = [1 for i in range(n-1)]
#     C = diag(d) + diag(up, 1) + diag(up, -1)
#     return C


# v = array([[1], [2], [3], [2], [1]])
# print(v)
# print()

# B = Matrice(5)
# print(B)

# sol = dot(inv(B), v)
# print(sol)


# print(solve(B, v))






#####################################################
####     Exercice 2 : décor 3D
#####################################################




# Commandes permettant d'avoir la même échelle en abscisse et en ordonnée
# et de contraindre le cadre de la figue.



# from numpy import *
# from numpy.linalg import *
# from matplotlib.pyplot import *


# axis("equal")
# xlim(-6, 6)
# ylim(-4, 4)

# # Les trois rectangles formés de 4 sommets + le premier qui est répété à la fin. 
# # D1 bleu
# D1 = [
#       [ 1.2, 3,-1], 
#       [-1.2, 3,-1], 
#       [-1.2, 3, 1], 
#       [ 1.2, 3, 1], 
#       [ 1.2, 3,-1]
#       ]
# # D2 rouge
# D2 = [
#       [-1, 1,-1], 
#       [-1, 2,-1],
#       [-1, 2, 1],
#       [-1, 1, 1],
#       [-1, 1,-1]
#       ]
# # D3 vert
# D3 = [
#       [1, 1,-1],
#       [1, 2,-1],
#       [1, 2, 1],
#       [1, 1, 1],
#       [1, 1,-1]
#       ]


# # # Les paramètres de translation et de rotation, à faire varier.
# a = 0   # bouger à gauche et à droite
# b = 0   # avancer et reculer
# t = 0    # tourner à l'horizon


# # La matrice de rotation d'angle t
# R = array([
#     [cos(t), -sin(t), 0],
#     [sin(t),  cos(t), 0],
#     [ 0,       0,     1]
#     ])


# # Fonction permettant de projeter un vecteur X sur le plan y=4.
# # Ne fonctionne que pour des vecteurs tels que y>0.
# def projection(X):
#     P = [0, 0, 0]
#     P[0] = X[0] * 4. / X[1]
#     P[1] = 4.
#     P[2] = X[2] * 4. / X[1]
#     return P



# # Fonction permettant de translater le décor. 
# # Pour décaler l'observateur de (a,b), on décale le décor de (-a,-b)
# def translation(X, a, b):
#     T = [0, 0, 0]
#     T[0] = X[0] - a
#     T[1] = X[1] - b
#     T[2] = X[2]
#     return T



# # Construction des images du rectangle D1 par les differentes transformations.
# # En commentaire : la simple projection, translation+projection, rotation+projection.    


# P1 = [0, 0, 0, 0, 0]
# for i in range(5):
#     P1[i] = translation(D1[i], a, b)
#     P1[i] = transpose(array([P1[i]]))
#     P1[i] = projection(dot(R, P1[i]))

# x1 = [P1[i][0] for i in range(5)]
# z1 = [P1[i][2] for i in range(5)]

# plot(x1, z1)
# fill(x1, z1)


# P2 = [0, 0, 0, 0, 0]
# for i in range(5):
#     P2[i] = translation(D2[i], a, b)
#     P2[i] = transpose(array([P2[i]]))
#     P2[i] = projection(dot(R, P2[i]))

# x2 = [P2[i][0] for i in range(5)]
# z2 = [P2[i][2] for i in range(5)]

# plot(x2, z2)
# fill(x2, z2)


# P3 = [0, 0, 0, 0, 0]
# for i in range(5):
#     P3[i] = translation(D3[i], a, b)
#     P3[i] = transpose(array([P3[i]]))
#     P3[i] = projection(dot(R, P3[i]))

# x3 = [P3[i][0] for i in range(5)]
# z3 = [P3[i][2] for i in range(5)]

# plot(x3, z3)
# fill(x3, z3)



###############################################################
## +++++++++++++++++++++++++++++++++++++++++++++

# from numpy import *
# from numpy.linalg import *
# from matplotlib.pyplot import *


# axis("equal")
# xlim(-6, 6)
# ylim(-4, 4)

# D1 = [
#       [ 1.2, 3,-1], 
#       [-1.2, 3,-1], 
#       [-1.2, 3, 1], 
#       [ 1.2, 3, 1], 
#       [ 1.2, 3,-1]
#       ]
# D2 = [
#       [-1, 1,-1], 
#       [-1, 2,-1],
#       [-1, 2, 1],
#       [-1, 1, 1],
#       [-1, 1,-1]
#       ]
# D3 = [
#       [1, 1,-1],
#       [1, 2,-1],
#       [1, 2, 1],
#       [1, 1, 1],
#       [1, 1,-1]
#       ]




# def projection(X):
#     P = [0, 0, 0]
#     P[0] = X[0] * 4. / X[1]
#     P[1] = 4.
#     P[2] = X[2] * 4. / X[1]
#     return P



# def translation(X, a, b):
#     T = [0, 0, 0]
#     T[0] = X[0] - a
#     T[1] = X[1] - b
#     T[2] = X[2]
#     return T



# def func(a, b, t):
    
#     R = array([
#         [cos(t), -sin(t), 0],
#         [sin(t),  cos(t), 0],
#         [ 0,       0,     1]
#         ])
    
#     P1 = [0, 0, 0, 0, 0]
#     for i in range(5):
#         P1[i] = translation(D1[i], a, b)
#         P1[i] = transpose(array([P1[i]]))
#         P1[i] = projection(dot(R, P1[i]))
    
#     x1 = [P1[i][0] for i in range(5)]
#     z1 = [P1[i][2] for i in range(5)]
    
#     plot(x1, z1)
#     fill(x1, z1)
    
    
#     P2 = [0, 0, 0, 0, 0]
#     for i in range(5):
#         P2[i] = translation(D2[i], a, b)
#         P2[i] = transpose(array([P2[i]]))
#         P2[i] = projection(dot(R, P2[i]))
    
#     x2 = [P2[i][0] for i in range(5)]
#     z2 = [P2[i][2] for i in range(5)]
    
#     plot(x2, z2)
#     fill(x2, z2)
    
    
#     P3 = [0, 0, 0, 0, 0]
#     for i in range(5):
#         P3[i] = translation(D3[i], a, b)
#         P3[i] = transpose(array([P3[i]]))
#         P3[i] = projection(dot(R, P3[i]))
    
#     x3 = [P3[i][0] for i in range(5)]
#     z3 = [P3[i][2] for i in range(5)]
    
#     plot(x3, z3)
#     fill(x3, z3)
#     show()

# move = 1
# while move:
#     move = input('a b t =')
#     a, b, t = move.split()
#     a = int(a)/10
#     b = int(b)/10
#     t = int(t)/10
#     func(a, b, t)