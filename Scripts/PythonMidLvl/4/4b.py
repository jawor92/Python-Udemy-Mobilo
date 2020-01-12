# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:20:22 2019

@author: Mateusz.Jaworski
"""

a=b=c=[1,2,3]

print(a, id(a))
print(b, id(b))
print(c, id(c))

a.append(4)

print(a, id(a))
print(b, id(b))
print(c, id(c))