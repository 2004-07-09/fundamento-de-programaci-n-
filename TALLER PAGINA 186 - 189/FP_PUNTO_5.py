# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:29:26 2021

@author: santi
"""

"""
Dados dos números enteros, realizar el algoritmo que calcule su cociente
y su resto
"""
M = int(input('Ingrese el dividendo: '))
N = int(input('Ingrese el divisor: '))
Q = 0
R = M
while R > N:
    R = R-N
    Q = Q+1
    print(Q)
print(f'Dividendo {M}, divisor {N}, cociente {Q}, resto {R}')