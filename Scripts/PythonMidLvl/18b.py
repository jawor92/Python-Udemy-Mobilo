# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:25:28 2019

@author: Mateusz.Jaworski
"""

instruction = ['hello', 'borrow money', 'thanks', ' bye']

instructionaproved = []

i=0

while i < len(instruction):
    instructionaproved.append(instruction[i])
    print('Lista:', instruction[i])

    
    if instruction[i] == 'abort':
        print('Aborting!')
        instructionaproved.clear()
        break
    i+=1
    
else:
    print('Lista cala:', instructionaproved)