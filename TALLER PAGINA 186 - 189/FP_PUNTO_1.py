# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:25:22 2021

@author: santi
"""

"""
Calcular el factorial de un número N utilizando la estructura desde
"""
n = int(input('Ingrese un valor: '))
factorial = 1
for x in range(n):
    factorial = factorial * (n-x)
print(f'El factorial de {n} es {factorial}')   