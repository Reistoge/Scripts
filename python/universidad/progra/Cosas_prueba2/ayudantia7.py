# ayudantia 7

lista1 = [10, 20, 24, 40,18,18]
lista2 = [14, 18, 30, 38,20,20]

diferencia_menor=lista1[0]
indice_menor=0
for i in range(0, len(lista1),1):
    diferencia=lista1[i]-lista2[i]
    if diferencia<0:
        diferencia=diferencia*-1
    if diferencia<diferencia_menor:
        diferencia_menor=diferencia
        indice_menor=i
        
        
print(diferencia_menor)

        
for i in range(0,len(lista1),1):
    diferencia=lista1[i]-lista2[i]
    if diferencia<0:
        diferencia=diferencia*-1
        
    if diferencia==diferencia_menor:
        print(i)
        
   
     
