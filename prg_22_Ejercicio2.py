# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:29:58 2021

@author: usuario
"""

#librerias usadas en el ejercicio

import random 

#Ejercicio 2

#Area declaracion de variables

contadorRepeticiones = 0
numero = 0
acumuladorSumaTodosNumero = 0
acumuladorsumaNumerosPositivos = 0
acumuladorsumaNumerosNegativos = 0
cantidadNumeros = 1

#entradas

cantidadNumeros=int(input("Cantidad de numeros :"))

#Procesos

while contadorRepeticiones <cantidadNumeros:
    numero=random.randint(-100,100) #Generamos numero aleatorio
    print("numero :",numero)
    acumuladorSumaTodosNumero=acumuladorSumaTodosNumero+numero  #acumulo positivos
    if numero>0:
        acumuladorsumaNumerosPositivos=acumuladorsumaNumerosPositivos+numero
    else:
        acumuladorsumaNumerosNegativos=acumuladorsumaNumerosNegativos+numero
    contadorRepeticiones=contadorRepeticiones+1
#Fin del ciclo
    
#Salida de resultados
print("La suma de todos los numeros es :",acumuladorSumaTodosNumero)
print("   ")
print("La suma de todos los numeros positivos es :", acumuladorsumaNumerosPositivos)
print("   ")
print("La suma de todos los numeros negativos es :", acumuladorsumaNumerosNegativos)
