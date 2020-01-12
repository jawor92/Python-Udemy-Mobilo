# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:01:26 2019

@author: Mateusz.Jaworski
"""

import random
my_number = random.randint(0,20)
guess = 14
trials = 0
 
print("Guess my number!")
 
while guess != my_number:
 
    guess = int(input())
    trials+=1
    
    if guess == my_number:
        print("You are right! It was:",my_number)
        print('Trial:', trials)
    elif guess>my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
        print('Trial:', trials)        
    else:
        print("Sorry- my number is greater than", guess, "Try again!")
        print('Trial:', trials)
        
