# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:03:02 2019

@author: Mateusz.Jaworski
"""

for x in range(1,5):
    for y in range(1,5):
        print(x, '*' , y, '=', x*y)
        
print('------ NEW ------')

for x in range(1,5):
    line = str(x)
    for y in range(1,5):
        line += ('\t%3d' % (x*y))
    print(line)
