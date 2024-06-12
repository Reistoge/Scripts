def se_encuentra(lista,elemento):
    for k in range(0,len(lista)):
        if lista[k]==elemento:
            return True
    else:
        return False
            
arch1=open("texto1.txt","r",encoding="utf-8")


linea=arch1.readline().strip()
lista=[]
contador=0
while linea!="":
     lista.append(linea)
     linea=arch1.readline().strip()
 
lista_nombres=[]
lista_contadores=[]


for i in range(len(lista)):
    if not se_encuentra(lista_nombres,lista[i]):
        lista_nombres.append(lista[i])
        repetidos=1
        for j in range(0,len(lista)):
            if lista[i]==lista[j] and i!=j:
                repetidos+=1
        lista_contadores.append(repetidos)
 
        
    
print(lista_nombres,len(lista_nombres))
print(lista_contadores,len(lista_contadores))