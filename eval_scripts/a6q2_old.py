import numpy as np

def find_target(d2,n):
    for j in range(6):
        for i in range(1,6):
            d2[i][j]+=d2[i-1][j]
    maxi=-1
    summ=0
    x=0
    y=0
    for j in range(2*n+1):
        summ+=d2[2*n][j]
    if maxi<summ:
        maxi=summ
        x=2*n
        y=2*n
    for j in range(2*n+1,6):
        summ-=d2[2*n][2*n+1-j]
        summ+=d2[2*n][j]
        if maxi<summ:
            maxi=summ
            x=2*n
            y=j
        
    for i in range(2*n+1,6):
        sum=0
        for j in range(2*n+1):
            summ+=(d2[i][j]-d2[2*n+1-i][j])
        if maxi<summ:
            maxi=summ
            x=i
            y=2*n
        for j in range(2*n+1,6):
            summ-=d2[i][2*n+1-j]
            summ+=d2[i][j]
            if maxi<summ:
                maxi=summ
                x=i
                y=j
    
    
    return x,y,maxi
        
            
    
    
    
    
d2=np.array([[1,2,3,4,5,6],[4,5,1,2,9,10],[12,5,3,5,2,8],
            [7,1,0,5,4,2],[5,7,3,9,12,8],[4,9,12,5,-100,2]],np.int64)
    
    
x,y,maxi=find_target(d2,2)

print(d2)
print(str(x)+" "+str(y)+" "+str(maxi) )