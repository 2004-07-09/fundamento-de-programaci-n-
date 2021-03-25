# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:31:01 2021

@author: santi
"""

"""
Se desea leer de una consola una serie de números hasta obtener 
un número inferior a 100
"""
x=True
while x==True:
    num = int(input('Escriba un número: '))
    if num < 100:
        print('Escribio un número menor a 100')
        break