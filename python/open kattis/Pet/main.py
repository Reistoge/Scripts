
max_sum=0
index=0
max_index=0
numbers=[]
for i in range(0,5,1):
    numbers=[]
    sum=0
    str_numbers=list(input())
    for j in range(0,8,2):
        
        numbers.append(int(str_numbers[j]))

    for n in numbers:
        sum+=n
    if(sum>max_sum):
        max_sum=sum
        max_index= i
print(max_index+1, max_sum)



    