#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 4: Tuples

@author: user01
"""

#%% Creating tuples

t=(1,);

print(t[-1]);

b=tuple([x for x in range(100,201)]);

print(b[0],b[-1]);

#%% Use tuples on a loop

mylist=[23,"hi",2.4e-10]

for (count,item) in enumerate(mylist):
    print(count,item)
    
for a in enumerate(mylist):
    print(a)
    count,item=a
    print(count)
    
#%%
(x,y)=(2,3)
print(y)

#%% Managing tuples in one line

(first,middle,last)=mylist

print(first,middle,last)

(fist,middle,last)=(middle,last,first)

print(first,middle,last)


