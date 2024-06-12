arch=open("playground.txt","r",encoding="utf-8")
linea=arch.readline().strip()
while linea!="":
    partes=linea.split(",")
    alumno=partes[0]
    universidad=partes[1]
    puntaje=int(partes[2])
    print(alumno+","+universidad+","+ str(puntaje))
    linea=arch.readline().strip()