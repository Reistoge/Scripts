# Construye una función llamada esPrimo que recibe como parámetro un 
# número, y retorna True o False dependiendo si el número es o no primo.
# Por ejemplo:
# print(esPrimo(7)) # retorna True
# print(esPrimo(6)) # retorna False
# print(esPrimo(7351)) # retorna True
# Después, usa la función esPrimo dentro de un ciclo para escribir por pantalla 
# los números primos entre 3 y 100


def esprimo(numero):
    primo=True
    for i in range(2,numero,1):
        if numero%i==0:
            primo=False

    return primo

for i in range(3,100,1):
    if esprimo(i):
        print(i)