limit=int(input())
months=int(input())
temp=limit
rest=0
for i in range(0, months,1):
    limit=temp
    spent=int(input())
    rest+=limit-spent
print(rest+temp)
