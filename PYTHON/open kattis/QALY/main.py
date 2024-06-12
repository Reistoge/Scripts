N=int(input())
product=0
for i in range(0, N,1):
    line=input()
    q,y=line.split()
    
    product+=float(q)*float(y)
print(product)
