num_1= int(input("Digite el primer numero:"))
num_2= int(input("Digite el segundo numero:"))
num_3= int(input("Digite el tercer numero:"))

if (num_1 > num_2):
    if (num_1 > num_3):
        print("El numero mayor es" + str(num_1))   

if (num_2 > num_3):
    if (num_1 > num_3):
        print("El numero mayor es:" + str(num_2))
      
else:
    print("El numero mayor es:"+ str(num_3))
