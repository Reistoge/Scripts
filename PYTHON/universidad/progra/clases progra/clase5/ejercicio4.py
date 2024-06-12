# Construya un programa que informe sobre el número de anillos que aparecen 
# en los dígitos de un número. Para ello deberá crear una función llamada 
# ANILLOS, la cual recibirá un número entero introducido por teclado. Considere 
# lo siguiente:
# • Se considera que los dígitos 0, 6 y 9 están formados por un anillo
# • Se considera que el digito 8 está formado por dos anillos.
# • El resto de los números no tiene anillos
# El programa deberá consultar al usuario si desea evaluar otro número, en el 
# caso de que se ingrese la palabra “No”, el programa terminará


def anillos(n):
    anillo=[0,6,9]
    anillos=8
    if int(n) in anillo:
        print("Hay un anillo en tu numero")
    elif int(n) == anillos:
        print("hay dos anillos en tu numero")
    else:
        print("no tienes anillos :c")
numero=input("ingresa tu numero: ")
while numero!="no":
    anillos(numero)
    input("presiona Enter para continuar")
    print("\n"*100)
    numero=input("ingresa tu numero: ")
    
   