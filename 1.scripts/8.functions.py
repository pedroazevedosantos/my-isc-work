#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 8: Functions

@author: user01
"""

#%% Define a simple function

def double_it(number):
    return 2*number

print(double_it(2.0))

print(double_it('two'))

def calc_hypo(a,b):
    if a<=0 or b<=0:
        print("Bad argument")
        return False
    else:
        hypo=(a**2+b**2)**0.5
        return hypo

print(calc_hypo(3,4))

print(calc_hypo(0,4))

