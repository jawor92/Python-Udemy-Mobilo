# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:48:04 2019

@author: Mateusz.Jaworski
"""

helloMessage='{0:s} has {1:d} {2:s}!'
print(helloMessage.format('Kinga', 1, 'animal'))

line='{0:20s} cost {1:6d} €'

print(line.format('Ice Cream', 133))
print(line.format('Trip to Venice', 119))
print(line.format('Pizza Hawai', 6))