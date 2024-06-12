# def encontrar_mayor():
# def encontrar_n_mayores():
# def ordenamiento_multicriterio():

# que te ordene las listas independiente del numero de listas independientes


def intercambiar(lista,i,j):
    # intercambio de variables, en este 
    # caso no es necesario retornar nada ya que el scope de las listas es mayor en python
    aux=lista[i]
    lista[i]=lista[j]
    lista[j]=aux
    
def ordenamiento_menor_mayor(lista):
    # siempre va revisando el menor
    for i in range(0,len(lista)-1,1):
         
        for j in range(i+1,len(lista),1):
            # va siempre buscando el menor
            if lista[i]<lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
                print(lista)

    return lista
def ordenamiento_mayor_menor(lista):
    # siempre va revisando el mayor
    for i in range(0,len(lista)-1,1):
         
        for j in range(i+1,len(lista),1):
            # va siempre buscando el menor
            if lista[i]<lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
                print(lista)

    return lista

def ordenamiento_multiple(lista,lista_dependiente,orden):
    # puede ir revisando de menor a mayor pero son con listas paralelas
    if orden=="max_to_min":
        for i in range(0,len(lista)-1,1):
             
            for j in range(i+1,len(lista),1):
                # va siempre buscando el menor
                if lista[i]<lista[j]:
                    # ¿es mayor?, si lo es, lo cambio, si no lo es sigue con el siguiente j
                    intercambiar(lista1, i, j)
                    intercambiar(lista2, i, j)

        
    elif orden=="min_to_max":
        for i in range(0,len(lista)-1,1):
             
            for j in range(i+1,len(lista),1):
                # va siempre buscando el menor
                if lista[i]>lista[j]:
                    # ¿es menor?, si lo es, lo cambio, si no lo es sigue con el siguiente j
                    intercambiar(lista1, i, j)
                    intercambiar(lista2, i, j)
                
def ordenamiento_alfabetico(lista,lista_dependiente):
    for i in range(0,len(lista)-1,1):
        for j in range(i+1,len(lista),1):
            if lista[i]>lista[j]:
               
                intercambiar(lista, i, j)
                intercambiar(lista_dependiente, i, j)
                
        
               
def ordenamiento_multicriterio(lista,lista_dependiente):
    for i in range(0,len(lista),1):
        for j in range(0,len(lista),1):
            if lista[i]<lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
                # si no cambias el index de lista_dependiente el algoritmo no funcionara.
                intercambiar(lista_dependiente, i, j)
            elif lista[i]==lista[j]:
                if lista_dependiente[i]<lista_dependiente[j]:
                    intercambiar(lista_dependiente, i, j)
                    
                    
def ordenamiento_multicriterio2(lista1,lista_dependiente,orden):
    if orden=="A_Z":
        for i in range(0,len(lista1),1):
            for j in range(0,len(lista1),1):
                if (lista1[i]<lista1[j] or ((lista1[i]==lista1[j]) and (lista_dependiente[i]<lista_dependiente[j]))):
                    intercambiar(lista1, i, j)
                    intercambiar(lista_dependiente, i, j)
    elif orden=="Z_A":         
        for i in range(0,len(lista1),1):
            for j in range(0,len(lista1),1):
                if (lista1[i]<lista1[j] or ((lista1[i]==lista1[j]) and (lista_dependiente[i]>lista_dependiente[j]))):
                    intercambiar(lista1, i, j)
                    intercambiar(lista_dependiente, i, j)
                    
        
lista2=["pedro","zuan","diego","ferran","miguel","antonio","antonio"]
lista1=[12,2,23,1,2,3,15]

ordenamiento_multicriterio2(lista1, lista2,"Z_A")
print(lista1)
print(lista2)
for i in range(0,len(lista1),1):
    print(lista2[i],end=" ")
    print(lista1[i])
    


        
    