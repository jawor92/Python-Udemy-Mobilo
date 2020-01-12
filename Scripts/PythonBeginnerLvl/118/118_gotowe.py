# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:50:11 2019

@author: Mateusz.Jaworski
"""

import random

number1 = random.randint(1,100)
print("The first generated number is %d" %(number1))
 
counter = 1
number2 = random.randint(1,100)
 
while number1 != number2:
    counter+=1
    number2=random.randint(1,100)
    print(counter, number2)
    
print("I needed %d attempts to generate %d again" % (counter, number1))