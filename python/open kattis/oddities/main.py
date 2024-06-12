T=int(input())
numbers=[]
for i in range(0,T,1):
    number=int(input())
    numbers.append(number)
for j in numbers:
    if j%2==0:
        print(str(j)+" is even")
    else:
        print(str(j)+" is odd")

