#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 6: Strings

@author: user01
"""

#%% Simple Example

latitude='22.7E'

longitude='2.3N'

S='Coordinates: {latitude}, {longitude}'.format(latitude,longitude)

#%% Play with Strings

S2="A sample string example"

for i in S2:
    print(i)
    
split_s2=S2.split()

print(split_s2)

for i in split_s2:
    if i.find('i')>-1:
        print("I found 'i' in " + i)

#%% Useful aspects of Strings
        
something="Completely Different"

print(dir(something))

print(something.count('t'))

print(something.find('plete'))

print(something.split('e'))

thing2=something.replace('Different','Silly')

print(thing2)
