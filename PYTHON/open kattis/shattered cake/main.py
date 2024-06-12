
W=int(input())
P=int(input())
tempArea=0
for i in range(0,P,1):
    line=input()
    width,length=line.split()
    width=int(width)
    length=int(length)
    tempArea+=width*length

print(int(tempArea/W))
