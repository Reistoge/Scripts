
def calcular_medallas(lista,_pais):
    _medallas=[0,0,0]

    for i in range(0,len(lista)):
        if "Gold" in lista[i] and _pais in lista[i]:
            _medallas[0]+=1
        elif "Silver" in lista[i] and _pais in lista[i]:
            _medallas[1]+=1
        elif "Bronze" in lista[i] and _pais in lista[i]:
            _medallas[2]+=1
    return _medallas

def deportista_mayor_y_menor(lista,_pais):
    _edad_mayor=0
    _edad_menor=200
    _nombre_edad_mayor=""
    _nombre_edad_menor=""
    _deportistas=[]
    for i in range(0,len(lista)):
        
        if float(lista[i][3])>_edad_mayor and _pais in lista[i]:
            _edad_mayor=float(lista[i][3])
            _nombre_edad_mayor=lista[i][1]
        if float(lista[i][3])<_edad_menor and _pais in lista[i]:
             _edad_menor=float(lista[i][3])
             _nombre_edad_menor=lista[i][1] 
             
    _deportistas.append(_nombre_edad_menor)
    _deportistas.append(_edad_menor)
    _deportistas.append(_nombre_edad_mayor)
    _deportistas.append(_edad_mayor)
    return _deportistas

def promedio(cantidad,total):
    
    return round(cantidad/(total),2)
def calc_promedio_estatura_y_peso(lista,_pais):
    estatura_hombres=0
    estatura_mujeres=0
    peso_mujeres=0
    peso_hombres=0
    _promedios=[]
    mujeres=0
    hombres=0
    for i in range(0,len(lista)):
        if _pais in lista[i]:
            if lista[i][2]=="M":
                hombres+=1
                estatura_hombres+=float(lista[i][4])
                peso_hombres+=float(lista[i][5])
            
            if lista[i][2]=="F":
                mujeres+=1
                estatura_mujeres+=float(lista[i][4])
                peso_mujeres+=float(lista[i][5])
 
    _promedios.append(promedio(estatura_hombres,hombres))
    _promedios.append(promedio(estatura_mujeres,mujeres))
    _promedios.append(promedio(peso_hombres,hombres))
    _promedios.append(promedio(peso_mujeres,mujeres))
    
    return _promedios
    
def imprimir_datos(_ciudad_ano,_pais,info):
    print(f"Información de Juegos Olimpicos {_ciudad_ano.capitalize()}")
    print(f"Datos Sobre Chile")
    medallas=calcular_medallas(info, _pais)
    deportistas=deportista_mayor_y_menor(info, _pais)
    promedios=calc_promedio_estatura_y_peso(info, _pais)
    print(f"Cantidad Medallas de Oro: {medallas[0]}")
    print(f"Cantidad Medallas de Plata: {medallas[1]}")
    print(f"Cantidad Medallas de Bronce: {medallas[2]}")
    print(f"El deportista chileno de Menor edad fue: {deportistas[0]} con {deportistas[1]} años")
    print(f"El deportista chileno de Mayor edad fue: {deportistas[2]} con {deportistas[3]} años")
    print(f"Promedio de Estatura en Hombres fue: {promedios[0]} cms.")
    print(f"Promedio de Estatura en Mujeres fue: {promedios[1]} cms.")
    print(f"Promedio de Peso en Hombres fue: {promedios[2]} kgs.")
    print(f"Promedio de Peso en Mujeres fue: {promedios[3]} kgs.")
    
arch=open("olympics.txt",encoding="utf-8")
ciudad_ano=arch.readline().strip()
formato=arch.readline().strip()
# ID;Name;Sex;Age;Height;Weight;Team;NOC;Season;City;Sport;Medal
info=[]
linea=arch.readline().strip()
while linea!="":
    datos=linea.split(";")
   
    info.append(datos)
    linea=arch.readline().strip()
    
imprimir_datos(ciudad_ano, "CHI", info)  