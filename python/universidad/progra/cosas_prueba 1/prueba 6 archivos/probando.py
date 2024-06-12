arch=open("bruh.txt","r",encoding="utf-8")

linea=arch.readline()
a=""
contador = 0
a=""
while linea!="":
    if linea.strip()!="":
        a.append(linea)
    else:
        contador+=1
        
    if contador==2:
        contador = 0
        a=["",""]
        
    print(contador)
    print(linea)
    linea=arch.readline()
    
        
    
    
        
        
    
        
        