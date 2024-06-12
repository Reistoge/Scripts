#Ahora pregunta por un numero inicial, uno final e imprime la suma de los números que se encuentren entre este rango, excluyendo los extremos.
#Ahora pide un tercer numero. Y luego imprime la sucesión de números en el intervalo del tercer numero. 
#Por ejemplo, si el inicial es 5, el final es 20 y el intervalo es 4, tendrás que imprimir el rango de números de 4 en 4. 
#5, 9, 13, 17.



a=int(input())
b=int(input())
suma=0
for i in range (a,b,1):
    suma+=i
print(suma)

c=int(input())
for i in range(a,b,c):
    print(i)