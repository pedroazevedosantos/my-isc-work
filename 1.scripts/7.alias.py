#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 7: Alias

@author: user01

This exercise only wants to present the objective of copy.deepcopy

"""

import copy

#%% Without deepcopy

a=[0,1,2]

#%% With deepcopy

b=a

c=copy.deepcopy(a)

b[0]=1
print(a,b)
c[0]=2
print(c,a)