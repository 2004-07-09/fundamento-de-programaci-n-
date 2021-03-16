# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:28:55 2021

@author: usuario
"""

#Programa que calcula el cuadrado de los primeros 100 numeros 

#Area de declaracion de variables

cuadradoNumero = 0
acumuladorSuma = 0

#Entradas

cantidaddNumeros = int(input("Cantidad de numeros :"))


#Procesos 
#Ciclos para de 1 hasta 100 


for num in range(cantidaddNumeros+1):

    cuadradoNumero = num * num
    acumuladorSuma = acumuladorSuma + cuadradoNumero
    print("El cuadrado de :",num , "es :",cuadradoNumero)
    print("La suma acumulada es :", acumuladorSuma)
#Fin de ciclo 

print("         ")
print("         ")
print("La suma de los cuadrados es:")
print(acumuladorSuma)
