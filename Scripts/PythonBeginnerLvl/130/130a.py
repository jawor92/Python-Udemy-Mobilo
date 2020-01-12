# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 08:16:45 2019

@author: Mateusz.Jaworski
"""

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

import math

print('In list "inputdata" are', len(inputdata), 'elements.')
print('In list "factor table" are', len(factortable), 'elements.')
if len(inputdata) == len(factortable):
    i=0 
    while i < len(inputdata):

        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print('Min Value =', minvalue,'Max Value =', maxvalue)

        
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger)
        print(maxinteger)
        print(inputdata[i])
        i+=1

else:
    print('inputdata and factortable need to have equal number of elements')


    