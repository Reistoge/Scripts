import numpy as np
bodega=open('bodega.txt','r',encoding='UTF-8')
linea=bodega.readline().strip()
zonas=[]
sectores=[]
while linea!='':
    partes=linea.split(';')
    zona=partes[0]
    sector=partes[1]
    if zona not in zonas:
        zonas.append(zona)
    if sector not in sectores:
        sectores.append(sector)
    linea=bodega.readline().strip()
bodega.close()
matriz=np.zeros([len(zonas),len(sectores)])
bodega=open('bodega.txt','r',encoding='UTF-8')
linea=bodega.readline().strip()
print('A) Ubicaciones sobrecargadas:')
while linea!='':
    partes=linea.split(';')
    zona=partes[0]+partes[1]
    if int(partes[2])>100:
        extra=int(partes[2])-100
        print(f'la ubicacion {zona} tiene {extra} articulos extra')
    matriz[zonas.index(partes[0])][sectores.index(partes[1])]=partes[2]
    linea=bodega.readline().strip()
bodega.close()
movimientos=open('movimientos.txt','r',encoding='UTF-8')
linea=movimientos.readline().strip()
print('*'*60)
print('B) Las ubicaciones sobrecargadas despues del cambio son:')
while linea!='':
    partes=linea.split(';')
    zonasector=partes[0].split('-')
    ubicacion_z=zonasector[0]
    ubicacion_s=zonasector[1]
    zona=zonas.index(zonasector[0])
    sector=sectores.index(zonasector[1])
    if partes[1]=='ingreso':
        matriz[zona][sector]+=int(partes[2])
    elif partes[1]=='retiro':
        matriz[zona][sector]-=int(partes[2])
    if matriz[zona][sector]>100:
        extra=matriz[zona][sector]-100
        print(f'la ubicacion {ubicacion_z}{ubicacion_s} tiene {extra} articulos extra')
    linea=movimientos.readline().strip()