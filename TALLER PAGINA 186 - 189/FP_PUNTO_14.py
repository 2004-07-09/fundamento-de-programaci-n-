# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:34:59 2021

@author: santi
"""

"""
Se dispone una lista de N números. Se desea calcular el valor del
número mayor.
"""
n = int(input('Ingrese la cantidad de números: '))
num = int(input('Ingrese el número:  '))
maximo = num 
x = 1
while x < n:
    x = x+1
    num = int(input('Ingrese el número:  '))
    if num > maximo:
        maximo = num
print(f'El número mayor ingresado fue {maximo}')