T=int(input())
numbers=[]

for i in range(0,T,1):
    Number=int(input())
    product=1
    for j in range(Number,1,-1):
        product=product*j

    numbers.append(product)
    
for number in numbers:
    print(number%10)   
