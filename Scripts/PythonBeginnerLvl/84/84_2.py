# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:41:54 2019

@author: Mateusz.Jaworski
"""

import random
my_number = random.randint(0,0)
guess = 0

print('Guess my number!')

while guess != int(input()):
    guess = int(input())
    
    if my_number == guess:
        print('Congrats')
    elif my_number < guess:
        print('Sorry- my number is smaller than your guess, Try again!')
    else:
        print('Sorry- my number is greater than your guess, Try again!')
        
        



