# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 12:59:09 2019

@author: Mateusz.Jaworski
"""

instruction = ['hello', 'borrow money', 'thanks',' bye']

instructionaproved = []

for x in instruction:
    instructionaproved.append(x)
    print("Instructions: ", x)
    
    if x == 'abort':
        print('Aborting!')
        instructionaproved.clear()
        break
    
else:
    print('List of instructions approved: ', instructionaproved)
