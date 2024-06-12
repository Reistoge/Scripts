
# Un cine cuenta con 4 salas disponibles de diferentes capacidades; en cada sala se muestra solo una película 
# que puede tener de 2 a 6 funciones por día.
# Los archivos de la forma “sala nombrepelicula.txt” contienen los asientos ocupados (x) y desocupados (o)
# de la primera función, seguido por una línea en blanco, la ocupación de la sala en la segunda función de 
# esa película, etc. 
# Por ejemplo,
# x x o o x o o
# o o x x o x x
# x x x x x x x
# x x x x x x x
# x x x o x o o
# x x o o
# o x x x
# x x x x
# x x x o
# Cree un menú para obtener la ocupación total de una sala dado el nombre ingresado de un archivo; la sala
# más ocupada (según su capacidad) dado un número de función ingresado; la función que recaudó más 
# fondos. Para esto último se tiene el archivo “cine.txt” el cual contiene en cada línea nombre de película y 
# precio por asiento.

# ocupacion de la sala
# recaudar màs fondos
# màs ocupada



# menu: aqui se solicitara la sala que quiere el usuario y la funcion que quiera
numero_funciones=6
salas=["los increibles 3", "saw x", "sonido de libertad", "the eras tour"]
print("Salas disponibles:\n")
i=0
for nombre in salas:
    i+=1
    print(f'{i}){nombre.capitalize()}')
print("Ingrese el nombre de la sala.")
sala=input("respuesta: ").lower().strip()
print("Ingrese la funcion")
funcion=int(input("respuesta: ").lower().strip())
while sala not in salas:
    print("\n"*100)
    print("Sala no encontrada, ingrese una Sala valida")
    print("Salas disponibles: \n")
    i=0
    for nombre in salas:
        i+=1
        print(f'{i}){nombre.capitalize()}')
    print("Ingrese el nombre de la sala.")
    sala=input("respuesta: ").lower().strip()
    print("Ingrese la funcion")
    funcion=int(input("respuesta: ").lower().strip())
    
arch2=open("cine.txt", "r",encoding="utf-8")
linea2=arch2.readline()
while linea2!="":
    if sala==linea2.split(",")[0]:
        coste=int(linea2.split(",")[1])
    linea2=arch2.readline()
    


# leer salas: aqui se leera el archivo de las salas a su correspondiente archivo

arch1=open("sala "+sala+".txt")
linea=arch1.readline().strip()
funciones=[]
for i in range(0,numero_funciones,1):
    texto=""
    texto+=linea.strip()

    while linea !="":
        linea=arch1.readline().strip()
        texto+=" "+linea.strip()
       
    funciones.append(texto)
    linea=arch1.readline()
    
    if funciones[i]==funciones[0] and i>1:
        break
    

    
# funciones siempre tendra el tamaño de numero de funciones
# funciones
desocupados_funciones=[]
ocupados_funciones=[]
ganancia_funciones=[]
ganancia_mayor=0
porcentaje_mayor=0
funcion_ganancia_mayor=''
funcion_porcentaje_mayor=''
for i in range(0,len(funciones),1):
    if funciones[i]!="":
        print(f"funcion {i+1}:\n{funciones[i]} ")
        ocupados=0
        desocupados=0
        for letra in funciones[i]:
            if letra=="x":
                ocupados+=1
            elif letra=="o":
                desocupados+=1
        desocupados_funciones.append(desocupados)
        ocupados_funciones.append(ocupados)
        ganancia_funciones.append(coste*ocupados)
        
        total=desocupados+ocupados
        ganancia=coste*ocupados
        porcentaje_de_ocupacion=(ocupados/total)*100
        
        if porcentaje_de_ocupacion>=porcentaje_mayor:
            porcentaje_mayor=porcentaje_de_ocupacion
            funcion_porcentaje_mayor=i+1
            
        if  ganancia> ganancia_mayor:
            ganancia_mayor=ganancia
            funcion_ganancia_mayor=i+1
   

print(desocupados_funciones)
print(ocupados_funciones)
print(ganancia_funciones)


print(ganancia_mayor)
print(porcentaje_mayor)
print(funcion_ganancia_mayor)
print(funcion_porcentaje_mayor)




# precios










    
    