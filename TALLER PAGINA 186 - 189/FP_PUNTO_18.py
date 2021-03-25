# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:38:01 2021

@author: santi
"""

"""
Calcular factorial (otro metodo)
"""
n = int(input('Ingrese un número: '))
factorial = 1
x = 1
while x <= n:
    factorial = factorial * x
    x = x+1
print(f'El factorial de {n} es {factorial}')