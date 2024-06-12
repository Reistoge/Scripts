# ID;Name;Sex;Age;Height;Weight;Team;noc_;Season;City;Sport;medal_
# 0  1     2   3   4      5      6    7    8      9    10   11

def intercambiar(lista,i,j):
    aux=lista[i]
    lista[i]=lista[j]
    lista[j]=aux

def medallero(n_archivo):
    arch=open(n_archivo,"r",encoding="utf-8")

    linea=arch.readline().strip()
    Año_ciudad=linea
    linea=arch.readline().strip()
    linea=arch.readline().strip()
    paises_=[]
    oros_=[]
    platas_=[]
    bronces_=[]
    info_=[]
    teams_=[]
    ids_=[]
    
   
    while linea!="":
        
        linea=linea.split(";")
        info_.append(linea)
         
        team_=linea[6]
        noc_=linea[7]
        
        medal_=linea[11]
        
        
        if noc_ not in paises_:
            paises_.append(noc_)
            teams_.append(team_)
             
            if medal_=="Gold":
                oros_.append(1)
                platas_.append(0)
                bronces_.append(0)
            elif medal_=="Silver":
                platas_.append(1)
                oros_.append(0)
                bronces_.append(0)
            elif medal_=="Bronze":
                bronces_.append(1)
                oros_.append(0)
                platas_.append(0)
            else:
                bronces_.append(0)
                oros_.append(0)
                platas_.append(0)
                
                
        elif noc_ in paises_:
            if medal_=="Gold":
                oros_[paises_.index(noc_)]+=1
            elif medal_=="Silver":
                platas_[paises_.index(noc_)]+=1
                
            elif medal_=="Bronze":
                bronces_[paises_.index(noc_)]+=1
                
            
        
        linea=arch.readline().strip()
        
    for i in range(0,len(paises_),1):
        for j in range(i+1,len(paises_),1):
            if oros_[i]<=oros_[j]:
                if oros_[i]<oros_[j] : 
                    intercambiar(oros_, i, j)
                    intercambiar(platas_, i, j)
                    intercambiar(bronces_, i, j)
                    intercambiar(paises_, i, j)
                    intercambiar(teams_, i, j)
                elif oros_[i]==oros_[j] and platas_[i]<platas_[j]:
                    intercambiar(oros_, i, j)
                    intercambiar(platas_, i, j)
                    intercambiar(bronces_, i, j)
                    intercambiar(paises_, i, j)
                    intercambiar(teams_, i, j)
                elif  oros_[i]==oros_[j]  and platas_[i]==platas_[j] and bronces_[i]<bronces_[j]:
                        intercambiar(oros_, i, j)
                        intercambiar(platas_, i, j)
                        intercambiar(bronces_, i, j)
                        intercambiar(paises_, i, j)
                        intercambiar(teams_, i, j)
                        
                        
                # esta parte daba problemas
                elif  oros_[i]==oros_[j]  and platas_[i]==platas_[j] and bronces_[i]==bronces_[j] and teams_[i]>=teams_[j]:
                            intercambiar(oros_, i, j)
                            intercambiar(platas_, i, j)
                            intercambiar(bronces_, i, j)
                            intercambiar(paises_, i, j)
                            intercambiar(teams_, i, j)
            
                          
                    

                
    # print(paises_,oros_,platas_,bronces_,teams_) 
    print(f"Información de Juegos Olimpicos {Año_ciudad}")
    print(f"Medallero")
    print("Posición/Equipo/Oro/Plata/Bronce")
    for i in range(0,15,1):
        print(f"{i+1} - {teams_[i]} {oros_[i]} {platas_[i]} {bronces_[i]}")
        
    return info_
    


def mayores(lista):
    nombres_mayores=[" "," "," "," "," "]
    ids_mayores=[" "," "," "," ",""]
    edades_mayores=["","","","",""]
    for i in range(5):
       
        nombre_mayor=""
        edad_mayor=0
        id_mayor=0
        for j in range(len(lista)):
            ID_=int(lista[j][0])
            name_=lista[j][1]
             
            age_=float(lista[j][3])
            
            if float(age_)> float(edad_mayor) and name_ not in nombres_mayores:   
                edad_mayor=age_
                nombre_mayor=name_
                id_mayor=ID_
                
    
                    
                        


                
        edades_mayores[i]=edad_mayor
        ids_mayores[i]=id_mayor
        nombres_mayores[i]=nombre_mayor
        
    for i in range(0,len(nombres_mayores),1):
        for j in range(i+1,len(nombres_mayores),1):
             if edades_mayores[i]<edades_mayores[j]:
                 intercambiar(edades_mayores, i, j)
                 intercambiar(ids_mayores, i, j)
                 intercambiar(nombres_mayores, i, j)
            #esta parte daba problemas 
             if edades_mayores[i]==edades_mayores[j] and ids_mayores[i]>ids_mayores[j]:
                 intercambiar(edades_mayores, i, j)
                 intercambiar(ids_mayores, i, j)
                 intercambiar(nombres_mayores, i, j)   
                
         
    print("Competidores de Mayor Edad")
    for i in range(0,5,1):
        print(f"{i+1} - ID: {ids_mayores[i]} Nombre: {nombres_mayores[i]} Edad: {edades_mayores[i]} Años")
        
        
def menores(lista):
    nombres_menores=[" "," "," "," "," "]
    ids_menores=[" "," "," "," "," "]
    edades_menores=[" "," "," "," "," "]
    for i in range(5):
       
        nombre_menor=""
        edad_menor=100
        id_menor=0
        for j in range(len(lista)):
            ID_=lista[j][0]
            name_=lista[j][1]
          
            age_=lista[j][3]
            
            if float(age_)<float(edad_menor) and name_ not in nombres_menores:   
                edad_menor=age_
                nombre_menor=name_
                id_menor=ID_
                
            edades_menores[i]=edad_menor
            ids_menores[i]=id_menor
            nombres_menores[i]=nombre_menor
            
    for i in range(0,len(nombres_menores),1):
        for j in range(i+1,len(nombres_menores),1):
             if edades_menores[i]>edades_menores[j]:
                 intercambiar(edades_menores, i, j)
                 intercambiar(ids_menores, i, j)
                 intercambiar(nombres_menores, i, j)
                
            #esta parte daba problemas 

             if edades_menores[i]==edades_menores[j] and ids_menores[i]>ids_menores[j]:
                 intercambiar(edades_menores, i, j)
                 intercambiar(ids_menores, i, j)
                 intercambiar(nombres_menores, i, j)   
                
                
         
    print("Competidores de Menor Edad")
    for i in range(0,5,1):
        print(f"{i+1} - ID: {ids_menores[i]} Nombre: {nombres_menores[i]} Edad: {edades_menores[i]} Años")
            
 
    

todo=medallero("olympics_v2.txt")
mayores(todo)
menores(todo)
            

          


 
