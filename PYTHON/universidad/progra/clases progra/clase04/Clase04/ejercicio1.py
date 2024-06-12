arch=open("ejercicio1.txt","r",encoding="utf-8")
numero=arch.readline().strip()
total=0
contador=0
maximo=0
minimo=int(numero)
while numero!="":
    print(numero)
    total+=int(numero)
    contador+=1
    if int(numero)>=maximo:
        maximo=int(numero)
    if int(numero)<=minimo:
        minimo=int(numero)
    numero=arch.readline().strip()
    
    
print(total, contador, maximo, minimo )