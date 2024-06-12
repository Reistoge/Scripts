N=int(input())
sum=0
""" string[start:stop:step] """
for i in range(0,N,1):
    number=input()
    rNumber=int(number[0:len(number)-1])
    powd=int(number[len(number)-1])
    
    sum+=pow(rNumber,powd)
print(sum)