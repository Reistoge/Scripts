# Ejercicio 2:
# Cree una función que dado un número n, imprima todas las posibles formas de obtenerlo como producto de 
# dos enteros. No debe contabilizar las repeticiones conmutativas (por ejemplo, 4x9 y 9x4 solo cuenta como
# una forma)
def operacion(n):
    for i in range(1,n,1):
        if n%i==0 and i<=n/i:
            a=(n/i)
            print(f"{i} * {a} = {n}")

n=int(input("ingresa un numero: "))
operacion(n)