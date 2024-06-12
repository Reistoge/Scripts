### ver si el numero es primo o no 
###solucion por ayudante

import random
numero_secreto=random.randint(1,100)
cantidad_intentos=0
intento=int(input("Intenta adivinar: "))
while intento!=numero_secreto:
    if intento<numero_secreto:
        print("mas alto")
    elif intento>numero_secreto:
        print("mas bajo")
    intento=int(input("Intenta adivinar"))
    cantidad_intentos+=1

print("Felicidades!")
print("¡Te tomó", cantidad_intentos,"adivinar")
    
