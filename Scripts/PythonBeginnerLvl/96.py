# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:56:58 2019

@author: Mateusz.Jaworski
"""

i = 10
result = 1

for j in range (1,11):
    result *= j
    print(i, result)
    
    
print('------NEW------')

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for x in list_noun:
    for y in list_adj:
        print(y, x)
    
    
    
