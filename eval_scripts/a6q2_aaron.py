import numpy as np

def find_target(d2,n):
    for j in range(d2.shape[1]):
        for i in range(1,d2.shape[0]):
            d2[i][j]+=d2[i-1][j]
    maxi=-1
    summ=0
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
        
            
    
    
    
    
d2=np.array([[1,1,1,1],
             [1,1,1,1],
             [1,1,3,1],
             [1,1,1,2]])
    
    
x,y,maxi=find_target(d2,2)

print(d2)
print(str(x)+" "+str(y)+" "+str(maxi) )