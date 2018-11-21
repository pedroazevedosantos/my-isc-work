#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 5: Inputs and Outputs

@author: user01
"""

import struct

#%% Read and Print a File 

filename='../python/exercises/example_data/weather.csv'

with open(filename) as reader:
    data=reader.read()
    
print("Length of the file:")    
print(len(data))

print("Contents of the file:")    
print(data)


#%% Read the file line by line
filename='../python/exercises/example_data/weather.csv'
with open(filename) as reader3:
    line=reader3.readline()
    while line !='':
        print(line)
        line=reader3.readline()
    if line == '':
        print("it's over!")

#%% Read, convert and write out rainfall data
     
rain=[]
with open(filename) as reader2:
    header=reader2.readline()
    for line in reader2.readlines():
        r=line.strip().split(",")[-1]
        r=float(r)
        rain.append(r)

print(rain)

with open("myrainfall.txt",'w') as writerain:
    for i in rain:
        writerain.write(str(i) + "\n")
        
#%% Pack and read/write binary files !

bin_data=struct.pack("bbbb",123,12,45,34)

filename2='mybunary.dat'
with open(filename2,'wb') as file_object:
    file_object.write(bin_data)
    
    
with open(filename2,'rb') as file_object:
    bin_data2=file_object.read()

data=struct.unpack("bbbb",bin_data2)
print(data)
