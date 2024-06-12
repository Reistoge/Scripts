####Cómo puedo escribir algo que realice lo siguiente:
##Queremos contar cuantos estudiantes varones son mayores de 18 años 
##También queremos desplegar la suma de las edades de los alumnos menores a 18 años
###Hay 15 estudiantes en el curso 
estudiante_varones_mayores=0
suma_de_estudiantes_menores=0
for i in range(0,15,1):
    sexo=input("introduce el sexo: ").upper()
    edad=int(input("introduce la edad: "))
    if sexo=="VARON" and edad>18:
        estudiante_varones_mayores+=1
    elif edad<18:
        suma_de_estudiantes_menores+=edad
print(estudiante_varones_mayores)
print(suma_de_estudiantes_menores)
        