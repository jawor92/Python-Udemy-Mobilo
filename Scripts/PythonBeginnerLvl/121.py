# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:01:41 2019

@author: Mateusz.Jaworski
"""

import random 
min = 1
max = 6

dice = random.randint(min, max)

if dice == 1:
    print('   ')
    print(' o ')
    print('   ')

elif dice == 2:
    print('  o')
    print('   ')
    print('o  ')
    
elif dice == 3:
    print('  o')
    print(' o ')
    print('o  ')
    
elif dice == 4:
    print('o o')
    print('   ')
    print('o o')
    
elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')
    
else:
    print('o o')
    print('o o')
    print('o o')