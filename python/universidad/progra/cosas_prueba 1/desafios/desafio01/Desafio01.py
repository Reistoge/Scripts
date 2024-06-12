peso=float(input('Ingrese peso en kg: '))
destino=input('Ingrese destino: ').upper()
coste_de_envio=0
if destino !="CHILE":
   #destino internacional
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
       if destino=="BRASIL":
           coste_de_envio+=10
        
elif destino=="CHILE":
    if peso<2:
        coste_de_envio=10
    elif peso >=2 and peso<5:
        coste_de_envio=15
    elif peso >=5:
        coste_de_envio=25
        
        
        

print('Costo total '+str(coste_de_envio)+' USD')