n=int(input("ingrese un numero: "))
contador=0
for i in range(1,n+1):
    if n%i==0:
        contador+=1
    
        
if contador==2:
    print("primo")
else:
    print("compuesto")
      

       
    
##felipe.guerra01@alumnos.ucn.cl