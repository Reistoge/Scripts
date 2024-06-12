import numpy as np

def position(_map_):
    rows=_map_.shape[0]
    columns=_map_.shape[1]
    for i in range(0,rows,1):
        for j in range(0,columns,1):
            if _map_[i][j]==1:
                return [i,j]
    return 0
            
def print_map(_map_):
    rows=_map_.shape[0]
    columns=_map_.shape[1]
    for i in range(0,rows,1):
        print(_map_[i])

            
    
    
    
    
    
    
    
map_=np.zeros([10,10])
mapa[5][5]=1
print_map(mapa)



