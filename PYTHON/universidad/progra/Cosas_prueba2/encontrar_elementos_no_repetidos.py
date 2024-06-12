arch1=open("texto.txt","r",encoding="utf-8")


linea=arch1.readline().strip()
lista=[]
lista_unicos=[]
contador=0
while linea!="":
    
    lista.append(linea)
    linea=arch1.readline().strip()

    

for i in range(0,len(lista)):
    repetidos=0
    for j in range(0,len(lista)):
        if lista[i]==lista[j]:
            repetidos+=1
    if repetidos==1:
        lista_unicos.append(lista[i])
            


print(lista_unicos)