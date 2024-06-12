
#Comencemos con algo sencillo. Crea un ciclo for que se repita 5 veces y que imprima la variable iteradora.
variable='hola'
for i in range(5):
    print(variable)
#Luego haz lo mismo con un ciclo while.
a=5
while a>0:
    print(variable)
    a-=1
    
#Crea un programa que imprima los números impares hasta el 50
for i in range(1,50,2):
    print(i)
    
#Luego intenta imprimir la suma de los primeros 100 enteros.
sum=0
for i in range(1,101,1):
    sum+=i
print(sum)