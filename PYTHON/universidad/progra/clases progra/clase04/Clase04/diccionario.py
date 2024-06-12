a={}
c=0
while True:
   
        
    c=input("nombre: ")
    if c=="-1":
        break
    b=int(input("ingresa un valor:"))
    if b==-1:
        break
    if c not in a:
        a[c]=b
    else:
        a[c]+=b
    
print(a)
