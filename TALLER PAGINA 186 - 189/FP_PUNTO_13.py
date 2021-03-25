# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:34:29 2021

@author: santi
"""

"""
Bucles anidados.
"""
n1 = 1
while n1 != 0:
    n = int(input('Ingrese un número: '))
    n1 = n
    for x in range(5):
        print(n*n)
print('fin')