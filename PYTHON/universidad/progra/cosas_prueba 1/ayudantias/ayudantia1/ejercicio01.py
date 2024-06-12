### ver si el numero es primo o no 
###solucion por ayudante


numero=int(input("Ingrese un número: "))
i=2
es_primo=False

## inicializamos la variable en false para que entre al while
while i < numero and es_primo:
    if numero%i==0:
        print("no es primo")
        es_primo=False
    i+=1
if es_primo:
    print("Es primo")    
        