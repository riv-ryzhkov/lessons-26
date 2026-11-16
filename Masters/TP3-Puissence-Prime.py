#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:51:36 2021

@author: jrh & riv

"""
from math import *


# ################ Exercice 1
     

def puiss1(a,b):
    global count   #  riv

    res = 1
    for k in range(b):
        res = res * a
        count += 1    #  riv
    return res


# a = 1
# # b = 2_000
# b = 100_000_000
# count = 0
# print('resultat puiss1    =', puiss1(a, b))    #  riv
# print("nombre d'iteration =", count)
# print()






# def puiss2(a, b):
#     global count
#
#     if b == 0:
#         return 1
#     else:
#         count += 1
#         return a * puiss2(a, b-1)
#
#
# count = 0    #  riv
# print('resultat puiss2    =', puiss2(a, b))
# print("nombre d'iteration =", count)
# print()












def puiss3(a, b):
    global count    #  riv
    count += 1

    if b == 0:
        return 1
    elif b % 2 == 0:
        c = puiss3(a, b//2)      # (a**(b/2))*(a**(b/2))=a**b
        return c * c
    else:
        return a * puiss3(a, b-1)


# count = 0
# print('resultat puiss3    =', puiss3(a, b))
# print("nombre d'iteration =", count)
# print('='*30)
# print()








# ###################### 1.6

def puiss_mod(a, b, n):
    if b == 0:
        return 1
    elif b % 2 == 0:
        c = puiss_mod(a, b//2, n)
        return (c * c) % n
    else:
        return (a * puiss_mod(a, b-1, n)) % n





# print('2^2 % 3     =', puiss_mod(2, 2, 3))
# print('5^2 % 7     =', puiss_mod(5, 2, 7))
# print('2^10 % 37   =', puiss_mod(2, 10, 37))
# print('10^2 % 52   =', puiss_mod(10, 2, 52))
# print('10^100 % 17 =', puiss_mod(10, 100, 17))





# ########################## Exercice 2 : tests de primalité

def test_premier(n):
    count = 0    #  riv
    if n == 1:
        res = False
    else:
        res = True
        for div in range(2, n):
            count +=1    #  riv
            if n % div == 0:
                print('n_iter =', count, '  diviseur =', div)    #  riv
                res = False
                return res
    print('n_iter =', count)    #  riv
    return res


# a, b, c, e = 1025, 1024, 1023, 1021
# print(a, test_premier(a), '\n', '='*30, '\n')
# print(b, test_premier(b), '\n', '='*30, '\n')
# print(c, test_premier(c), '\n', '='*30, '\n')
# print(e, test_premier(e), '\n', '='*30, '\n')


# print('*' * 30)

################################### riv
# def test_premier1(n):
#     count = 0      #  riv
#     if n == 1:
#         res = False
#     else:
#         res = True
#         for div in range(2, n//2+1):    # [2; n//2]
#             count += 1    #  riv
#             if n % div == 0:
#                 print('n_iter =', count, '  diviseur =', div)    #  riv
#                 return False
#     print('n_iter =', count)    #  riv
#     return res
#
#
#
# a, b, c, e = 1025, 1024, 1023, 1021
# print(a, test_premier1(a), '\n', '='*30, '\n')
# print(b, test_premier1(b), '\n', '='*30, '\n')
# print(c, test_premier1(c), '\n', '='*30, '\n')
# print(e, test_premier1(e), '\n', '='*30, '\n')





# from math import *
# Version legerement ameliorée : on ne cherche des diviseurs que
# jusqu'à racine de n.


def test_premier2(n):
    count = 0     #  riv
    if n == 1:
        return False
    else:
        res = True
        for div in range(2, ceil(sqrt(n))+1):
            count += 1    #  riv
            if n % div == 0:
                # print('n_iter =', count, '  diviseur =', div)    #  riv
                return False
        # print('n_iter =', count)    #  riv
        return res
    
#
# a, b, c, e = 1025, 1024, 1023, 1021
# print(a, test_premier2(a), '\n', '='*30, '\n')
# print(b, test_premier2(b), '\n', '='*30, '\n')
# print(c, test_premier2(c), '\n', '='*30, '\n')
# print('sqrt(e) =', sqrt(e))
# print(e, test_premier2(e), '\n', '='*30, '\n')





# a = 1021    #  1021    
# print(a, 'test_premier', test_premier(a))
# print(a, 'test_premier1', test_premier1(a))
# print(a, 'test_premier2', test_premier2(a))
# print()
# print()


# Test de pseudo-primalité. On applique le critère de Fermat
# à quatre valeurs de a. Si le test est satisfait les 4 fois, 
# on considère que le nombre n est probablement premier.
# les nombres de Carmichael: 561, 1105, 1729, 2465, 2821, 6601


# def fermat(n):

#     count = 0     #  riv
#     res = 'probablement premier'
#     for a in [2, 3, 5, 7]:
#         count += 1
#         c = puiss_mod(a, n, n)
#         if c != a:
#             res = 'non premier'
#             break
#     print('n_iter =', count, 'c =', c)    #  riv
#     return res
#
# a, b, d, e = 1024, 1021, 561, 1105
# print(a, fermat(a), '\n', '='*30, '\n')
# print(b, fermat(b), '\n', '='*30, '\n')
# print(d, fermat(d), f'mais {d}:3 = {d/3} \n', '='*30, '\n') #   les nombres de Carmichael
# print(e, fermat(e), f'mais {e}:5 = {e/5} \n', '='*30, '\n') #   les nombres de Carmichael




################################################### les nombres de Carmichael

# n = 100_000
# for i in range(8, n):
#     if fermat(i) == 'probablement premier' and test_premier2(i) == False:
#         print(i)


# ##################################
# def fermat(n):
#     count = 1     #  riv 
#     num = [
#         561,
#         1105,
#         1729,
#         2465,
#         2821,
#         6601,
#         8911,
#         10585,
#         15841,
#         29341,
#         41041,
#         46657,
#         52633,
#         62745,
#         63973,
#         75361
#         ]    
#     if n in num:
#         print('n_iter =', count) 
#         return 'non premier'

#     res = 'premier!!!'
#     for a in [2, 3, 5, 7]:
#         count += 1
#         c = puiss_mod(a, n, n) 
#         if c != a:
#             res = 'non premier'
#             break
#     print('n_iter =', count)    #  riv
#     return res


# a, b, d, e = 1024, 1021, 561, 1105
# print(a, fermat(a), '\n========\n')
# print(b, fermat(b), '\n========\n')
# print(e, fermat(e), '\n========\n')
# print(d, fermat(d), '\n========\n')



