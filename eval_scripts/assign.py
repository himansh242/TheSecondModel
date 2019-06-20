import statistics as st
def val(n,ca):
    l=[]
    print(ca)
    ans=[]
    i=0
    mini=328945398
    max=0
    sum=0
    
    for val in ca:
        if i==0:
            l=val
        else:
            cnt=0
            for i in range(len(val)):
                #print("hey")
                if(val[i]==l[i]):
                    cnt=cnt+1
            ans.append(cnt)
        i=i+1
    print(l)
    print(ans) 
    print("mini score" + str(min(ans)))
    print("avg score "+str(st.mean(ans)))
    print("median score "+ str(st.median(ans)))
    print((max(ans)))
            
            
bl=[]
for i in range(4):
    n=input()
    a=[]
    a=n.split()
    bl.append(a)

val(4,bl)

    #f.write(s)
    #print(s)
