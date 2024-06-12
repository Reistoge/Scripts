def ingresar_dos_numeros():
    numero1=(input("Ingresa el primer numero: "))
    numero2=(input("Ingresa el segundo numero: "))
    while numero1 not in ["0","1"] and numero2 not in ["0","1"]:
        saltar_n_lineas(100)
        numero1=(input("Ingresa el primer numero: "))
        numero2=(input("Ingresa el segundo numero: "))
    saltar_n_lineas(100)
    return [numero1,numero2]
def saltar_n_lineas(n):
    print("\n"*n)
def repetir_programa():
    opciones=["0","1"]
    opcion=input("Ingresa 0 para salir y 1 para volver a introducir dos numeros: ").lower().strip()
    while opcion not in opciones:
        saltar_n_lineas(100)
        opcion=input("Ingresa 0 para salir y 1 para volver a introducir dos numeros").lower().strip()
    return int(opcion)
def sumar_o_multi_dos_numeros(numeros):
    opciones=["a","b","c"]
    print(f"Ingresaste los numeros {numeros[0]} y {numeros[1]}")
    print("Que operacion quieres realizar?: \na)Multiplicar los numeros \nb)Sumar los numeros \nc)Salir")
    opcion=input("Input :").lower().strip()
    while opcion not in opciones:
        saltar_n_lineas(100)
        print("En este programa solo puedes multiplicar o sumar.")
        input("Ingrese ENTER Para continuar")
        saltar_n_lineas(100)
        print(f"Ingresaste los numeros {numeros[0]} y {numeros[1]}")
        print("Que operacion quieres realizar?: \na) Multiplicar los numeros \nb) Sumar los numeros \nc) Salir")
        opcion=input("Que operacion quieres realizar?: ")
    if opcion=="a":
        print(f"El producto entre estos dos numeros es: {numeros[1]*numeros[0]}")
        if repetir_programa()==1:
            return 1
        else:
            print("Saliendo...")
            return 0
    elif opcion=="b":
        print(f"La suma entre estos dos numeros es: {numeros[0]+numeros[1]}")
        if repetir_programa()==1:
            return 1
        else:
            print("Saliendo...")
            return 0
    elif opcion not in ["salir", "c"]:
        print("saliendo...")
        return 0
while sumar_o_multi_dos_numeros(ingresar_dos_numeros())==1:
    saltar_n_lineas(100)
    sumar_o_multi_dos_numeros(ingresar_dos_numeros())



    

