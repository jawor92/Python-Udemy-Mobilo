# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:21:56 2019

@author: Mateusz.Jaworski
"""

def double(x):
    return 2 *x
 
def root(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2

number = 8

trans = [double, root, div2, negative]

tmp_return_value = number

for x in trans:
    x = temp_return_value
    
    tmp_return_value = x
    