# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:58:17 2021

@author: santi
"""

def orden_num(n1,n2,n3):
    if n1 < n2 and n1 < n3:
        if n2 < n3:
            print(n1,n2,n3)
        else:
            print(n1,n3,n2)
    if n2 < n1 and n2<n3:
        if n1<n3:
            print(n2, n1, n3)
        else:
            print(n2, n3, n1)
    if n3 < n2 and n3 < n1:
        if n1 < n2:
            print(n3,n1,n2)
        else:
            print(n3, n2,n1)
    
def variables():
    n1 = int(input('Ingrese un número: '))
    n2 = int(input('Ingrese un número: '))
    n3 = int(input('Ingrese un número: '))
    orden_num(n1,n2,n3)
    
variables()