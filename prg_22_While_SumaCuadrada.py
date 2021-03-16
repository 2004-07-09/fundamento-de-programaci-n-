# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:53:57 2021

@author: usuario
"""


#Ciclo While
#Declaracion de variables

cantidaddNumeros = 0
contadorRepeticiones = 1
cuadradoNumero = 0
acumuladorSuma = 0

#Entradas

cantidaddNumeros = int(input("Cantidad de numeros :"))

#Procesos

while contadorRepeticiones <= cantidaddNumeros:
    cuadradoNumero = pow(contadorRepeticiones,2)
    acumuladorSuma += cuadradoNumero
    print("El cuadrado de :",contadorRepeticiones , "es:",cuadradoNumero)
    print("La suma acumulada es :", acumuladorSuma)
    contadorRepeticiones=contadorRepeticiones+1
    
#Fin While

#Salida

print("La suma de los cuadrados es :")
print(acumuladorSuma)