
def verificar_numero(palabra):
    numeros_verificar=["0","1","2","3","4","5","6","7","8","9"]
    n=0
    for letra in palabra:
        for digito in numeros_verificar:
            if letra==digito:
                n+=1
                
    if n==len(palabra):
        print("es numero")
    else:
        print("no es numero ")       

        
        
verificar_numero("asd")




