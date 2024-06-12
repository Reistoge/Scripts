peso=float(input('Ingrese peso en kg: '))
destino=input('Ingrese destino: ').upper()
coste_de_envio=0
if destino !="CHILE" :
    if peso<2:
        coste_de_envio=20
        if destino=="ARGENTINA":
            coste_de_envio-=5
    elif peso >=2 and peso<5:
        coste_de_envio=30
        if destino=="ARGENTINA":
            coste_de_envio-=5
    elif peso >=5:
        coste_de_envio=50
        if destino=="ARGENTINA":
            coste_de_envio-=5
        if destino=="BRASIL" and peso>5:
            coste_de_envio+=10
## Si el país de destino es ARGENTINA y el peso es menor o igual a 5kg, se debe realizar un descuento de 5 dólares al total.
##Si el país de destino es BRASIL y el peso es mayor a 5kg se debe aplicar un recargo adicional de 10 dólares por impuestos
        
elif destino=="CHILE":
    if peso<2:
        coste_de_envio=10
    elif peso >=2 and peso<5:
        coste_de_envio=15
    elif peso >=5:
        coste_de_envio=25
        
        
        

print('Costo total '+str(coste_de_envio)+' USD')