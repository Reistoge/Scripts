cupon=input("tienes cupon ?: ")
edad =int(input("introduce la edad de la persona: "))
cupon=cupon.lower()
if edad <=3:
    print("la entrada es gratis")
if edad >=4 and edad<=12 and cupon=="no":
    print('el valor de tu entrada es 5000')
elif edad >=4 and edad<=12 and cupon=="si":
    print('el valor de tu entrada es 3000')
    
if edad>=13 and edad<=64 and cupon=="no":
    print('el valor de tu entrada es 10.000')
elif edad>=13 and edad<=64 and cupon=="no":
    print('el valor de tu entrada es 8000')

if edad>=65  and cupon=="no":
    print('el valor de tu entrada es 7.500')
elif edad>=65  and cupon=="si":
    print('el valor de tu entrada es 5.500')
    
    

