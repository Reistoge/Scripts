line=input()
H,M=line.split()
H=int(H)
M=int(M)

if(M>=45):
    print(str(H)+' '+str(M-45))
if(M<45):
    if((H-1)<0):
        print(str((H+24)-1)+' '+str((M+60)-45))
    else:
        print(str(H-1)+' '+str((M+60)-45))