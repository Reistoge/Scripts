# ayudantia ejercicio 3

def tomar_jugadores(n_jugadores):
    lista_jugadores=[]
    
    for i in range(n_jugadores):
        jugador=input(f"jugador {i+1}: ")
        lista_jugadores.append(jugador)
    return lista_jugadores
       

def formatear_lista(lista):
    lista_nueva=[]
    for i in lista:
        if i!="0":
            lista_nueva.append(i)
    return lista_nueva

def rondas(lista):
    _jugadores=len(lista)
    rondas=int(_jugadores/2)
    contador=1
    while len(lista)!=2:
        print(f"ronda {contador}: ")      
        for i in range(0,len(lista),2):
            opcion=input(f"{lista[i]} - {lista[i+1]}: ")
            if opcion=="a":
                lista[i+1]="0"
            elif opcion=="b":
                lista[i]="0"
                
        rondas=int(rondas*0.5)
        contador+=1
        lista=formatear_lista(lista)
        
    print(f"ronda {contador}: ")  
    opcion=input(f"{lista[0]} - {lista[1]}: ")
    if opcion=="a":
        print(f"ganador: {lista[0]}")
    elif opcion=="b":
        print(f"ganador: {lista[1]}")

def verificar_torneo_valido(numero):
    temp=numero
    while temp>1:
        temp=temp*0.5
        if temp==2:
            return True
    
    return False
        
 
def mostrar_torneos_disponibles(n_min,n_max):
    contador=0
    for i in range(n1,n2,1):
        
        if verificar_torneo_valido(i):
            contador+=1
            print(f"{i} jugadores es un torneo valido ")

    if contador==0:
        print("no hay torneos validos para este intervalo.")
        
         
    
    

n=int((input("jugadores: ")))
while not verificar_torneo_valido(n) or n==1:
    print("\n"*10000)
    print("Numero de jugadores no apto para 1v1")
    ver=int(input("Quieres los numeros de jugadores validos para el torneo en un intervalo deseado ?: "))
    if ver==1:
        n1=int(input("minimo: "))
        n2=int(input("maximo: "))
        mostrar_torneos_disponibles(n1,n2)
    
    n=int((input("jugadores: ")))
     


                
                    
jugadores=tomar_jugadores(n)
rondas(jugadores)

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    

                    