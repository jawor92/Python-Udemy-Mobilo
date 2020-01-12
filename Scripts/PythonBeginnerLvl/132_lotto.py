# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:32:57 2019

@author: Mateusz.Jaworski
"""

import random

numbers=[]

while len(numbers) < 6:
    
    number = random.randint(1,49)
    
    if number in numbers:
        print('Eliminated:', number)
        continue
    
    numbers.append(number)
    
print('Lotto:', numbers)