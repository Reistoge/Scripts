
def comparar(array,array2):
    for i in range(8):
        if array[i]!=array2[i]:
            return False
    return True


steps=0
final_state=[1,2,4,6,10,12,16,18]
current_state=input().split(" ")
for i in range(len(current_state)):
    current_state[i]=int(current_state[i])
 

while current_state[7]<18:
    steps+=510510
    current_state[7]+=1
 

while not (comparar(current_state,final_state)):
    current_state[0]+=1
    steps+=1
    if current_state[0]==2:
        current_state[0]=0
        current_state[1]+=1
        
    if current_state[1]==3:
        current_state[1]=0
        current_state[2]+=1
        
    if current_state[2]==5:
        current_state[2]=0
        current_state[3]+=1
    
    if current_state[3]==7:
        current_state[3]=0
        current_state[4]+=1
        
    if current_state[4]==11:
        current_state[4]=0
        current_state[5]+=1
        
    if current_state[5]==13:
        current_state[5]=0
        current_state[6]+=1
        
    if current_state[6]==17:
        current_state[6]=0
        current_state[7]+=1
 
 
 
 

print(steps)