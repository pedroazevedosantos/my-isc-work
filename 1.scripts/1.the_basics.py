"""
Exploring Matplotlib

Date: Nov/2018
"""

## Import libs

import math as m

## Print strings and integers

course="python";

rating=9;

print(course + str(rating));

## Apply Pythagoras

b=3

c=4


a=m.sqrt(b**2 + c**2);

## Data Types

#a is a float while b and c are ints
print(type(a) == type(b))

a=int(a);
print(a)

print(str(a) + " squared equals " + str(b) + " squared + " + str(c) + " squared.")


