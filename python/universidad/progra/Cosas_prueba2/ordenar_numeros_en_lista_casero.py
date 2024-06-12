#ordenar numeros en una lista
lista1=[1,5,4,12,78,23,6,7,3,2,2,2,2,2,4,2,4,56]
lista2=[9,4,6,2,3]

## deter
def determinar_menor_lista(lista):
    menor=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]<menor:
            menor=lista[i]
    return menor

def crear_lista_sin_ese_elemento(lista,elemento):
    lista_nueva=[]
    for i in range(0,len(lista)):
        if elemento!=lista[i]:
            lista_nueva.append(lista[i])
    
    return lista_nueva

def determinar_numeros_unicos(lista):
    lista_unicos=[]
    for i in lista:
        if i not in lista_unicos:
            lista_unicos.append(i)
    return lista_unicos
    
def ordenar_lista(lista):
    lista_ordenada=[]
    lista_recursiva=lista
    for i in range(0,len(determinar_numeros_unicos(lista)),1):
        menor=determinar_menor_lista(lista_recursiva)
        lista_recursiva=crear_lista_sin_ese_elemento(lista_recursiva, menor)
        lista_ordenada.append(menor)
    return lista_ordenada

print(sorted(lista1))
print(ordenar_lista(lista1))