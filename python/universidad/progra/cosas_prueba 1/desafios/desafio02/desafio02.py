# Desafío 02 - Programación
# Suma de cuadrados perfectos hasta X número
# Desarrolle un programa que sume los cuadrados perfectos en un rango definido por usuario.
 # Debe preguntar al usuario el número limite a considerar, y luego el programa debe sumar todos 
 # los cuadrados perfectos en el rango desde el número 1.

# Definición de Cuadrado Perfecto:
# Número cuya raíz cuadrada es un entero. Por ejemplo, 4 es un cuadrado perfecto porque su raíz cuadrada es el entero 2.

# Consideraciones:

# El primer cuadrado perfecto es el 1.
# El número indicado como rango superior se considera para la sumatoria en caso de ser un cuadrado perfecto.
# Las entradas y salidas (input y prints) deben tener exactamente el mismo texto que el del ejemplo de ejecución.
# Considere que nadie ingresará valores erróneos (Sólo considere enteros positivos)

# Ejemplo 1:

# Ingrese Rango Superior: 9
# Sumatoria: 14
sum=0
n=int(input("Ingrese Rango Superior: "))
for i in range(1,n+1,1):
    if (i**0.5)-round(i**0.5)==0:
        sum+=i
        
print(f"Sumatoria: {sum}")