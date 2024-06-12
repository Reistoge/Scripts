q = 0
suma = 3
i = 10 
while i > 0: 
    i = i - 2 
    q = q + i 
    if i > 5: 
        for j in range(i, i + 2): 
            suma = suma + (j+(q%2))
            while (j==7):
                frase = "Muy "
                j=j+1
    elif (i<5 and i >2):
        suma = suma % 3
        q=q*2
        suma = suma % 2
        while (i==5):
            frase = "Habiloso"
            i += 1
    else: 
        for j in range(i - 1, i): 
            suma = suma - (j+i)
            while (j==1):
                frase = "Bien"
                j += 1
 
suma = suma + 1
print((suma+q)-(j+i),frase)


