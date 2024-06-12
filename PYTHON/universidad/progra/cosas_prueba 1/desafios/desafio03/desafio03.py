# Desafío 03 - Programación
# Transformador de unidades de longitud
# Se desea construir un transformador de unidades de longitud dinámico que permita a los usuarios decidir qué unidades convertir. Su programa debe ser capaz de realizar las siguientes conversiones:

# Centímetros (CM) a Metros (M) y viceversa
# Centímetros (CM) a Kilómetros (KM) y viceversa
# Centímetros (CM) a Pulgadas (IN) y viceversa
# Centímetros (CM) a Pies (FT) y viceversa
# Metros (M) a Kilómetros (KM) y viceversa
# Metros (M) a Pies (FT) y vicevera
# Metros (M) a Pulgadas (IN) y viceversa
# Pulgadas (IN) a Pies (FT) y viceversa
# Pulgadas (IN) a Kilómetros (KM) y viceversa
# Pies (FT) a Kilómetros (KM) y viceversa
# Para lograrlo, el usuario debe ingresar primero las unidades que quiere convertir utilizando la abreviación correspondiente y el símbolo >. Por ejemplo: M>KM busca convertir de metro a kilómetro. El programa debe terminar cuando la persona escriba la palabra FIN.

# Consideraciones:

# Debe convertir los input de entrada a mayúsculas de lo contrario el juez le dará error
# Considere que una pulgada es equivalente a 2.54 cms.
# Considere que un pie es equivalente a 30.48 cms.
# El tipo de dato de las medidas a convertir será FLOAT.
# Las entradas y salidas (input y prints) deben tener exactamente el mismo texto que el del ejemplo de ejecución.
# Considere que nadie ingresará valores erróneos (unidades mal escritas o valores fuera de rango). Ya veremos esto más adelante.
# Para que su problema funcione correctamente al final de su input debe colocar .strip() como se ve en el siguiente ejemplo:
# variable = input('blablabla').upper().strip()
# #si convierte el resultado en float .strip() debe estar donde corresponde
# variable_numerica = float(input('blabla').strip())

def transformador(unidad1,unidad2,cantidad):
    unidad=["CM","M","KM","IN","FT"]
    magnitudes=[1.0, 100.0, 100000.0,2.54, 30.48]
    # unidad.index(unidad1)
    # unidad.index(unidad2)
    
    return cantidad * magnitudes[unidad.index(unidad1)] / magnitudes[unidad.index(unidad2)]
    
    

unidades=""

while True:
    unidades=input("Ingrese unidades a convertir: 'UNIDAD1>UNIDAD2' (FIN para terminar) : ").upper().strip()
    if unidades=="FIN":
        break
    unidad1=unidades.split(">")[0].strip()
    unidad2=unidades.split(">")[1].strip()
    
    cantidad=input("Ingrese valor a convertir: ").upper().strip()
    if cantidad=="FIN":
        break
    cantidad=float(cantidad)
    respuesta=transformador(unidad1, unidad2, cantidad)
    
    print(cantidad, unidad1,"corresponden a", round(respuesta,4) , unidad2)
    
print("Conversión finalizada")