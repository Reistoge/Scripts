def comparar_textos(texto1,texto2):
    arch1=open(texto1,"r",encoding="utf-8")
    arch2=open(texto2,"r",encoding="utf-8")
    linea1=arch1.readline().strip()
    linea2=arch2.readline().strip()
    iguales=True
    while linea1!="":
        if linea1!=linea2:
            iguales=False
            print(linea1)
            print(linea2)
            
        linea1=arch1.readline().strip()
        linea2=arch2.readline().strip()
        
    print(iguales)        
    return iguales
    
comparar_textos("original.txt", "output.txt")