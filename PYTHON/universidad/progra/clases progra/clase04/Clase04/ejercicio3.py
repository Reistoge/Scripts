arch=open("ejercicio3.txt","r",encoding="utf-8")
n=0
n_mayor=0
edad_mayor=0
ciudad_mayor=""
promedio_cada_una=""
nombre_e_m=""
edades_entre_25y30=0
empleados_totales=0
nombre_33=""
ponderacion_menor=100000
linea=arch.readline()
while linea!="":
    
    ciudad=linea.split(",")[0]
    n=int(linea.split(",")[1])
    empleados_totales+=n
    if n>n_mayor:
        n_mayor=n
        ciudad_mayor=ciudad
    
    edad_t_su=0
    for i in range(n):
        linea_p=arch.readline()
        nombre=linea_p.split(",")[0]
        edad=int(linea_p.split(",")[1])
        edad_t_su+=edad
        if edad>edad_mayor:
            edad_mayor=edad
            nombre_e_m=nombre
        if edad>=25 and edad<=30:
            edades_entre_25y30+=1
        if edad==33:
            nombre_33=nombre
        
    promedio=round(edad/n,3)  
    
    ponderacion=round(n*10+promedio*0.5,3)
    promedio_cada_una+="\n"+ciudad+" "+str(promedio)+" "+str(ponderacion)
    if ponderacion_menor>ponderacion:
        ponderacion_menor=ponderacion
    linea=arch.readline()

porcentaje=100*(edades_entre_25y30/empleados_totales)
print(ciudad_mayor,n_mayor, nombre_e_m, ciudad_mayor,promedio_cada_una)
print(porcentaje, nombre,ponderacion_menor)
 
 
    