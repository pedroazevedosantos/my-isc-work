#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 3: Lists and Slicing

@author: user01
"""

#%% Create a list

x= [x for x in range(1,6)]

#%% Manage Lists

forward=[]
backward=[]

values=["a","b","c"]

for value in values:
    forward.append(value)
    backward.insert(0,value)
    print(forward)
    print(backward)

forward.reverse()
print("Lists are equal after reverse?")
print(forward==backward)

#%% Other things

countries=["uk","usa","uk","uae"]
print(countries)
print("Number of 'uk' on the list")
print(countries.count("uk"))
