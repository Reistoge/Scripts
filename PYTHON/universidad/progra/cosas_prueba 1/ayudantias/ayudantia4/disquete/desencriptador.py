from decodificadores_ezic import desencriptar,ezic


def desencriptar_mensaje():
    arch = open("mensaje.txt", encoding="utf-8")
    linea = arch.readline().strip()
    
    while linea != "":
        linea_desencriptada=desencriptar(linea)
        print(linea_desencriptada)
        linea=arch.readline().strip()
def desencriptar_linea():
    arch=open("gloria_a_la_nueva_artotzka.txt",encoding="utf-8")
    linea=arch.readline()
    print(desencriptador_reforzado(linea, 2))
    
def desencriptar_mensaje_ezic():
    arch = open("ezic_only.txt", encoding="utf-8")
    linea = arch.readline().strip()

    
    while linea != "":
        partes = linea.split(",")
        numero=int(partes[0])
        palabra_clave=partes[1].upper()
        
        if palabra_clave == "KOL":
            nivel_encriptacion = 1
        elif palabra_clave == "GRE":
            nivel_encriptacion = 2
        else:
            nivel_encriptacion = 3
        
        for i in range(numero):
            linea = arch.readline().strip()
            mensaje_desencriptado=desencriptador_reforzado(linea, nivel_encriptacion)
            print(mensaje_desencriptado)
            
            
        linea = arch.readline().strip()

def desencriptador_reforzado(mensaje, nivel_encriptacion):
    for capas in range(nivel_encriptacion):
        mensaje = desencriptar(mensaje)
    return mensaje

desencriptar_linea()

