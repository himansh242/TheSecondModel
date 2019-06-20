from __future__ import print_function
import json
import numpy as np

from networkx.readwrite import json_graph
from argparse import ArgumentParser

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures
from keras.layers import Dense, Activation
from keras.models import Sequential
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense, Conv2D, Flatten


from keras.layers import Dense
from keras.layers import Dropout
from keras.layers.convolutional import Conv2D
from keras.layers import Dense
from keras.layers.convolutional import MaxPooling2D
from keras.layers import BatchNormalization

import os
cntf=0.25
cnts=0.0005
trav=[2,4,8]
for frst in trav:
    cntf=0.25
    for row in range(0,3):
        cnts=0.0005
        for col in range(0,10):
            s="C"+str(frst)+"Pin"+str(cntf)+"Pout"+str(cnts)
            print("Loading data...")
            G = json_graph.node_link_graph(json.load(open(s + "/ppi-G.json")))
            labels_x = json.load(open(s + "/just_x_class_map.json"))
            labels_x = {int(i):l for i, l in labels_x.items()}
            
            labels_y = json.load(open(s + "/just_y_class_map.json"))
            labels_y = {int(i):l for i, l in labels_y.items()}
            
            train_ids = [n for n in G.nodes() if not G.node[n]['val'] and not G.node[n]['test']]
            test_ids = [n for n in G.nodes() if G.node[n]['test'] or G.node[n]['val']]
            all_ids = [n for n in G.nodes()]
            
            train_labels_x = np.array([labels_x[i] for i in train_ids])
            test_labels_x = np.array([labels_x[i] for i in test_ids])
            all_labels_x = np.array([labels_x[i] for i in all_ids])
            
            train_labels_y = np.array([labels_y[i] for i in train_ids])
            test_labels_y = np.array([labels_y[i] for i in test_ids])    
            all_labels_y=np.array([labels_x[i] for i in all_ids])
            
            #print(train_embeds.shape)
            
            print("running","unsup-example_data/graphsage_meanpool_small_0.000010")
            
            embeds = np.load(s+"/graphsage_meanpool_small_0.000010" + "/val.npy")
            id_map = {}
            with open(s+"/graphsage_meanpool_small_0.000010" + "/val.txt") as fp:
                for i, line in enumerate(fp):
                    id_map[int(line.strip())] = i
            train_embeds = embeds[[id_map[id] for id in train_ids]] 
            test_embeds = embeds[[id_map[id] for id in test_ids]] 
            all_embeds= embeds[[id_map[id] for id in all_ids]] 
            print("Running regression..")
            sc=StandardScaler()
            train_embeds=sc.fit_transform(train_embeds)
            test_embeds=sc.fit_transform(test_embeds)
            all_embeds=sc.fit_transform(all_embeds)
            input_shape=[1,train_embeds.shape[1],1]
            cnn4 = Sequential()
            cnn4.add(Conv2D(32, kernel_size=(1, 1), activation='relu', input_shape=input_shape))
            cnn4.add(BatchNormalization())
            
            cnn4.add(Conv2D(32, kernel_size=(1, 1), activation='tanh'))
            cnn4.add(BatchNormalization())
            cnn4.add(MaxPooling2D(pool_size=(1, 1)))
            cnn4.add(Dropout(0.25))
            
            cnn4.add(Conv2D(64, kernel_size=(1, 1), activation='tanh'))
            cnn4.add(BatchNormalization())
            cnn4.add(Dropout(0.25))
            
            cnn4.add(Conv2D(128, kernel_size=(1, 1), activation='tanh'))
            cnn4.add(BatchNormalization())
            cnn4.add(MaxPooling2D(pool_size=(1, 1)))
            cnn4.add(Dropout(0.25))
            
            cnn4.add(Flatten())
            
            cnn4.add(Dense(512, activation='tanh'))
            cnn4.add(BatchNormalization())
            cnn4.add(Dropout(0.25))
            
            cnn4.add(Dense(128, activation='tanh'))
            cnn4.add(BatchNormalization())
            cnn4.add(Dropout(0.25))
            
            cnn4.add(Dense(1))
            
            cnn4.compile(loss='mean_squared_error',
                          optimizer='adam',
                         metrics=['accuracy'])
            print("Fitting the model X")
            #cnn4.compile(optimizer = 'adam',loss = 'mean_squared_error',metrics=['accuracy'])
            train_embeds=train_embeds.reshape(train_embeds.shape[0],1,input_shape[1],1)
            print(train_embeds.shape)
            cnn4.fit(train_embeds,train_labels_x,batch_size=32,epochs=100, verbose=1)
            #all_x=poly_for_x.predict(poly.fit_transform(all_embeds))
            PRE=cnn4.predict(test_embeds)
            
            plt.plot(test_labels_x,color='red',label='RealDATA')
            plt.plot(PRE,color='blue',label='predictedDATA')
            plt.legend()
            plt.show()
            '''i=0
            for val in PRE:
                print(str(val)+" "+str(test_labels_x[i]))
                i=i+1
                if i==5:
                    break
            
            print("Done for X-Axis")
            
            
            Model = Sequential()

            # Adding the input layer and the first hidden layer
            Model.add(Dense(512, activation = 'relu', input_dim = 256))
            
            # Adding the second hidden layer
            Model.add(Dense(units = 128, activation = 'relu'))

            # Adding the third hidden layer
            Model.add(Dense(units = 64, activation = 'relu'))
            Model.add(Dense(units = 128, activation = 'relu'))
            Model.add(Dense(units = 32, activation = 'relu'))
            Model.add(Dense(units = 32, activation = 'relu'))
            # Adding the output layer
            Model.add(Dense(units = 1))
            print("Fitting the model X")
            Model.compile(optimizer = 'adam',loss = 'mean_squared_error',metrics=['accuracy'])
            
            Model.fit(train_embeds,train_labels_y,batch_size=32,epochs=100, verbose=1)
            #all_x=poly_for_x.predict(poly.fit_transform(all_embeds))
            PRE_y=Model.predict(test_embeds)
            
            plt.plot(test_labels_y,color='red',label='RealDATA')
            plt.plot(PRE_y,color='blue',label='predictedDATA')
            plt.legend()
            plt.show()
            i=0
            for val in PRE_y:
                print(str(val)+" "+str(test_labels_y[i]))
                i=i+1
                if i==5:
                    break
            print("Done for Y-Axis")
            fig=plt.figure()
            #plt.scatter(all_labels_x,all_labels_y,color='blue',s=1)
            plt.scatter(PRE,PRE_y,color='red',s=0.5)
            plt.xlabel('X-Coordinate')
            plt.ylabel('y-Coordinate')
            plt.show()
            fig.savefig('plot_C4__ALL_LABELS.png',dpi = 1200)    
            import math
            data = zip(PRE, PRE_y, all_labels_x, all_labels_y)
            distance_data = [ math.sqrt( (x1-x2)**2 + (y1-y2)**2 ) for x1,y1,x2,y2 in data]
            print("MEAN = "+ str(np.mean(distance_data)))
            print("MINIMUM = "+str(np.min(distance_data)))
            print("MAXIMUM = "+str(np.max(distance_data)))
            print("MEDIAN = "+ str(np.median(distance_data)))
            print("STANDARD DEVIATION = "+ str(np.std(distance_data))) 
            from scipy import stats
            print("MODE = "+ str(stats.mode(distance_data)))
            print("Geometric mean = "+ str(stats.gmean(distance_data)))
            print("Harmonic mean = "+ str(stats.hmean(distance_data)))
            
            fig=plt.figure()
            plt.plot(distance_data)
            plt.plot(np.mean(distance_data), color='red')
            plt.xlabel("No. of Nodes")
            plt.ylabel("difference b/w predicted and actual values")
            plt.show()
            fig.savefig("ERROR_C4_for_all_labels_Iter.png")
            
            #fig.savefig("ERROR_range.png")
            fig=plt.figure()
            plt.hist(distance_data, bins='auto')
            plt.xlabel("Euclidian Distance")
            plt.ylabel("number of data points in range")
            plt.show()
            fig.savefig("Euclidian_C4_for_all_lables_Iter.png")'''
            cnts=cnts+0.001
            cnts=round(cnts,4)
            break
            
        cntf=cntf+0.25
        cntf=round(cntf,2)
        break
    break
    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                