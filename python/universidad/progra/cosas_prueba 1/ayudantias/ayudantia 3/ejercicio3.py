arch=open("ejercicio 3.txt","r",encoding="utf-8")
linea=arch.readline().strip()
 
while linea!="":
    n=int(linea.split(",")[0])
    ciudad=linea.split(",")[len(linea.split(","))-1]
    print(n,ciudad)
    linea=arch.readline().strip()
    
        
    
    
    