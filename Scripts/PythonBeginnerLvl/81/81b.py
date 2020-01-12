# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:09:04 2019

@author: Mateusz.Jaworski
"""

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0 
imax = len(numbers)-2

while i < imax:
    print(i, numbers[i], numbers [i+1], numbers [i+2])
    if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:
        print('\tFound:', numbers[i], numbers [i+1], numbers [i+2])
    i+=1
        
