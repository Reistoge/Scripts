import numpy as np
rows=int(input())
columns=int(input())
mtx=np.zeros([rows,columns])

for i in range(0,columns):
    for j in range(0,rows):
        mtx[j][i]=(input())
print(mtx)