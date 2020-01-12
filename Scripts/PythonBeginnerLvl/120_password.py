# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:35:55 2019

@author: Mateusz.Jaworski
"""

import random

ints = range(33,127)
password = ''

for i in range(10):
    password += chr(random.choice(ints))
print(password)