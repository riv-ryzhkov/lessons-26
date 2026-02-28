#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:51:36 2021

@author: jrh & riv

"""

# def f(x, y):
#     z = x**2 - 3*y
#     return z


# print(f(5, 2))



# a = f(5, 2)
# print('a =', a)


# ........................


# def affiche(name):
#     print('Bonjour,', name)



# prenom = input('Prénom : ')
# affiche(prenom)



# a = affiche('Pierre')
# print('a =', a)


# ...................................




# def rac2(eps):
#     u = 2
#     n = 0
#     while abs(u**2-2) > 2*eps:
#         u = u/2 + 1/u
#         n = n + 1
#         # n += 1
#         # print(u, n)
#     return [u, n]


# print('========', rac2(0.00001))
# print('2**(1/2)=', 2**(1/2))
    



# def fact1(n):
#     res = 1
#     for k in range(1, n+1):
#          res = res * k
#          # res *= k
#          print(k, end=' * ')
#     return res



def fact2(n):
    if n == 0:
        return 1
    else:
        print(n, end=' * ')
        return n * fact2(n-1)


# print('.'*10)
# print('=', fact1(5))
# # # 
# print('.'*10)

# print('=', fact2(5))






# ################ Exercice 1
import time
     

def puiss1(a,b):
    global n    #  riv
    res = 1
    for k in range(b):
        n += 1    #  riv
        res = res * a
    print('n puiss1 =', n)    #  riv
    return res




# a = 1000000
# a = 1_000_000
# print(a, type(a))


# a = 1    #  riv
# b = 100_000_000    #  riv
# n = 0    #  riv

# start = time.time()
# print('res piiss1 =', puiss1(a, b))    #  riv
# print('time puiss1 =', time.time() - start)
# print()







# def puiss2(a, b):
#     global n    #  riv
#     n += 1    #  riv
#     if b == 0:
#         print('n puiss2 =', n)      #  riv
#         return 1
#     else:
#         return a * puiss2(a, b-1)
    
# a = 1    #  riv
# b = 2000   #  riv
# n = 0    #  riv


# start = time.time()
# print('res piiss2 =', puiss2(a, b))    #  riv
# print('time puiss2 =', time.time() - start)
# print()












# def puiss3(a, b):
#     global n    #  riv
#     n += 1    #  riv
#     if b == 0:
#         print('n puiss3 =', n)    #  riv
#         return 1
#     elif b % 2 == 0:
#         c = puiss3(a, b/2)         # (a**(b/2))*(a**(b/2))=a**b
#         return c*c
#     else:
#         return a * puiss3(a, b-1)
 
  
# a = 1    #  riv
# b = 100_000_000   #  riv
# n = 0    #  riv

# start = time.time()
# print('res piiss3 =', puiss3(a, b))    #  riv
# print('time puiss3 =', time.time() - start)








###################### 1.6

def puiss_mod(a, b, n):
    if b == 0:
        return 1
    elif b % 2 == 0:
        c = puiss_mod(a, b/2, n)   
        return (c * c) % n
    else:
        return (a * puiss_mod(a, b-1, n)) % n



# print('4 % 3 =', puiss_mod(2, 2, 3))
# print('25 % 7 =', puiss_mod(5, 2, 7))
# print('1024 % 37 =', puiss_mod(2, 10, 37))
# print('100 % 52 =', puiss_mod(10, 2, 52))





########################## Exercice 2 : tests de primalité

# def test_premier(n):
#     count = 0    #  riv         
#     if n == 1:                  
#         res = False
#     else:
#         res = True              
#         for div in range(2,n):  
#             count +=1    #  riv
#             if n % div == 0:
#                 print('n =', count, 'div =', div)    #  riv 
#                 res = False
#                 return res
#     print('n =', count)    #  riv 
#     return res


# a, b, c, e = 1025, 1024, 1023, 1021
# print(a, test_premier(a), '\n========\n')
# print(b, test_premier(b), '\n========\n')
# print(c, test_premier(c), '\n========\n')
# print(e, test_premier(e), '\n========\n')


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
#                 print('n =', count, 'div =', div)    #  riv 
#                 return False
#     print('n =', count)    #  riv 
#     return True



# a, b, c, e = 1025, 1024, 1023, 1021
# print(a, test_premier1(a), '\n========\n')
# print(b, test_premier1(b), '\n========\n')
# print(c, test_premier1(c), '\n========\n')
# print(e, test_premier1(e), '\n========\n')





from math import *
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
                # print('n =', count, 'div =', div)    #  riv 
                return False
        # print('n =', count)    #  riv
        return res
    
    

# a, b, c, e = 1025, 1024, 1023, 1021
# print(a, test_premier2(a), '\n========\n')
# print(b, test_premier2(b), '\n========\n')
# print(c, test_premier2(c), '\n========\n')
# print('sqrt(e) =', sqrt(e))
# print(e, test_premier2(e), '\n========\n')





# a = 1021    #  1021    
# print('test_premier', test_premier(a))
# print('test_premier1', test_premier1(a))
# print('test_premier2', test_premier2(a))




# Test de pseudo-primalité. On applique le critère de Fermat
# à quatre valeurs de a. Si le test est satisfait les 4 fois, 
# on considère que le nombre n est probablement premier.
# les nombres de Carmichael: 561, 1105, 1729, 2465, 2821, 6601


def fermat(n):    
    count = 0     #  riv 
    res = 'probablement premier'
    for a in [2, 3, 5, 7]:
        count += 1
        c = puiss_mod(a, n, n) 
        if c != a:
            res = 'non premier'
            break
        
    # print('n =', count, 'c =', c)    #  riv
    return res



# a, b, d, e = 1024, 1021, 561, 1105
# print(a, fermat(a), '\n========\n')
# print(b, fermat(b), '\n========\n')
# print(d, fermat(d), f'mais {d}:3 = {d/3}\n========\n') #   les nombres de Carmichael
# print(e, fermat(e), f'mais {e}:5 = {e/5}\n========\n') #   les nombres de Carmichael




################################################### les nombres de Carmichael

n = 100_000
for i in range(8, n):
    if fermat(i) == 'probablement premier' and test_premier2(i) == False:
        print(i)


##################################
def fermat(n):
    count = 1     #  riv 
    num = [
        561,
        1105,
        1729,
        2465,
        2821,
        6601,
        8911,
        10585,
        15841,
        29341,
        41041,
        46657,
        52633,
        62745,
        63973,
        75361
        ]    
    if n in num:
        print('n =', count) 
        return 'non premier'

    res = 'premier!!!'
    for a in [2, 3, 5, 7]:
        count += 1
        c = puiss_mod(a, n, n) 
        if c != a:
            res = 'non premier'
            break
    print('n =', count)    #  riv
    return res


a, b, d, e = 1024, 1021, 561, 1105
print(a, fermat(a), '\n========\n')
print(b, fermat(b), '\n========\n')
print(e, fermat(e), '\n========\n')
print(d, fermat(d), '\n========\n')



