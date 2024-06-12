tiempo_calidad_normal=30
tiempo_calidad_alta=46
filamento=330.0

def obtener_filamentos():
    arch1=open("config.txt","r",encoding="utf-8")
    arch1.readline()
    linea=arch1.readline().strip().lower()
    materiales=[]
    while linea!="":
        partes=linea.split(",")
        material=partes[0]
        materiales.append(material)
        linea=arch1.readline().strip().lower()
    return materiales
    arch1.close()
        
    
def obtener_precio(material_solicitado):
    material_solicitado=material_solicitado.lower()
    arch1=open("config.txt","r",encoding="utf-8")
    arch1.readline()
    linea=arch1.readline().strip().lower()
    while linea!="":
        partes=linea.split(",")
        material=partes[0]
        precio=partes[1]
        if material==material_solicitado:
            return float(precio)
        linea=arch1.readline().strip().lower()
    arch1.close()


def obtener_tiempo(minutos):
    if minutos>=1440:
        dias=minutos//(60*24)
        horas_no_formateadas=minutos%(60*24)
        horas=horas_no_formateadas//60
        minutos=horas_no_formateadas%60
        
        
        print(f"{round(dias)} dias {round(horas)} horas {round(minutos)} minutos")
    
    elif minutos<1440 and minutos>=60:
        horas=minutos//60
        minutos=(minutos%60)
        print(f"{round(horas)} horas {round(minutos)} minutos")
    elif minutos<60:
        print(f"{round(minutos)} minutos")
    
    

arch1=open("config.txt","r",encoding="utf-8")
pedidos=int(arch1.readline())
numero_piezas=0
n_alta_calidad=0
n_calidad_normal=0
materiales=obtener_filamentos()
suma_materiales=[]
precio_total=0
for i in range(len(materiales)):
    suma_materiales.append(0)
for i in range(pedidos):
    contador_archivo=i+1
    nombre_archivo="P"+str(contador_archivo)+".txt"
    pedido=open(nombre_archivo,"r",encoding="utf-8")
    linea=pedido.readline().strip().lower()
    # id_pedido*metros*calidad*material
    # aqui leera cada pedidos p1p2 p3 p4 p...
    pedido_tiempo_mayor=""
    tiempo_pedido_mayor=0
    pedido_tiempo_menor=""
    tiempo_pedido_menor=1000000000.0
    
    tiempo_total_minutos_pedido=0
    
    while linea!="":
        
        numero_piezas+=1
        partes=linea.split("*")
        id_pedido=partes[0]
        metros=float(partes[1])
        calidad=partes[2]
        material=partes[3]
        for i in range(0,len(materiales),1):
            
            if materiales[i]==material:
                suma_materiales[i]+=metros
        if calidad=="alta":
            n_alta_calidad+=1
            tiempo_minutos=metros*tiempo_calidad_alta
        elif calidad=="normal":
            n_calidad_normal+=1
            tiempo_minutos=metros*tiempo_calidad_normal
    
        if tiempo_minutos>tiempo_pedido_mayor:
            tiempo_pedido_mayor=tiempo_minutos
            pedido_tiempo_mayor=id_pedido
            
        if tiempo_minutos<tiempo_pedido_menor:
            tiempo_pedido_menor=tiempo_minutos
            pedido_tiempo_menor=id_pedido
        
        tiempo_total_minutos_pedido+=tiempo_minutos
        precio_por_metro=obtener_precio(material)/filamento
        precio_pedido=metros*precio_por_metro
        precio_total+=precio_pedido
    
        linea=pedido.readline().strip().lower()
    print(f"**PERIODO{i+1} **")
    obtener_tiempo(tiempo_total_minutos_pedido)
    print(f"-más rapida: {pedido_tiempo_menor}")
    obtener_tiempo(tiempo_pedido_menor)
    print(f"-más lenta: {pedido_tiempo_mayor}")
    obtener_tiempo(tiempo_pedido_mayor)
    print("-----")
porcentaje_alta_calidad=round((n_alta_calidad/numero_piezas)*100,2)
porcentaje_calidad_normal=round((n_calidad_normal/numero_piezas)*100,2)

print(f"Se imprimirán {numero_piezas} piezas ")

print(f"con un {porcentaje_alta_calidad}% de impresiones en alta calidad y un { porcentaje_calidad_normal}% de impresiones en calidad normal")

print("3) Filamento utilizado:")

for i in range(0,len(suma_materiales),1):
    print(f"{materiales[i].capitalize()}, {round(suma_materiales[i])} m")
print(f"Total: ${round(precio_total)}")


    