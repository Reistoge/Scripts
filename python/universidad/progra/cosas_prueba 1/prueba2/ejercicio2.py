arch=open("payroll -original.txt","r",encoding="utf-8")
linea=arch.readline().strip().lower()
trabajadores_totales=0
sueldo_mas_alto_gerente=0
nombre_gerente_mas=""
sueldo_mas_alto_vendedor=0
nombre_vendedor_mas=""
utilidad_mayor=0
nombre_ciudad_u_mayor=""
nombre_ciudad_u_menor=""
utilidad_menor=0
prioridad_baja_problemas=0
prioridad_baja=0
gerentes=0
gerente_mujeres=0
while linea!="":
    partes=linea.split("-")
    ciudad=partes[0]
    ventas=float(partes[1])
    cantidad_empleados=int(partes[2])
    trabajadores_totales+=cantidad_empleados
    prioridad=partes[3]
    sueldo_anuales=0
    for i in range(cantidad_empleados):
        linea=arch.readline().strip().lower()
        partes2=linea.split(";")
        NombreEmpleado=partes2[0]
        Sexo=partes2[1]
        SueldoAnual=float(partes2[2])
        edad=int(partes2[3])
        cargo=partes2[4]
        sueldo_anuales+=SueldoAnual
        if cargo=="gerente":
            gerentes+=1
            if SueldoAnual > sueldo_mas_alto_gerente:
                sueldo_mas_alto_gerente=SueldoAnual
                nombre_gerente_mas=NombreEmpleado
                
        if cargo=="gerente" and Sexo=="f":
            gerente_mujeres+=1
                
                
        elif cargo=="vendedor":
            if SueldoAnual >sueldo_mas_alto_vendedor:
                sueldo_mas_alto_vendedor=SueldoAnual
                nombre_vendedor_mas=NombreEmpleado
        
                
            
    if prioridad=="baja":
        prioridad_baja+=1        
            
    utilidad=ventas-1.1*sueldo_anuales
    if utilidad<=0:
        print(f"{ciudad} {prioridad} Pérdidas. Se recomienda cerrar")
        if prioridad=="baja":
            prioridad_baja_problemas+=1
            
    elif utilidad >0:
        print(f"{ciudad} {prioridad} Utilidades. Se recomienda mantener")
    if utilidad>utilidad_mayor:
        utilidad_mayor=utilidad
        nombre_ciudad_u_mayor=ciudad
        # asignamos el valor màs grande encontrado a utilidad menor para tener un valor siempre grande.
        utilidad_menor=utilidad_mayor
    if utilidad<utilidad_menor:
        utilidad_menor=utilidad
        nombre_ciudad_u_menor=ciudad
        
   
        
        
        
    linea=arch.readline().strip().lower()
        
print(f"2) El total de trabajadores es {trabajadores_totales}")
print(f"3.1) El Gerente con sueldo más alto es {nombre_gerente_mas} con {sueldo_mas_alto_gerente}")
print(f"3.2) El Vendedor con el sueldo más alto es {nombre_vendedor_mas} con {sueldo_mas_alto_vendedor}")
print(f" 4.1) La sucursal con menor utilidad es {nombre_ciudad_u_menor} con {utilidad_menor}")
print(f"4.2) La sucursal con mayor utilidad es {nombre_ciudad_u_mayor} con {utilidad_mayor}")
print(f"5) El porcentaje de sucursales de prioridad baja con problemas es de un {(prioridad_baja_problemas/prioridad_baja)*100}%")
print(f"6) El porcentaje de gerentes mujeres es de {(gerente_mujeres/gerentes)*100}%")






