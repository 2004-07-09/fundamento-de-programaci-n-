# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:31:45 2021

@author: santi
"""

"""
Escribir un algoritmo que permita escribir en una pantalla la frase 
'Desea continuar? S/N' hasta que la respuesta sea S o N 
"""
x = True
while x == True:
    print('Desea continuar? S/N')
    respuesta = input('Respuesta: ')
    if respuesta == 'S' or respuesta == 'N':
        break 