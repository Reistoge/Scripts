cards=input()
ranks=""
cards=cards.split()
for card in cards:
    ranks+=card[0]

#crear un diccionario vacio para guardar las frecuencias
frecuencias={}


for letra in ranks:
    if letra in frecuencias:
        frecuencias[letra]+=1
    else:
        frecuencias[letra]=1


letra_max=max(frecuencias,key=frecuencias.get)
print(frecuencias[letra_max])
