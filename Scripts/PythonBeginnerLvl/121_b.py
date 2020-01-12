# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:08:53 2019

@author: Mateusz.Jaworski
"""

import random

min = 1
max = 6

dices = []

for i in range(5):
    dices.append(random.randint(min,max))

dices.sort()
print(dices)    