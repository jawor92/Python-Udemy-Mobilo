# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:15:26 2019

@author: Mateusz.Jaworski
"""

number = 1
previousNumber = 0

while number <= 50:
    print(previousNumber , '+' , number , '=' , number + previousNumber)
    previousNumber = number
    number+=1