# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:53:56 2021

@author: santi
"""

def multiplicar(lista, escalar):
    for x in range(len(lista)):
        lista[x] = lista[x]*escalar
    print(lista)
                

lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)