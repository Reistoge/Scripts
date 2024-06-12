# ID;Name;Sex;Age;Height;Weight;Team;noc_;Season;City;Sport;medal_
# 0  1     2   3   4      5      6    7    8      9    10   11
def intercambiar(lista,i,j):
    aux=lista[i]
    lista[i]=lista[j]
    lista[j]=aux
arch=open("olympics_v2.txt","r",encoding="utf-8")
Año_ciudad=arch.readline().strip()
linea=arch.readline().strip()
linea=arch.readline().strip()
jugadores_mayores=[]
jugadores_menores=[]
paises=[]
noc=[]
oros=[]
platas=[]
bronces=[]
jugadores=[]
edades=[]
ids=[]
while linea!="":
    
    linea=linea.split(";")
    identificador=int(linea[0])
    edad=float(linea[3])
    jugador=linea[1]
    if jugador not in jugadores:
        jugadores.append(jugador)
        ids.append(identificador)
        edades.append(edad)
    
    
        
    if linea[7] not in noc:
        
        noc.append(linea[7])
        paises.append(linea[6])
        
        if linea[11]=="Gold":
            oros.append(1)
            platas.append(0)
            bronces.append(0)
            
        elif linea[11]=="Silver":
            platas.append(1)
            oros.append(0)
            bronces.append(0)
            
        elif linea[11]=="Bronze":
            bronces.append(1)
            oros.append(0)
            platas.append(0)
        else:
            oros.append(0)
            platas.append(0)
            bronces.append(0)
    elif linea[7] in noc:
        if linea[11]=="Gold":
            oros[noc.index(linea[7])]+=1
        elif linea[11]=="Silver":
           platas[noc.index(linea[7])]+=1
        elif linea[11]=="Bronze":
            bronces[noc.index(linea[7])]+=1
    linea=arch.readline().strip()
for i in range(len(noc)-1):
   for j in range(i+1,len(noc),1):
           if oros[i]<oros[j] : 
               intercambiar(oros, i, j)
               intercambiar(platas, i, j)
               intercambiar(bronces, i, j)
               intercambiar(noc, i, j)
               intercambiar(paises, i, j)
           elif oros[i]==oros[j]:
               if platas[i]<platas[j]:
                   intercambiar(oros, i, j)
                   intercambiar(platas, i, j)
                   intercambiar(bronces, i, j)
                   intercambiar(paises, i, j)
                   intercambiar(noc, i, j)
               elif platas[i]==platas[j]:
                    if bronces[i]<bronces[j]:
                         intercambiar(oros, i, j)
                         intercambiar(platas, i, j)
                         intercambiar(bronces, i, j)
                         intercambiar(paises, i, j)
                         intercambiar(noc, i, j)               
print(f"Información de Juegos Olimpicos {Año_ciudad}")
print(f"Medallero")
print("Posición/Equipo/Oro/Plata/Bronce")
for i in range(0,15,1):
    print(f"{i+1} - {paises[i]} {oros[i]} {platas[i]} {bronces[i]}")
for i in range(0,len(edades)-1):
     for j in range(i+1,len(edades)):
         if edades[i]<edades[j]:
             intercambiar(edades,i,j)
             intercambiar(jugadores, i, j)
             intercambiar(ids,i,j)
         elif edades[i]==edades[j]:
             if ids[i]>ids[j]:
                 intercambiar(edades, i,j)
                 intercambiar(jugadores, i, j)
                 intercambiar(ids,i,j)
print("Competidores de Mayor Edad")
for i in range(0,5,1):
  print(f"{i+1} - ID: {ids[i]} Nombre: {jugadores[i]} Edad: {edades[i]} Años")    
for i in range(0,len(edades)-1):
     for j in range(i+1,len(edades)):
         if edades[i]>edades[j]:
             intercambiar(edades,i,j)
             intercambiar(jugadores, i, j)
             intercambiar(ids,i,j)
         elif edades[i]==edades[j]:
             if ids[i]>ids[j]:
                 intercambiar(edades, i,j)
                 intercambiar(jugadores, i, j)
                 intercambiar(ids,i,j)
         
print("Competidores de Menor Edad")
for i in range(0,5,1):
 print(f"{i+1} - ID: {str(ids[i])} Nombre: {jugadores[i]} Edad: {edades[i]} Años")