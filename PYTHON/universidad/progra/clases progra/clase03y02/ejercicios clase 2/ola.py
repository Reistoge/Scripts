edad = int(input("Escriba su edad: "))
cupon = (input("Tiene cupón (Sí/No): ")).lower()

precio_niños = 0
precio_grande = 5000
precio_regular = 10000
precio_anciano = 7500
descuento = 2000
if edad <= 3:
    precio_final = precio_niños
elif 4 >= edad and edad <= 12:
    precio_final = precio_grande
elif 13 <= edad and edad <= 64:
    precio_final = precio_regular
elif edad >= 65:
    precio_final = precio_anciano
else:
    print("Su edad no es válida")

if cupon == "si":
    print(f"Tu descuento es de {precio_final - descuento}")
else:
    print(f"{precio_final}")