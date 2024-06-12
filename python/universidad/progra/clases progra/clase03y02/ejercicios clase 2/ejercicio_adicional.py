a=1
while a!=0:
    a=float(input())
    impar=False
    nuevo_valor=0

        
    if a%2 != 0:
        impar=True
        
    if a%2 == 0:
        impar=False


    if impar and a>25:
        #impar positivo mayor que 25
        nuevo_valor=(a+(3*a))*4
        print("impar")
        print("caso 1")
        print(a, nuevo_valor)
        
    if not impar and a>25:
        #par positivo mayor que 25
        nuevo_valor=(a+(3*a))/3
        print("quiza es par")
        print("caso 2")
        print(a, nuevo_valor)
        
    if  a<=25 and a>0:
        # positivo menor que 25 y mayor que 0
        print("quiza es par")
        print('caso 3')
        nuevo_valor=(a+(3*a))/3
        print(a, nuevo_valor)
       
    if  a<0 and a >=-10:
        # entre 0 y -10 negativo
        print("quiza es par")
        print("caso 4")
        nuevo_valor=(a - 2*(a/2))/3
        print(a, nuevo_valor)
                
    if impar and a<-10:
        #impar menor que -10 y negativo
        print("Impar")
        print("caso 5")
        nuevo_valor=(a - 2*(a/2))*4
        print(a, nuevo_valor)
    if not impar and a <-10:
         #par menor que -10,negativo
         print("quiza es par")
         print("caso 6")
         nuevo_valor=(a - 2*(a/2))/3
         print(a, nuevo_valor)
    

     
temp=nuevo_valor

if  a==0:
    print('fin')
    
#a que numero se refiere puede ser el input o el del output??.
if  nuevo_valor==0:
    print('fin')
    

if a > nuevo_valor:
    a=temp
    nuevo_valor=temp
    print('el resultado final es '+ str(a)+' y el original es '+ str(nuevo_valor))
    
    


    
