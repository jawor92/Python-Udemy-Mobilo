# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:08:07 2019

@author: Mateusz.Jaworski
"""

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
imax = len(numbers)-1

while i < imax:
    print(i, numbers[i], numbers[i+1])
    if numbers[i]**2 == numbers[i+1]:
        print('\tFOUND', numbers[i], numbers[i+1])
    i+=1
    
    
