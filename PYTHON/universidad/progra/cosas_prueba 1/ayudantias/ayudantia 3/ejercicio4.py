arch=open("ejercicio 4.txt","r",encoding="utf-8")
n=int(arch.readline())
for i in range(0,n,1):
    maestria_mayor=0
    nombre=""
    linea=arch.readline()
    clase=linea.split(",")[0]
    rep=int(linea.split(",")[1])
    for i in range(0,rep,1):
        linea_cha_maes=arch.readline()
        character=linea_cha_maes.split(",")[0]
        maestria=int(linea_cha_maes.split(",")[1])
        if maestria>maestria_mayor:
            maestria_mayor=maestria
            nombre=character
        
    print(clase, maestria_mayor, nombre)    