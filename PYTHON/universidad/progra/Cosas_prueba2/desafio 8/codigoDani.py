
""" funciones """
def intercambiar(lista,a,b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def bublesort(lista1,lista2,lista3):
    for a in range(len(lista1)-1):
        for b in range(a+1,len(lista1)):
            if lista1[a] > lista1[b]:
                intercambiar(lista1,a,b)
                intercambiar(lista2,a,b)
                intercambiar(lista3,a,b)

def buscarAgregar(elemento,lista1,lista2):
    for i in range(len(lista2)):
        if lista2[i] not in lista1:
            lista1.append(lista2[i])
    
import numpy as np

arch = open("maquinaria.txt","r", encoding = "utf-8")
linea = arch.readline().strip()
#CategoríaMaquinaria,Año,ValorenMillones

anhosrepetidos = []
anhos = []
categoriasrepetidas = []
categorias = []
valoresrepetidos = []

while linea != "":
    partes = linea.strip().split(";")
    categ = partes[0]
    anho = int(partes[1])
    valor = float(partes[2])
    
    if ((anho >= 2023) and (anho <= 2027)):
        anhosrepetidos.append(anho)
        categoriasrepetidas.append(categ)
        valoresrepetidos.append(valor)
        
    linea = arch.readline().strip()

bublesort(anhosrepetidos,categoriasrepetidas,valoresrepetidos)
buscarAgregar(anho,anhos,anhosrepetidos)
buscarAgregar(categ,categorias,categoriasrepetidas)

matrix = np.zeros([len(categorias),len(anhos)])

for i in range(len(categoriasrepetidas)): 
    f = categorias.index(categoriasrepetidas[i])
    c = anhos.index(anhosrepetidos[i])
    if (int(matrix[f][c]) == 0):
        matrix[f][c] = valoresrepetidos[i]
    else:
        matrix[f][c] += valoresrepetidos[i]

menor = 9999

for fila in range(len(categorias)):
    val_prom = 0
    for columna in range(len(anhos)):
        val_prom += matrix[fila][columna]
    if ((val_prom/5) < menor): #porque 5 ??
        menor = (val_prom/5)
        menorcat = categorias[fila]
print(f"La categoría con menor valor promedio es {menorcat} con un valor promedio de {round(menor,1)}") # pasar a float 

for columna in range(len(anhos)):
    print(f"{anhos[columna]} - {round(matrix[categorias.index(menorcat),columna],1)} Millones")

val_final = 0
for fila in range(len(categorias)):
    val_final += matrix[fila][4]
print(f"La valorización final {anhos[-1]} es de {round(val_final,1)}")

if val_final < 9500:
    print("El proyecto es conveniente")
else:
    print("El proyecto NO es conveniente")