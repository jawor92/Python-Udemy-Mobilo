# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:24:08 2019

@author: Mateusz.Jaworski
"""

for candidate in range(2,31):
    
    for divider in range(2,candidate):
        
        if candidate % divider == 0:
            
            print(candidate, 'is not prime', divider)
            break
    else:
        print(candidate, 'IS PRIME')
            