#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:51:36 2021

@author: Igor Ryzhkov
"""

import numpy as np
import matplotlib.pyplot as plt
import math


# #################################################
# ##############    Exercice 1    #################
# #################################################

a = 0
b = 1

# ## Méthode des points milieux ####

def f(x):
    # y = x**2
    # y = np.exp(x)
    y = np.cos(x)
    return y



def pt_mil(a, b, n):
    dx = (b-a) / n
    res = 0
    for i in range(n):
        res = res + f(a+i*dx)
        # res = res + f(a+(i+1)*dx)
        # res = res + f(a+(i+0.5)*dx)
    res = res * dx
    return res


x = np.linspace(0, 1, 100)
y = f(x)
# print(type(x), x)
# print(type(y), y)
# plt.plot(x, y)
# plt.show()

n = 20
# print('result     e-1  =\t\t\t', np.e - 1)
# print('result     x^2  =\t\t\t', 1/3)
# print('result  sin(x)  =\t\t\t', np.sin(1))
#
# print('Méthode des rectangles =\t', pt_mil(a, b, n))


# # #### Méthode des trapèzes ####

def trapz(a, b, n):
    dx = (b-a)/n
    res = 0.5*(f(a)+f(b))
    for i in range(1, n):
        res = res + f(a+i*dx)
    res = dx*res
    return res


# print('Méthode des trapèzes =\t\t', trapz(a, b, n))

# # # # #### Méthode de Simpson ####


def Simps(a, b, n):
    dx = (b-a)/n
    res = f(a) + f(b) + 4 * f(a+dx/2)
    for i in range(1, n):
        res = res + 2 * f(a+i*dx) + 4*f(a+dx/2+i*dx)
    res = res * (dx/6)
    return res


# print('Méthode de Simpson =\t\t', Simps(a, b, n))


# # # #### Vitesse de convergence :
# # # # # ??????????????????????????????????????????????
# a = 0
# b = 1
#
# n = 30
# # n = 500
#
# # I = 1/3
# # I = np.exp(1)-1
# I = np.sin(1)
#
#
# err_PtMil = np.zeros(n)
# err_Trapz = np.zeros(n)
# err_Simps = np.zeros(n)
#
# for i in range(n):
#     err_PtMil[i] = np.abs(pt_mil(a, b, i+1) - I)
#     err_Trapz[i] = np.abs(trapz(a, b, i+1) - I)
#     err_Simps[i] = np.abs(Simps(a, b, i+1) - I)
#
# x=[k+1 for k in range(n)]
#
# # plt.plot(x, err_PtMil, color='blue')
# # plt.plot(x, err_Trapz, color='green')
# # plt.plot(x, err_Simps, color='black')
#
#
# plt.plot(np.log(x), np.log(err_PtMil), color='blue')
# plt.plot(np.log(x), np.log(err_Trapz), color='green')
# plt.plot(np.log(x), np.log(err_Simps), color='black')
#
# plt.plot(np.log(x), -1*np.log(x), '+', color='red')
# plt.plot(np.log(x), -2*np.log(x), '+', color='y')
# plt.plot(np.log(x), -4*np.log(x), '+', color='m')
#
# plt.title("Vitesse de convergence")
# plt.show()


# #################################################
# ##############    Exercice 2    #################
# #################################################


# #### Question 3 :


# # def rectg(a, b, n):
# #     dx = (b-a)/n
# #     res = 0
# #     for i in range(n):
# #         res = res + f(a+i*dx);
# #     res = res * dx
# #     return res


# # ### Vitesse de convergence :

# # a = 0
# # b = 1

# # n = 500
# # I = np.exp(1)-1


# # err_rectg = np.zeros(n)

# # for i in range(n):
# #     err_rectg[i] = abs(rectg(a, b, i+1)-I)


# # x = [k+1 for k in range(n)]


# # # plt.plot(x, err_rectg)


# # plt.plot(np.log(x),np.log(err_rectg),"m")
# # plt.plot(np.log(x),-np.log(x),'+', "b")
# # plt.show()


###################################################################

# #################################################
# ##############    Exercice 3    #################
# #################################################


# # On sait que l’accélération γ est la dérivée de la vitesse V, donc,
# # V(t)=V(0)+int(γ(s),s=0..t) Donc V(80)=0+int(γ(s),s=0..80)


# # Calculons I par la méthode des trapèzes. Ici, d’après le tableau
# # des valeurs, h=10. On en déduit que


dx = 10
gam = [30, 31.63, 33.44, 35.47, 37.75, 40.33, 43.29, 46.70, 50.67]
n = len(gam)


x = [i for i in range(0, 85, 10)]
for i in range(n):
    plt.plot([i*10, i*10],[30, gam[i]])
    pass

plt.plot(x, gam, 'o')
plt.xlabel('t, s')
plt.ylabel('gamma (m/s^2)')
plt.title("L'accéeleration")
# plt.grid(True)
plt.show()

# # # # # le graphique de la fonction n'est pas droit.
# # # # # Il a une légère courbure.
#
#
Irect_ag = dx * sum(gam[:n-1])
print('Calculons I par la méthode des rectangle à gauche =', Irect_ag)


Irect_adr = dx * sum(gam[1:n])
print('Calculons I par la méthode des rectangle à droite =', Irect_adr)

print((Irect_ag+Irect_adr)/2)

gam_mil = [(gam[i]+gam[i+1])/2 for i in range(len(gam)-1)]
Irect_mil = dx * sum(gam_mil)
print('Calculons I par la méthode des points milieux =', Irect_mil)


Itrap = (dx/2) * (gam[0] + gam[n-1] + 2*sum(gam[1:n-1]))
print('Calculons I par la méthode des trapèzes =', Itrap)


# # # # # # # ###  Calculons I par la méthode de Simpson :
#
dx = 20
ISimp = (dx/6) * (gam[0] + gam[n-1] + 4*sum(gam[1:n-1:2]) + 2*sum(gam[2:n-1:2]))
print('Calculons I par la méthode de Simpson =', ISimp)


# # #################################################
# # ##############    Exercice 4    #################
# # #################################################

# # ######################### riv ##################################

#
# def f(x):
#     y = np.cos(x)
#     return y
#
#
# a = -np.pi/2
# b = np.pi/2
#
# exacte = abs(np.sin(b) - np.sin(a))
# epsi = 1e-10
# n = 1
#
# res = Simps(a, b, n)
#
#
# while abs(res-exacte) > epsi:
#     n += 1
#     res = Simps(a, b, n)
#     # print(n, res)
#
# print('exacte =', exacte)
# print('n =', n, 'result =', res)
# print('2*n =', n*2)
#
#
# x = np.linspace(a, b, 100)
# y = f(x)
# plt.plot(x, y)
#
# z = 0*x
# plt.plot(x, z)
#
# plt.show()

###############################

# def f(x):
#     y = np.cos(x)
#     return y


# epsi = 10**(-8)

# n = math.floor((((2*np.pi)**5) / (2880*epsi))**(1/4)) + 1


# print('N =', n)