# Derek Kunkel, ddk960, 11096287
# a6q1

# CMPT 141, Assignment 6
# Arrarys

# Continue your codes based on this starter file

import numpy as np
import csv

import math as m
def perchange(nval,row):
    lis=[]
    lis=[abs(((nval[row][i]-nval[row][i-1])/nval[row][i-1])*100) for i in range(1,5)]
    return lis
# put the csv file in the same folder as your program
f = open('age_statistics.csv', 'r')
csvreader = csv.reader(f, delimiter=',')
data = []
for row in csvreader:
    row1 = [item.replace(',', '') for item in row]  # This is used to remove the thousand separator , in each row
    data.append(row1)
print(data)

data1=[]
data2=[]
for i in range(9,len(data)):
    data1.append(data[i])
for i in range(len(data1)):
    data2.append(data1[i][1:])
    
data2 =[list(map(int,i) ) for i in data2]
age_dict={}
for i in range (len(data1)):
    age_dict[i]=data1[i][0]
    
# write your assignment based on the varaible data

data_array=np.array(data2)
print(data_array.shape)
print(data_array.size)
print(data_array.dtype)

summ=np.sum(data_array, axis=0)

largest=[]
for i in range(0,21):
    largest.append(sum(perchange(data_array,i)))
    
    
maxi=-1
idxx=0
for i in range (len(largest)):
    if maxi<largest[i]:
        maxi=largest[i]
        idxx=i
print(maxi)
print(age_dict[i-1])