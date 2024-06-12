arch=open("ejercicio 2_variante.txt", "r", encoding="utf-8")
n=arch.readline()
n=int(n)
for i in range(0,int(n),1):
    linea=arch.readline()
  
suma=0
## acaba el for
dinero=arch.readline()
while dinero!="":
    
    numero=int(dinero)
    suma+=numero
    dinero=arch.readline()
    
print("la vaquita es de:",str(suma)+"$.")
