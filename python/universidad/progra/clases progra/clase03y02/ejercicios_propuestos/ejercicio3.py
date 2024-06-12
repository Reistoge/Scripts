alternativas=["a","b"]
print("Introduce la asignatura: \na)progra\nb)progra avanzada ")
asignatura=input("opcion: ").lower()
while asignatura not in alternativas or asignatura!="progra" or asignatura!="progra avanzada":
    print("\nOpcion erronea, debes escoger entre a o b:")
    asignatura=input("Introduce la asignatura: ").lower()

print("Escogiste: "+asignatura.upper())
###verificamos si introduce bien la info tanto como la asignatura como la accion

print("Que quieres hacer en "+asignatura+"?\na)Asistencia\nb)Promedio Final")
accion=input("Que quieres hacer en "+asignatura+" ? ")
while accion not in alternativas:
    print("Opcion erronea, debes escoger entre a o b:\nQue quieres hacer en",asignatura,"?")
    print("a)Asistencia\nb)Promedio Final")
    accion=input("")
    

print("Perfecto !!, entonces quieres ",accion,asignatura)
