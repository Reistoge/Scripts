#escribe un programa que simule un cajero automatico. el programa debe permitir al usuario realizar las 
# siguientes variables.
#### poner input dentro de while"

#consultar saldo
#depositar dinero
#retirar dinero
#salir

#el programa debe mantener un saldo inicial de 1000 dolares y permitir al usuario realizar operaciones 
#hasta que decida salir asegurate de validar las entradas del usuario para evitar errores

saldo=1000
opcion=0
while opcion!=4:
    
    print("==Cajero Automatico==")
    print("Seleccione una opcion: ")
    print("1. consultar saldo")
    print("2. depositar saldo")
    print("3. retirar saldo")
    print("4. salir")
    opcion=int(input("> "))
      
    for i in range(50):
        print("")
    while opcion > 5 or opcion <1:
        print("opcion invalida")
        opcion=int(input("> "))
  
    
    if opcion==1:
        print("tienes $", saldo, "dolares!" )
        input("presione [Enter] para continuar")
    
    if opcion==2:
        print("==depositar==")
        deposito=int(input("cantidad a depositar: "))
        while deposito<1:
            deposito=int(input("valor invalido. cantidad a depositar: "))
        
        saldo+= deposito
        print("¡dinero depositado exitosamente")
        input("presione [Enter] para continuar")
    
    if opcion==3:
        print("==Retirar==")
        deposito=int(input("cantidad a retirar: "))
        while deposito<1:
            deposito=int(input("valor invalido. cantidad a retirar: "))
        
        saldo-= deposito
        print("¡dinero retirado exitosamente")
        input("presione [Enter] para continuar")
        
print("saliendo")
