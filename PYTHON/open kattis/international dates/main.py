line=input()
a=line[0:2]
b=line[3:5]
c=line[6:10]


if int(a)>12 and int(b)<=12:
    print("EU")
if int(a)<=12 and int(b)>12:
    print("US")
if int(a)<=12 and int(b)<=12:
    print("either")