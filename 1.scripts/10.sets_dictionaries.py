#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:56:45 2018

@author: user01
"""

#%% Combine sets

a=set([0,1,2,3,4,5])

b=set([2,4,6,8])

#Union
print(a|b)

#Intersection
print(a & b)

#%% Dictionaries

band=["mel","geri","victoria","mel","emma"]

#Empty dictionary
counts={}

for member in band:
    if member not in counts:
        counts[member]=1
    else:
        counts[member]+=1
    print(member,counts[member])
