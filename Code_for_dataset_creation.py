'''with open("abc0.txt") as f:
    abc0 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
abc0 = [x.split('\t') for x in abc0]

abc0.pop(0)


for i in range(1,8):
    maxi=-1.0
    for val in  abc0:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc0:
        val[i]= int((float(val[i])*1000)//maxi)'''

#rough
'''new=[]        
for val in abc0:
    r=[]
    for i in range (0,10):
        val[i]= int (float(val[i]))
    val.pop(0)
    new.append(val)

        
from  sklearn.preprocessing import OneHotEncoder
onehotencoder= OneHotEncoder(categories='auto')
X=onehotencoder.fit_transform(new).toarray()

'''
###END

'''with open("hello.txt") as f:
    hello = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
hello = [x.split('\t') for x in hello]

hello.pop(0)

for i in range(1,8):
    maxi=-1.0
    for val in  hello:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in hello:
        val[i]= int((float(val[i])))
        
for i in range(8,10):
    maxi=-1.0
    for val in  hello:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in hello:
        val[i]= int((float(val[i])))
        

######ROUGH
hello11=[]        
for val in hello:
    r=[]
    for i in range (0,10):
        val[i]= int (float(val[i]))
    val.pop(0)
    hello11.append(val)

        
from  sklearn.preprocessing import OneHotEncoder
onehotencoder= OneHotEncoder(categories='auto')
Y=onehotencoder.fit_transform(hello11).toarray()
        
#####END
        
with open("abc1.txt") as f:
    abc1 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
abc1 = [x.split('\t') for x in abc1]

abc1.pop(0)

for i in range(1,8):
    maxi=-1.0
    for val in  abc1:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc1:
        val[i]= int((float(val[i])*100)//maxi)
for i in range(8,10):
    maxi=-1.0
    for val in  abc1:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc1:
        val[i]= int((float(val[i])*500)//maxi)

######ROUGH
ABC1=[]        
for val in abc1:
    r=[]
    for i in range (0,10):
        val[i]= int (float(val[i]))
    val.pop(0)
    ABC1.append(val)

        
from  sklearn.preprocessing import OneHotEncoder
onehotencoder= OneHotEncoder(categories='auto')
Y1=onehotencoder.fit_transform(ABC1).toarray()    
#####END







with open("abc2.txt") as f:
    abc2 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
abc2 = [x.split('\t') for x in abc2]

abc2.pop(0)

for i in range(1,8):
    maxi=-1.0
    for val in  abc2:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc2:
        val[i]= int((float(val[i])*100)//maxi)
        
for i in range(8,10):
    maxi=-1.0
    for val in  abc2:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc2:
        val[i]= int((float(val[i])*500)//maxi)
######ROUGH

ABC2=[]        
for val in abc2:
    r=[]
    for i in range (0,10):
        val[i]= int (float(val[i]))
    val.pop(0)
    ABC2.append(val)

        
from  sklearn.preprocessing import OneHotEncoder
onehotencoder= OneHotEncoder(categories='auto')
Y2=onehotencoder.fit_transform(ABC2).toarray()

#####END


with open("abc3.txt") as f:
    abc3 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
abc3 = [x.split('\t') for x in abc3]

abc3.pop(0)

for i in range(1,8):
    maxi=-1.0
    for val in  abc3:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc3:
        val[i]= int((float(val[i])*100)//maxi)

for i in range(8,10):
    maxi=-1.0
    for val in  abc3:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc3:
        val[i]= int((float(val[i])*150)//maxi)
        
        
        
####ABC4

with open("abc4.txt") as f:
    abc4 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
abc4 = [x.split('\t') for x in abc4]

abc4.pop(0)

for i in range(1,8):
    maxi=-1.0
    for val in  abc4:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc4:
        val[i]= int((float(val[i])*100)//maxi)

for i in range(8,10):
    maxi=-1.0
    for val in  abc4:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc4:
        val[i]= int((float(val[i])*500)//maxi)
#END

####ABC5
print("TEn started")
with open("abcten.txt") as f:
    abc5 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
abc5 = [x.split('\t') for x in abc5]

abc5.pop(0)

for i in range(1,8):
    maxi=-1.0
    for val in  abc5:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    maxi=int(maxi)
    print(maxi)
    if maxi>0:
        for val in abc5:
            val[i]= int((float(val[i])))

for i in range(8,10):
    maxi=-1.0
    for val in  abc5:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc5:
        val[i]= int((float(val[i])))
        
#END
        
####ABC5
        
with open("abcten.txt") as f:
    abc5 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
abc5 = [x.split('\t') for x in abc5]

abc5.pop(0)

for i in range(1,8):
    maxi=-1.0
    for val in  abc5:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc5:
        val[i]= int((float(val[i])*100)//maxi)

for i in range(8,10):
    maxi=-1.0
    for val in  abc5:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc5:
        val[i]= int((float(val[i])*4000)//maxi)

##END


####ABC6
        
with open("abc6.txt") as f:
    abc6 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
abc6 = [x.split('\t') for x in abc6]

abc6.pop(0)

for i in range(1,8):
    maxi=-1.0
    for val in  abc6:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc6:
        val[i]= int((float(val[i])*100)//maxi)

for i in range(8,10):
    maxi=-1.0
    for val in  abc6:
        if maxi <abs(float(val[i])):
            maxi=abs(float((val[i])))
    print(maxi)
    for val in abc6:
        val[i]= int((float(val[i])*500)//maxi)'''

##END
import json
####ABC7
cntf=0.25
cnts=0.0005
trav=[2,4,8]
for frst in trav:
    cntf=0.25
    for row in range(0,3):
        cnts=0.0005
        for col in range(0,10):
            s="C"+str(frst)+"Pin"+str(cntf)+"Pout"+str(cnts)
            s2="C"+str(frst)+"_pin"+str(cntf)+"pout"+str(cnts)
            s3="C"+str(frst)+"_pin"+str(cntf)+"_pout"+str(cnts)
            with open(s+"/"+"1"+s2+".txt") as f:
                abc7 = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            abc7 = [x.split('\t') for x in abc7]
            
            abc7.pop(0)
            for i in range(1,10):
                maxi=-1.0
                for val in abc7:
                    val[i]= (float(val[i]))
            
            ##END
                    
                    
                    
            ####ABC8
                    
            with open(s+"/"+"2"+s2+".txt") as f:
                abc8 = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            abc8 = [x.split('\t') for x in abc8]
            
            abc8.pop(0)
            for i in range(1,10):
                maxi=-1.0
                for val in abc8:
                    val[i]= (float(val[i]))
            
            ##END
            count=0
            ####ABC9
                    
            with open(s+"/"+"100"+s2+".txt") as f:
                abc9 = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            abc9 = [x.split('\t') for x in abc9]
            
            abc9.pop(0)
            for i in range(1,10):
                for val in abc9:
                    val[i]= (float(val[i]))
            
            ##END
            
            
            ['node',
             'a_force.x',
             'a_force.y',
             'g_force.x',
             'g_force.y',
             'r_force.x',
             'r_force.y',
             'global_speed',
             'move_node.x',
             'move_node.y\n']
            '''
            import numpy as np
            x=np.zeros(shape=(18773,3400))
            i=1
            for val in hello:
                x[i][val[8]+500]=1
                x[i][val[9]+1000+500]=1
                x[i][val[1]+2000+100]=1
                x[i][val[2]+2200+100]=1
                x[i][val[3]+2400+100]=1
                x[i][val[4]+2600+100]=1
                x[i][val[5]+2800+100]=1
                x[i][val[6]+3000+100]=1
                x[i][val[7]+3200+50]=1
                i=i+1
            
            
            '''
            ###For Features
            import numpy as np
            i=0
            x=np.zeros(shape=(len(abc9),9))
            for val in abc7:
                x[i][0]=val[8]
                x[i][1]=val[9]
                i=i+1
            i=0
            for val in abc8:
                x[i][2]=val[1]
                x[i][3]=val[2]
                x[i][4]=val[3]
                x[i][5]=val[4]
                x[i][6]=val[5]
                x[i][7]=val[6]
                x[i][8]=val[7]
                i=i+1
            
            ###END
            dict_x={}
            for j in range(0,i):
                lis=[int(val) for val in x[j]]
                dict_x[str(j)]=lis
            
            
            np.save(s+"/ppi-feats.npy",x)
            
            dict_y={}
            
            #for j in range(0,i+1):
             #   lis=[int(val) for val in y[j]]
              #  dict_y[str(j)]=lis
            
            ###FOR JUST X
            i=0
            for val in abc9:
                dict_y[str(i)]=val[8]+4000;    
                i=i+1
            
                
            print(i)  
            ####END
            
            
            
            

            with open(s+"/just_x_class_map.json",'w')  as outfile:
                json.dump(dict_y, outfile)
                
            ##FOR JUST Y
            
            dict_y1={}
            
            
            i=0
            for val in abc9:
                dict_y1[str(i)]=val[9]+4000;    
                i=i+1
            
            

            with open(s+"/just_y_class_map.json",'w')  as outfile:
                json.dump(dict_y1, outfile)
            
            ####END
                
            '''G=json.load(open("ppi-G.json"))
            
            link_list=G["links"]
            
            nodes=G["nodes"]
            i=0
            cnt=0
            for val in nodes:
                if val['test']==False and val['val']==False:
                    print(val)
                    cnt=cnt+1
                i=i+1
                
                
            print(cnt/i)
            
            '''
            with open(s+"/"+s3+".txt") as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.split() for x in content]
            
            links=[]
            maxi=-1
            for val in content: 
                dict={'test_removed':False, 'train_removed':True,'source':int(val[0]),'target':int(val[1])}
                links.append(dict)
                if maxi < int(val[0]):
                    maxi=int(val[0])
                if maxi <int(val[1]):
                    maxi=int(val[1])
            
            
            NG={}
            NG['directed']=False
            NG['graph']={'name':'disjoint_union( , )'}
            NG['multigraph']=False
            NG['links']=links
            
            
            list_for_features=[]
            
            for j in range(0,len(abc9)):
                lis=[val for val in x[j]]
                list_for_features.append(lis)
            
            
            i=0
            y=np.zeros(shape=(len(abc9),2))
            for i in range(0,len(abc9)):
                y[i][0]=dict_y[str(i)]
                y[i][1]=dict_y1[str(i)]
                i=i+1
            
            list_for_label=[]
            for j in range(0,len(abc9)):
                lis=[int(val) for val in y[j]]
                list_for_label.append(lis)
            
            class_map={}
            i=0
            for val in list_for_label:
                class_map[str(i)]=val
                i=i+1
                
            with open(s+"/ppi-class_map.json",'w')  as outfile:
                json.dump(class_map, outfile)
            
            
            for val in links:
                if val['target']==0 or val['source']==0:
                    print(val)
            
            
            
            # x is the feature y is the label
            node_list=[]
            i=0
            g=False
            for i in range(0,len(abc9)):
                node_dict={}
                node_dict['id']=i
                #i=i+1
                g=False
                if i%5==0:
                    node_dict['test']=True
                    g=True
                else:
                    node_dict['test']=False
                if i%8==0 and g==False:
                    node_dict['val']=True
                else:
                    node_dict['val']=False
                
                node_dict['feature']=list_for_features[i]
                
                node_dict['label']=list_for_label[i]    
                i=i+1
                
                node_list.append(node_dict)
                
                
                
            i=0
            for i in range(0,10):
                print(node_list[i])
                
            NG['nodes']=node_list  
            
            with open(s+"/ppi-G.json",'w')  as outfile:
                json.dump(NG, outfile)
            
            cnts=cnts+0.001
            cnts=round(cnts,4)
            
            
        cntf=cntf+0.25
        cntf=round(cntf,2)
        
            
            
