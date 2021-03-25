# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:40:50 2021

@author: santi
"""

"""
Sumar los números enteros del 1 al 100 mediante 
Estructura while
Estructura for
"""
n= 1
suma = 0
for x in range(101):
    suma = suma + x
print(suma)
suma = 0
while n <= 100:
    suma= suma+n
    n=n+1
print(suma)