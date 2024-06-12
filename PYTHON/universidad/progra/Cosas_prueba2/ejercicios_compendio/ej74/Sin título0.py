arch=open("texto.txt")
linea=arch.readline().strip()
autos=[]
anhos=[]
rendimientos=[]
def intercambiar(lista,i,j):
    aux=lista[i]
    lista[i]=lista[j]
    lista[j]=aux
def bubble_sort(lista,lista1):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if(lista[i]<lista[j]):
                intercambiar(lista,i,j)
                intercambiar(lista1,i,j)
            elif lista[i]==lista[j]:
                if lista1[i]>lista1[j]:
                    intercambiar(lista,i,j)
                    intercambiar(lista1,i,j)
                    
                    
                    
                    
                 
while linea!="":
    partes=linea.split(",")
    auto=partes[0]
    anho=int(partes[1])
    rend=partes[2]
    if auto not in autos and anho >2010:
        autos.append(auto)
        rendimientos.append(rend)
    
        
    
    linea=arch.readline().strip()
bubble_sort(rendimientos, autos)
for i in range(len(autos)):
    print(f"{autos[i]}: {rendimientos[i]}")
    
 
