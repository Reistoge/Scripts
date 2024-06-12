#  3 cables Si no hay cable rojo, corte el segundo 
# cable. Si no, en caso de que el último cable sea blanco,
#  corte el último cable. Si no, en caso de que el primer y 
#  segundo cable sean azules, corte el segundo cable azul. Si no, corte el último cable.

#  4 Cables Si hay más de un cable rojo corte el último cable. 
# Si no, en caso de que el último cable sea amarillo y no haya cables rojos
#  corte el primer cable. Si no, en caso de que haya exactamente un cable rojo,
#  corte el segundo cable. Si no, en caso de que el segundo y el tercer cable sean de color amarillo,
#  corte el último cable. Si no, corte el tercer cable.

# 5 Cables Si el último cable es negro corte el cuarto cable. Si no, si el 
# tercer cable es rojo y hay más de un cable amarillo, corte el tercer cable. 
# Si no, en caso de no haber cables negros, corte el segundo cable. Si no, corte el primer cable


arch=open("dispositivos.txt","r",encoding="utf-8")
linea=arch.readline().strip().lower()
contador=1
while linea!="":
    cables=[]
    partes=linea.split(",")
    n_cables=int(partes[0])
    if n_cables == 3:
        for i in range(1,n_cables+1,1):
            cables.append(partes[i])
            
        if "rojo" not in cables:
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el segundo cable ({cables[1].capitalize()})")
            # cortar segundo cable
            
        elif cables[-1]=="blanco":
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el tercer cable ({cables[-1].capitalize()})")
            # cortar ultimo cable
        elif cables[0] =="azul" and cables[1]=="azul":
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el segundo cable ({cables[1].capitalize()})")
            # cortar el segundo cable azul
        else:
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Corte el tercer cable ({cables[-1].capitalize()})")
            # cortar ultimo cable
        
    elif n_cables ==4:
        cables_rojos=0
        for i in range(1,n_cables+1,1):
            cables.append(partes[i])
        for i in range(0,n_cables,1):
            if cables[i]=="rojo":
                cables_rojos+=1
        if cables_rojos==1:
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el segundo cable ({cables[1].capitalize()})")
        # corte el segundo cable
        elif cables_rojos>1:
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el cuarto cable ({cables[-1].capitalize()})")
        # cortar ultimo cable
        elif cables[-1] =="amarillo" and "rojo" not in cables:
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el primer cable ({cables[0].capitalize()})")
        # cortar primer cable
        elif cables[1]=="amarillo" and cables[2]== "amarillo":
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el último/cuarto cable ({cables[-1].capitalize()})")
        # Si no, en caso de que el segundo y el tercer cable sean de color amarillo,
        #  corte el último cable.
        else:
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el tercer cable ({cables[2].capitalize()})")
            # Si no, corte el tercer cable.
            
        
    # 5 Cables Si el último cable es negro corte el cuarto cable. Si no, si el 
    # tercer cable es rojo y hay más de un cable amarillo, corte el tercer cable. 
    # Si no, en caso de no haber cables negros, corte el segundo cable. Si no, corte el primer cable
        
        
    elif n_cables==5:
        cables_amarillos=0
        for i in range(1,n_cables+1,1):
            cables.append(partes[i])
        for i in range(0,n_cables,1):
            if cables[i]=="amarillo":
                 cables_amarillos+=1
        
        if cables[-1]=="negro":
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el cuarto cable ({cables[3].capitalize()})")
            # cortar el cuarto cable
        elif cables[2]=="rojo" and cables_amarillos>1:
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el tercer cable ({cables[2].capitalize()})")
            # cortar tercer cable
        elif "negro" not in cables:
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el segundo cable ({cables[1].capitalize()})")
            # cortar segundo cable
        else:
            print(f"Dispositivo {contador} tiene {n_cables} cables")
            print(f"Cortar el primer cable ({cables[0].capitalize()})")
            # cortar primer cable
        
            
            
    linea=arch.readline().strip().lower()
    contador+=1
print(f"Se analizaron {contador-1} dispositivos")
        
   