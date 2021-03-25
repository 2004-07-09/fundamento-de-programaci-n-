# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 09:00:19 2021

@author: santi
"""

def lista_10():
    elementos= []
    for x in range(10):
        elemento = int(input('Ingrese un número: '))
        elementos.append(elemento)
    return elementos
def pos_neg(elementos):
    positivos = []
    negativos = []
    for x in range(len(elementos)):
        if elementos[x] > 0:
            positivos.append(elementos[x])
        else:
            negativos.append(elementos[x])
    print(positivos, negativos)
pos_neg(lista_10())