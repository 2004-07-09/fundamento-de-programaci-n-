# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:39:51 2021

@author: santi
"""

"""
Determinar la media de una lista indefinida de números positivos,
terminados con un número negativo. 
"""
import numpy
n_list = []
x = True
while x == True:
    num = int(input('Agrege un numero a la lista: '))
    if num >= 0:
        n_list.append(num)
        continue
    else: 
        break
media_lista = numpy.mean(n_list)
print(f'La media de la lista es {media_lista: .2f}')