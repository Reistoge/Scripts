# ayudantia 8 carreras.txt


def intercambiar(lista,i,j):
    aux =lista[i]
    lista[i]=lista[j]
    lista[j]=aux
    
def menor_a_mayor(lista,lista2):
    for i in range(0,len(lista)-1,1):
        for j in range(i+1,len(lista),1):
            if lista[i]>lista[j]:
                intercambiar(lista, i, j)
                intercambiar(lista2, i, j)
def mayor_a_menor(lista,lista2):
    for i in range(0,len(lista)-1,1):
        for j in range(i+1,len(lista),1):
            if lista[i]<lista[j]:
                intercambiar(lista, i, j)
                intercambiar(lista2, i, j)
                
def determinar_unicos(lista,lista2,elemento,elemento2):
    if elemento not in lista:
        lista.append(elemento)
        lista2.append(elemento2)
    else:
        lista2[lista.index(elemento)]+=elemento2
                    
arch=open("carrera.txt","r",encoding="utf-8")
linea=arch.readline().strip()
corredores=[]
tiempos=[]
corredores_unicos=[]
tiempos_unicos=[]
while linea!="":
    partes=linea.split(",")
    nombre=partes[0]
    tiempo=abs(float(partes[1]))
    
    corredores.append(nombre)
    tiempos.append(tiempo)
    determinar_unicos(corredores_unicos,tiempos_unicos,nombre, tiempo)
    
    linea=arch.readline().strip()
    
menor_a_mayor(tiempos, corredores)
mayor_a_menor(tiempos_unicos, corredores_unicos)
print(corredores)
print(tiempos)

print(corredores_unicos,tiempos_unicos)
