import decimal
N=int(input())
answers=[]
b=[]
for i in range(0,N,1):
    line=input()
    B,P=line.split()
    BPM=(60*float(B))/float(P)
    answers.append(BPM)
    b.append(BPM/int(B))

for i in range(0,N,1):
    s1=format(answers[i]-b[i],".4f")
    s2=format(answers[i],".4f")
    s3=format(answers[i]+b[i],".4f")
    print(s1,end=" ")
    print(s2,end=" ")
    print(s3)

