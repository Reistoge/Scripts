import math

line=input()
a,b,c,d=line.split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
s=(a+b+c+d)/2

maxArea=math.sqrt((s-a)*(s-b)*(s-c)*(s-d))
print(maxArea)
