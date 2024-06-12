variable=[1,0,0]




line=input()
for x in line:
    
    ballPos=variable.index(1)
    if (x=="A"):
        
        if ballPos==0:
            variable[0]=0
            variable[1]=1
        if ballPos==1:
            variable[0]=1
            variable[1]=0
        if ballPos==2:
            variable[2]=variable[2]
        
    if (x=="B"):
        
        if ballPos==0:
            variable[0]=variable[0]
        if ballPos==1:
            variable[2]=1
            variable[1]=0
        if ballPos==2:
            variable[2]=0
            variable[1]=1
        
            
    if (x=="C"):
        
        if ballPos==0:
            variable[0]=0
            variable[2]=1
        if ballPos==1:
            variable[1]=variable[1]
        if ballPos==2:
            variable[2]=0
            variable[0]=1
            
print(variable.index(1)+1)
        

    

    
    
    