#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 2: Control Flow

@author: user01
"""

#%% While statement

gases=['He', 'Ne', 'Ar', 'Kr'];

count=0;

while count <4:
    item=gases[count]
    print(item + " " + str(gases.index(item)))
    count += 1;
else:
    print("Value" + str(count) + " not on the list")

#%% if statement
    
name="Lisa"

if name == "Lisa":
    print("plays saxophone")
elif name == "Bart":
    print("rides sakeboard")
else:
    print("lives in Springfield")
    

#%% Logical tests
    
x=1

if x: print(x," is True")
    
