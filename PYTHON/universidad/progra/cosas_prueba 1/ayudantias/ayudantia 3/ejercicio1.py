arch=open("ejercicio 1.txt", "r", encoding="utf-8")
linea=arch.readline()
n=0
while linea!="":
    n+=1
    linea=arch.readline()
print(n)