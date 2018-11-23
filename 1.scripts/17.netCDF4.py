#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Working with NetCDF4

@author: user01
"""


#%% Import functions
import netCDF4

from netCDF4 import Dataset

import numpy as np

#%% Load data

dataset=Dataset('../python/exercises/example_data/ggas2014121200_00-18.nc')

#Check the format
print(dataset.file_format)

#Check the convention
print(dataset.Conventions)

#%% Inspect the global aspects 

print('All the global attributes:')
for attr in dataset.ncattrs():
    print(attr, '=', getattr(dataset,attr))

#%% Inspect dimensions and variables (always useful)

print('See all the dimensions:')
print(list(dataset.dimensions.keys()))

print('See all the variables:')
print(list(dataset.variables.keys()))

#%% Inspect one variable

time_var=dataset.variables['time']
print('Inspect the time variable (always a good practice)!')
print(time_var)

#%% Check another variable

sst=dataset.variables['SSTK']

print(sst)

arr=[1,0,10:20,30:35]



