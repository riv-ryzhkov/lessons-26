
#####################################################
####     Exercice : décor 3D
#####################################################




# Commandes permettant d'avoir la même échelle en abscisse et en ordonnée
# et de contraindre le cadre de la figue.


#
# from numpy import *
# from numpy.linalg import *
# from matplotlib.pyplot import *
#
#
# axis("equal")
# xlim(-6, 6)
# ylim(-4, 4)
#
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
#
#
# # # Les paramètres de translation et de rotation, à faire varier.
# a = 0   # bouger à gauche et à droite
# b = 0   # avancer et reculer
# t = 0    # tourner à l'horizon
#
#
# # La matrice de rotation d'angle t
# R = array([
#     [cos(t), -sin(t), 0],
#     [sin(t),  cos(t), 0],
#     [ 0,       0,     1]
#     ])
#
#
# # Fonction permettant de projeter un vecteur X sur le plan y=4.
# # Ne fonctionne que pour des vecteurs tels que y>0.
# def projection(X):
#     P = [0, 0, 0]
#     P[0] = X[0] * 4. / X[1]
#     P[1] = 4.
#     P[2] = X[2] * 4. / X[1]
#     return P
#
#
#
# # Fonction permettant de translater le décor.
# # Pour décaler l'observateur de (a,b), on décale le décor de (-a,-b)
# def translation(X, a, b):
#     T = [0, 0, 0]
#     T[0] = X[0] - a
#     T[1] = X[1] - b
#     T[2] = X[2]
#     return T
#
#
#
# # Construction des images du rectangle D1 par les differentes transformations.
# # En commentaire : la simple projection, translation+projection, rotation+projection.
#
#
# P1 = [0, 0, 0, 0, 0]
# for i in range(5):
#     P1[i] = translation(D1[i], a, b)
#     P1[i] = transpose(array([P1[i]]))
#     P1[i] = projection(dot(R, P1[i]))
#
# x1 = [P1[i][0] for i in range(5)]
# z1 = [P1[i][2] for i in range(5)]
#
# plot(x1, z1)
# fill(x1, z1)
#
#
# P2 = [0, 0, 0, 0, 0]
# for i in range(5):
#     P2[i] = translation(D2[i], a, b)
#     P2[i] = transpose(array([P2[i]]))
#     P2[i] = projection(dot(R, P2[i]))
#
# x2 = [P2[i][0] for i in range(5)]
# z2 = [P2[i][2] for i in range(5)]
#
# plot(x2, z2)
# fill(x2, z2)
#
#
# P3 = [0, 0, 0, 0, 0]
# for i in range(5):
#     P3[i] = translation(D3[i], a, b)
#     P3[i] = transpose(array([P3[i]]))
#     P3[i] = projection(dot(R, P3[i]))
#
# x3 = [P3[i][0] for i in range(5)]
# z3 = [P3[i][2] for i in range(5)]
#
# plot(x3, z3)
# fill(x3, z3)
#
# show()

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