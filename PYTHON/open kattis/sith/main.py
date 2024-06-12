name=input()
a=float(input())
b=float(input())
c=float(input())

if (a-b)<0 and c<0 and abs(a-b)!=c:
    print("JEDI")
elif abs(a-b)==c and a<b and c>0:
    print("SITH")
elif abs(a-b)==c and a>b and c>0:
    print("VEIT EKKI")