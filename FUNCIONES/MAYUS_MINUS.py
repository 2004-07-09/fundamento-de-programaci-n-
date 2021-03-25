# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:55:44 2021

@author: santi
"""

def a_o_A(i):
    cont_a = 0
    cont_a_mayus = 0
    for x in i:
        if x == 'a':
            cont_a += 1
        elif x == 'A':
            cont_a_mayus += 1
    print(f'Para {i}:\nCantidad de a: {cont_a}, cantidad de A: {cont_a_mayus}')

a_o_A('Adios')
a_o_A('adios')