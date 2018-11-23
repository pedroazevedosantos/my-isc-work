#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Working with masked arrays

@author: user01
"""

#%% Import functions

import numpy as np

import numpy.ma as MA

#%%

b=MA.masked_greater(np.arange(9),3)

# When writing to a file, you should use the fill_value
b.filled()

marr=MA.masked_array(data=np.arange(10),fill_value=-999)

marr[3]=MA.masked

marr

#%% Check another masekd array

narr=MA.masked_less(marr,7)

narr

narr.fill_value

type(narr.filled())


#%% Another masked array

m1=MA.masked_array(range(1,9))

m2=MA.reshape(m1,(2,4))

m3=MA.masked_greater(m2,6)

m3=m3*100

#A masked array opperated with a nparray continues to be a masked array
type(m3-np.ones((2,4)))

