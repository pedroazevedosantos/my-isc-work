#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logging Data

@author: user01

Check USB port on the terminal

ls -F /dev/ttyUSB* /dev/serial/by*

"""
#%% Import functions
from datetime import datetime

import serial

import io

#%% Set the serial port

ser=serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
)

#%% Adjust for python 3

sio=io.TextIOWrapper(io.BufferedRWPair(ser,ser,1),encoding='ascii',newline='\r')
#For Python 3
sio._CHUNK_SIZE=1


#%% Just print temps into the terminal

# =============================================================================
# while ser.isOpen():
#     datastring=sio.readline()
#     print(datetime.utcnow().isoformat(),datastring)
#     
# 
# =============================================================================
#%% Read temps and write to file

outfile='/tmp/serial-temperature.tsv'

with open(outfile,'a') as f: #appends to existing file 
   while ser.isOpen():
      datastring = sio.readline()
      #\t is tab; \n is line separator
      f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
      f.flush() #included to force the system to write to disk

ser.close()



