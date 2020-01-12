# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:54:12 2019

@author: Mateusz.Jaworski
"""

import random
my_number = random.randint(0,20)
guess=-1
 
print("Guess my number!")
 
while guess != my_number :
 
    guess = int(input())
    
    if guess == my_number:
        print("You are right! It was:",my_number)
    elif guess>my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")