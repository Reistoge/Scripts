def texto_lista(nombre_arch):
    arch=open(nombre_arch)
    linea=arch.readline().strip().lower()
    lista=[]
    while linea!="":
        lista.append(linea)
        linea=arch.readline().strip().lower()
        
    return lista


lista1=texto_lista("texto.txt")
lista2=texto_lista("texto1.txt")
lista3=[]
for nombre in lista1:
   if nombre in lista2:
       lista3.append(nombre)
      
lista4=[]
for nombre in lista3:
    if nombre not in lista4:
        lista4.append(nombre)
        
        
print(lista4)