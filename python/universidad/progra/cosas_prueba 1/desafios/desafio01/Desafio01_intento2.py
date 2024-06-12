peso = float(input("Ingrese peso en kg: "))
destino = input("Ingrese destino: ").upper()
 
if peso <= 2 and destino == "CHILE":
    coste_total = 10
elif peso <= 2 and destino != "CHILE":
    coste_total = 20
if peso >= 2 and peso < 5 and destino == "CHILE":
    coste_total = 15
elif peso >= 2 and peso < 5 and destino != "CHILE":
    coste_total = 30
if peso >= 5 and destino == "CHILE":
    coste_total = 25
elif peso >= 5 and destino != "CHILE":
    coste_total = 50
 
if destino == "ARGENTINA" and peso <= 5:
    coste_total -= 5
elif destino == "BRASIL" and peso >= 5:
    coste_total += 10
    
print(f"Costo total {coste_total} USD")