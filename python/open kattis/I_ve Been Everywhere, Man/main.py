T=int(input())
frequency=[]
for i in range(0,T,1):
    frequency.append(0)
    T2=int(input())
    places={}
    for j in range(0,T2,1):
        place=input()
        if place in places:
            places[place]+=1
        else:
            places[place]=1
    for k in places:
        frequency[i]+=1

for l in frequency:
    print(l)

