def max_triple(lista):

    mayor1=0
    mayor2=0
    mayor3=0
    for i in range(0,len(lista),1):
        if lista[i]>mayor1:
            mayor1=lista[i]
        
        
    for i in range(0,len(lista),1):
        if lista[i]>mayor2 and lista[i]!=mayor1:
            mayor2=lista[i]
        
        
    for i in range(0,len(lista),1):
        if lista[i]>mayor3 and lista[i] not in[mayor1, mayor2]:
            mayor3=lista[i]
        
    return[mayor1,mayor2,mayor3]


arch=open("numeros.txt","r",encoding="utf-8")
lista_numeros=[]
linea=arch.readline().strip()
while linea!="":
    lista_numeros.append(int(linea))
    
    linea=arch.readline().strip()


print(max_triple(lista_numeros))

