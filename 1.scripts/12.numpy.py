#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Numpy INTRO

@author: user01
"""

import numpy as np


#%% Create and inspect a ndarray

a=np.zeros((2,3,4))

b=np.ones((2,3,4))

c=np.arange(0,999)

#Understand a multi-dimensional array as (time,level,lon,lat)
d=np.arange(8000).reshape(10,2,20,20)

#%% Array calculations and operations


aa=np.array([range(4),range(10,14)])

bb=np.array([2,-1,1,0])

arr=np.array([range(0,10)])

#Array comparison
answer1=arr>3
answer2=np.greater(arr,3)
answer3=np.logical_not(arr<=3)

answer4=np.logical_or(arr<3,arr>8)

#Apply an operation on the array based on a condition
answer5=np.where(np.logical_or(arr<3,arr>8),arr*5,arr*-5)


#%% Function to calculate wind vector magnitude

def windmag(uarray,varray):
    windmag=((uarray**2)+(varray**2))**0.5
    windmag=np.where(windmag<0.1,0.1,windmag)
    return windmag
    
#%% Assess wind component fields
    
u=np.array([[4,5,6],[2,3,4]])
v=np.array([[2,2,2],[1,1,1]])

U=windmag(u,v)

u2=np.array([[4,5,0.01],[2,3,4]])
v2=np.array([[2,2,0.03],[1,1,1]])

U2=windmag(u2,v2)

