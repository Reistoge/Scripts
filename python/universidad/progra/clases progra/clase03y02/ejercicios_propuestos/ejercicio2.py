L=int(input("TAMAÑO DEL MUNDO DE JUANITO: "))
p=int(input("POSICION INICIAL DESDE DONDE SALTA JUANITO: "))
q=int(input("LONGITUD DE CADA SALTO: "))
n=int(input("CANTIDAD DE SALTOS QUE HARA JUANITO: "))

pasos_totales=(q*n)+p
while pasos_totales>L:
    pasos_totales=pasos_totales-L
    
print(pasos_totales)


