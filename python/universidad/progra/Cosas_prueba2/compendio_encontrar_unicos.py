def leerNombres(archivo):
    lista=[]
    arch=open(archivo,"r")
    linea=arch.readline().strip()
    while linea!="":
        lista.append(linea) 
        linea =arch.readline().strip()
    arch.close()
    return lista
    
def escribirResultados(unicos,frecuencias):
    for i in range(0,len(frecuencias)):
        print(unicos[i],frecuencias[i])
    
def determinarUnicos(lista,unicos,frecuencias):
    for n in nombres:
        if esta(n,nombresUnicos):
            i=indice(n,nombresUnicos)
            frecuencias[i]=frecuencias[i]+1
        else:
            nombresUnicos.append(n)
            frecuencias.append(1)
def esta(s,lista):
    for i in range(0,len(lista)):
        if s==lista[i]:
            return True
    return False

def indice(s, lista):
    for i in range(0,len(lista)):
        if s==lista[i]:
            return i
    return -1



#lee los nombres desde el archivo (esta lista tiene duplicados!)
nombres=leerNombres("texto1.txt")


#estas son las dos listas donde se guardaran los nombres 
#unicos y las frecuencias correspondientes 
nombresUnicos =[]
frecuencias =[]


#este procedimiento realizara el proceso de identificar 
#los nombres unicos y contar las veces que se repiten
determinarUnicos(nombres,nombresUnicos,frecuencias)

# se escriben los resultados por pantalla 
escribirResultados(nombresUnicos,frecuencias)

##la lista de nombres unicos con "leer nombres" sirve para poder verificar cada nombre de la lista general.
## determinar_unicos: recorres la lista nombres(contiene todos) y por cada nombre iterado (for) se verifica si esta dentro de la lista de unicos, si este se encuentra
## entonces con "indice"  buscas el indice de la palabra en la lista nombre unico para poder guardarla en el indice de frecuencias.
 ## ya que tienen el mismo len.



