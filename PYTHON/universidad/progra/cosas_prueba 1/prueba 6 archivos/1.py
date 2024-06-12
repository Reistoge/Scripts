
def obtenerNombresUnicos(lista):
    unicos=[]
    for s in lista:
        if not esta(s, unicos):
            unicos.append(s)
    return unicos
    
def esta(palabra,lista):
    for s in lista:
        if s==palabra:
            return True
    return False
    
    
def obtener_nombres_unicos(lista):
    lista_temp=[]
    lista_unica=[]
    for i in lista:
        lista_temp.append(i)
    for i in range(0,len(lista_temp),1):
        for j in range(0,len(lista_temp),1):
            if lista_temp[i]==lista[j] and i!=j:
                lista_temp[i]=0
        
    for i in range(0,len(lista),1):
        if lista_temp[i]!=0:
            lista_unica.append(lista_temp[i])
            
            
    return lista_unica
    
    
    
lista=["a","a","a","b","c","e","d","b"]
print(obtener_nombres_unicos(lista))




lista1=["a","b","c","v","r",]














