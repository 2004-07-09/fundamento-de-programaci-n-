# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:54:49 2021

@author: santi
"""

def mascaracteres(i):
    maxcaracteres = ''
    for x in range(len(i)):
        if len(i[x]) > len(maxcaracteres):
            maxcaracteres = i[x]
    return maxcaracteres
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))