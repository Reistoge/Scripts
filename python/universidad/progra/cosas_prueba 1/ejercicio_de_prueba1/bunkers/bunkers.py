opcion=input("Ingrese A para Norte o B para Sur: ").lower()
while opcion!="a" and opcion!="b" and opcion!="fin":
    #volvemos a preguntar reasignando a opcion
    opcion=input("Error, Ingrese A para Norte o B para sur: ").lower()

while opcion!="fin":
        
    if opcion=="a":
        archA=open("A.txt","r",encoding="utf-8")
        lineaA=archA.readline().strip()
        mayor_factor_A=0
        bunker_convenienteA=["",0.0,0.0]
        refugios_habitables_A=0
        refugios_inhabitables_A=0
        while lineaA!="":
            nombre_refugio=lineaA.split(",")[0]
            distancia=int(lineaA.split(",")[1])-200
            capacidad=int(lineaA.split(",")[2])
            suministros=int(lineaA.split(",")[3])
            radiacion=lineaA.split(",")[4].lower()
            actividad=lineaA.split(",")[5].lower()
            # analizamos los datos de cada linea
            if capacidad>=20 and radiacion=="protegido" and actividad=="true":
                # chekeamos el factor de conveniencia de cada bunker por linea
                print("refugio ",nombre_refugio," es conveniente para sumistros" )
                # refugio mas conveniente
                factor_conveniencia_A=(1800/distancia)+((12*suministros/90))
                print(factor_conveniencia_A)
                if factor_conveniencia_A>mayor_factor_A and radiacion=="protegido":
                    # almacenamos el bunker mas conveniente
                    mayor_factor_A=factor_conveniencia_A
                    bunker_convenienteA[0]=nombre_refugio
                    bunker_convenienteA[1]=factor_conveniencia_A
                    bunker_convenienteA[2]=distancia
            if capacidad>=30 and radiacion=="protegido":
                refugios_habitables_A+=1
            elif capacidad<30 or radiacion!="protegido":
                refugios_inhabitables_A+=1
                    
                  
            lineaA=archA.readline().strip()
        totalA=refugios_habitables_A+refugios_inhabitables_A
        porcentajeA=round((100*(refugios_inhabitables_A/totalA)),3)
        print("1) El refugio más conveniente es ",bunker_convenienteA[0]," con un factor de ",str(bunker_convenienteA[1]))
        print("2) Hay",refugios_habitables_A," refugios habitables")
        print("3) Hay ",refugios_inhabitables_A," refugios inhabitables equivalentes a ",porcentajeA," del sector analizado")
        n=0
        for i in range(1,51,10):
            n+=1
            distancia_bunker_conveniente=bunker_convenienteA[2]
            horas=bunker_convenienteA[2]//i
            minutos=(bunker_convenienteA[2]/i-bunker_convenienteA[2]//i)*60
            print(str(n)+") para llegar a", bunker_convenienteA[0],"faltan ",str((horas))," horas y ",str(round(minutos))," minutos a ",i," nudos")
            
              
    if opcion=="b":
        archB=open("b.txt","r",encoding="utf-8")
        lineaB=archB.readline().strip()
        mayor_factor_B=0
        bunker_convenienteB=["",0.0,0.0]
        refugios_habitables_B=0
        refugios_inhabitables_B=0
        while lineaB!="":
            nombre_refugio=lineaB.split(",")[0]
            distancia=int(lineaB.split(",")[1])+200
            capacidad=int(lineaB.split(",")[2])
            suministros=int(lineaB.split(",")[3])
            radiacion=lineaB.split(",")[4].lower()
            actividad=lineaB.split(",")[5].lower()
            # analizamos los datos
            if capacidad>=20 and radiacion=="protegido" and actividad=="true":
                print("refugio ",nombre_refugio," es conveniente para sumistros" )
                # refugio mas conveniente
                factor_conveniencia_B=(1800/distancia)+((12*suministros/90))
                
                if factor_conveniencia_B>mayor_factor_B and radiacion=="protegido":
                    mayor_factor_B=factor_conveniencia_B
                    bunker_convenienteB[0]=nombre_refugio
                    bunker_convenienteB[1]=factor_conveniencia_B
                    bunker_convenienteB[2]=distancia
            if capacidad>=30 and radiacion=="protegido":
                refugios_habitables_B+=1
            elif capacidad<30 or radiacion!="protegido":
                refugios_inhabitables_B+=1
                 
            
            # calculo de nudos 
            
        
                
                
            lineaB=archB.readline().strip()
        totalB=refugios_habitables_B+refugios_inhabitables_B
        porcentajeB=round((100*(refugios_inhabitables_B/totalB)),3)
        print("informacion en B")
        print("1) El refugio más conveniente es ",bunker_convenienteB[0]," con un factor de ",str(bunker_convenienteB[1]))
        print("2) Hay",refugios_habitables_B," refugios habitables")
        print("3) Hay ",refugios_inhabitables_B," refugios inhabitables equivalentes a ",porcentajeB," del sector analizado")
        n=0
        for i in range(1,51,10):
            n+=1
            distancia_bunker_conveniente=bunker_convenienteB[2]
            horas=bunker_convenienteB[2]//i
            minutos=(bunker_convenienteB[2]/i-bunker_convenienteB[2]//i)*60
            print(str(n)+") para llegar a", bunker_convenienteB[0],"faltan ",str((horas))," horas y ",str(round(minutos))," minutos a ",i," nudos")
            
        
    opcion=input("Ingrese A para Norte o B para Sur: ")
        
        


