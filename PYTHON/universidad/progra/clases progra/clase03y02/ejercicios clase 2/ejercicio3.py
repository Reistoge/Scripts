 #Escribe un programa que muestre en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por
# la palabra Fizz y, a su vez, los múltiplos de 5 por Buzz. Para los números que, al mismo tiempo,
 #son múltiplos de 3 y 5, utiliza el combinado FizzBuzz
 
for i in range(1,100,1):
    
    if i%5==0 and i%3==0:
        print('fizzbuzz')
        
    elif i%3==0:
        print('fizz')
       
    elif i%5==0:
        print('buzz') 
    else:
         print(i)
    
     
     
   