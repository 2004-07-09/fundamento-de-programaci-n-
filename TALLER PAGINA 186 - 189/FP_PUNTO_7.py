# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:30:50 2021

@author: santi
"""

"""
Buscar y escribir la primera vocal leída del teclado
"""
x = True
while x== True:
    caracter = input('Escriba una letra: ')
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter=='u':
        print(f'Primera vocal: {caracter}')
        break