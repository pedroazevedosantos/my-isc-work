o#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 5: Inputs and Outputs

@author: user01
"""

import struct

#%% Define functions

def split_and_strip(line):
    values=[]
    for value in line.split(","):
        values.append(value.strip())
    return values

def read_data_file(fpath):
	"""
	Reads weather data from CSV file.
	Params:
	 - fpath: file path to CSV file
	Returns:
	 - data dictionary.
	"""
	# Main code
	data = {}

	with open(fpath, 'r') as reader:

		# Read header
		header = reader.readline()
		col_names = split_and_strip(header)
		
		# Set up dictionary for loading
		for col in col_names:
			data[col] = []

		# Read data
		for line in reader:
			data_items = split_and_strip(line)
#           Prints each line of the file
#			print(f"[INFO] Data items: {data_items}")
			
			for (index, item) in enumerate(data_items):
				col = col_names[index]
				value = item
				data[col].append(value)
				
	return data


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


#%% Work with the data with a dictionary

datadic=read_data_file(filename)

print(datadic)

