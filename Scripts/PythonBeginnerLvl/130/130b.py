# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:54:12 2019

@author: Mateusz.Jaworski
"""

import random

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = random.random(0,1)

i=0

while i < len(inputdata):

        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print('Min Value =', minvalue,'Max Value =', maxvalue)
        i+=1

else:
    print('inputdata and factortable need to have equal number of elements')

