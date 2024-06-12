line=input()
N,K=line.split()
N=float(N)
K=int(K)
sum=0
for i in range(0,K,1):
    sum+=float(input())   
max=float((((N-K)*3)+sum)/N)
min=float((((N-K)*-3)+sum)/N)
print(min,end=" ")
print(max)
