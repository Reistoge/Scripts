N=int(input())
total=0
for i in range(0,N,1):
    temp=int(input())
    total+=temp
print(total-(N-1))