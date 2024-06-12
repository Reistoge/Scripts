arch1=open("texto2.txt","r",encoding="utf-8")


linea=arch1.readline().strip()
lista=[]
while linea!="":
    lista.append(float(linea))
    linea=arch1.readline().strip()

    
def calcular(operacion,lista):
    if operacion=="minimo":
        minimo=lista[0]
        for i in range(len(lista)):
            if lista[i]<minimo:
                minimo=lista[i]
        return minimo
    
    elif operacion=="maximo":
        maximo=lista[0]
        for i in range(len(lista)):
            if lista[i]>maximo:
                maximo=lista[i]
        return maximo
    
        
    elif operacion=="promedio" or operacion=="suma":
        sum=0
        for i in range(len(lista)):
            sum+=lista[i]
        if operacion=="promedio":
            return sum/len(lista)
            
        
        elif operacion=="suma":
            return sum

promedio=(calcular("promedio",lista))


# calculamos numeros entre medio del promedio.
print(promedio*0.9,promedio*1.1)
numeros_entre=[]
for numero in lista:
    if (numero >promedio*0.9) and (numero<promedio*1.1):
        numeros_entre.append(numero)
print(numeros_entre)