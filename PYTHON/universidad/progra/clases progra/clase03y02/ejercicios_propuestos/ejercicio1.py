#Un número es primo si solamente es divisible por sí mismo y por 1. 
#Esto quiere decir que el resultado de la división es un número entero, por 
#ejemplo: 
# 10 es divisible por 2 ya que 10/5 = 2 , pero 5 no es divisible por 2, ya que 5/2 = 
# 2.5 
# Construye un programa que pregunte un número, e indique si el número es 
# primo o no


numero=0
while numero!=-1:
    numero=int(input("Introduce un numero: "))
    if numero!=2 and numero%2==0:
        print("compuesto divisible por 2")
       
    elif numero!=3 and numero%3==0:
        print("compuesto divisible por 3")
        print(numero/3)
    elif numero!=5 and numero%5==0:
        print("compuesto divisible por 5")
    elif numero!=7 and numero%7==0:
        print("compuesto divisible por 7")
    else:
        print("primo")
        
        
    
        
if numero!=1 or numero!=2 or numero!=3 or numero!=5 or numero!=7:
    for i in range(1, numero):
        if numero%i==0:
            print("compuesto")
else:
    print("primo")

    
        
            
                
                
