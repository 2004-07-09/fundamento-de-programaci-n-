# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:30:03 2021

@author: santi
"""

"""
Realizar el algoritmo para obtener la suma de los números pares
hasta 1000
"""
suma = 0
x=0
while x <= 1000:
    x=x+1
    if x%2 == 0:
        suma = suma + x
print(f'La suma de los números pares hasta 1000 incluyendo el 1000 es {suma}')