#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 13:22:03 2018

@author: user01
"""

#%% Import
import numpy as np

import matplotlib.pyplot as plt

#scipy interpolate function!!!!! Check that!!

import scipy as sp


#%% Use LateX for the labels

plt.rc('text', usetex=True)
#plt.rc('font', family='serif')


#%% Set and plot

times=[0,0.25,0.5,0.75]

f1=plt.figure()
plt.plot(times,[1,2,3,4],'g--',times,[4,5,4,6],'r')
plt.title('Concentration of something')
plt.xlabel('Time [h]')
plt.ylabel('Concentration [-]')
plt.legend()

#plt.savefig("myfig.eps")
plt.show()


#%% Another plot


x1=np.linspace(0,5)

x2=np.linspace(0,2)

y1=np.cos(2*np.pi*x1)*np.exp(-1)

y2=np.cos(2*np.pi*x2)

plt.subplot(2,1,1)

plt.plot(x1,y1,'yo-')

plt.subplot(2,1,2)

plt.plot(x2,y2,'r.-')

plt.show()


#%% Plot with double axis

fig,ax1 = plt.subplots()

time=[0,1,2,3,4,5,6]
CO2=[250,265,272,260,300,320,389]
temp=[14.1,15.5,16.3,18.1,17.3,19.1,20.2]

ax1.plot(time,CO2,'r-')
ax1.set_ylabel("CO$_2$ [ppm]")

ax1.set_xlabel("Time step")

ax2=ax1.twinx()
ax2.plot(time,temp,'g-')
ax2.set_ylabel("Temp [$^{o}$C]")
plt.show()

