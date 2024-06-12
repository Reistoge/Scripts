motores=open('Simulacro_ejercicio2_motores.txt','r',encoding='UTF-8')

'''
Porcentaje de motores defectuosos con respecto al total y listado de esos motores
defectuoso es emisiones mayor a 25
Porcentaje de motores que se pueden rectificar con respecto al total y listado de esos motores
Rectificar es cumplir con emisiones pero su hp no es suficiente
Promedio caballos de fuerza de motores que si cumplen (2 decimales)
Marca con el motor que menos emite y su porcentaje de emision
'''
cinta=open('Simulacro_ejercicio2_cinta.txt','r',encoding='UTF-8')
linea=cinta.readline().strip()
total_motores=0
total_defectuosos=0
lista_defectuosos=[]
total_rectificar=0
lista_rectificar=[]
total_cumplimiento=0
total_buenos_D=0
total_buenos_V=0
total_buenos_B=0
menor=100**10
marca_menor=''



while linea!='':
    partes=linea.split(',')
    numero_serie=partes[0]
    Marca=numero_serie.split('-')
    hp=partes[1]
    emisiones=int(partes[2])
    if numero_serie!='':
        total_motores+=1
    if emisiones>25:
        total_defectuosos+=1
        lista_defectuosos.append(numero_serie)
    elif emisiones<25:
        if emisiones<menor:
            menor=emisiones
            marca_menor=Marca
        if Marca=='D':
            if hp<350:
                total_rectificar+=1
                lista_rectificar.append(numero_serie)
            elif hp>=350:
                total_buenos_D+=1
        elif Marca=='V':
            if hp<500:
                total_rectificar+=1
                lista_rectificar.append(numero_serie)
            elif hp>=500:
                total_buenos_V+=1
        elif Marca=='B':
            if hp<200:
                total_rectificar+=1
                lista_rectificar.append(numero_serie)
            elif hp>=200:
                total_buenos_B+=1
    linea=cinta.readline().strip()
porcentaje_defectuosos=




print(f'los motores defectuosos representan un {porcentaje_defectuosos}%')
print(f'Sus numeros de serie son {lista_defectuosos}')
print('*'*60)
print(f'Los motores rectifiablen representan un {porcentaje_rectificables}%')
print(f'Sus numeros de serie son {lista_rectificables}')
print(f'Los motores xx de xx tienen un promedio de {hp_D}HP')
print(f'Los motores xx de xx tienen un promedio de {hp_V}HP')
print(f'Los motores xx de xx tienen un promedio de {hp_B}HP')
    
    
    
    
    
    
    
    
    
    