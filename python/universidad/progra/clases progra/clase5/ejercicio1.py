# La empresa “TicketMusica” necesita un programa para gestionar las ventas de 
# entradas en los diferentes eventos que tiene a cargo. Para ello le ha solicitado 
# a usted que desarrolle el programa, con la condición de que tiene que incluir 
# una función llamada “ventas”. La función debe recibir la cantidad de entradas 
# que se desean comprar y el tipo de entrada. La función debe retornar el monto 
# que se debe cancelar por cada venta. 
# Los tipos de entradas son las siguientes:
# • Cancha: $20.000
# • Platea: $30.000
# • Vip: $40.000


def ventas(entradas, tipo):
    if tipo.lower()=="cancha":
        return entradas*20000
    elif tipo.lower()=="platea":
        return entradas*30000
    elif tipo.lower()=="vip":
        return entradas*40000
        
print(ventas(4,"platea"))