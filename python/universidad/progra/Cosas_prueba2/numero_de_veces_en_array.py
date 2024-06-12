arch1=open("texto1.txt","r",encoding="utf-8")


linea=arch1.readline().strip()
lista=[]
contador=0
while linea!="":
     lista.append(linea)
     linea=arch1.readline().strip()
print(lista)
lista_unicos=[]
 
for i in range(len(lista)):
    repetidos=1
    if lista[i] not in lista_unicos:
        lista_unicos.append(lista[i])
        lista_unicos.append(repetidos)
        
    for j in range(len(lista)):
        if lista[i]==lista[j] and i!=j:
            repetidos+=1
    for k in range(0,len(lista_unicos)):
        if lista_unicos[k]==lista[i]:
            lista_unicos[k+1]=repetidos
            
print(lista_unicos)
    
            