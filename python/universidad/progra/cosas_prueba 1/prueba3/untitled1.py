archivo=input("archivo: ")
arch=open(archivo,"r",encoding="utf-8")
linea=arch.readline().strip()
nombres=[]

while linea!="":
    nombres.append(linea)
    linea=arch.readline().strip()
arch.close()
nombres_unicos=[]
for i in nombres:
    print(i)
# for i in range(0,len(nombres),1):
#     if nombres[i] not in nombres_unicos:
#         nombres_unicos.append(nombres[i])
#     elif nombres[i] in nombres_unicos:
#         nombres_unicos.remove(nombres[i])
 


    

