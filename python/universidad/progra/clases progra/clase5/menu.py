def menu(opciones, titulo):
    for i in range(0,len(opciones),1):
        print(opciones[i]+")", titulo[i])
    print(f"Selecciona una de las {len(opciones)} opciones mostradas en pantalla: ")
    opt=input("")
    while opt not in opciones:
        print(f"Debes seleccionar una de las {len(opciones)} mostradas en pantalla ")
        for i in range(0,len(opciones),1):
            print(opciones[i]+")", titulo[i])
        print(f"Selecciona una de las {len(opciones)} opciones mostradas en pantalla")
        opt=input("")
        
        
    
    






    