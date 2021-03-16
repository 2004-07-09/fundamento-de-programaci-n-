sum = 0
med = 0.0
cantL = 0
contadorR = 0 
salida = False

while (contadorR<=7):
    num=int(input("digite su eded :"))
    if(num >0):
    sum = sum + num
    cantL = cantL+1
    else:
        salida = True
        

med = sum / cantL
print("El promedio es de :", med)                
                
