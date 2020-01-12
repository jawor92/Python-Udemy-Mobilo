# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:28:38 2019

@author: Mateusz.Jaworski
"""

import os


line = input('Price for next course is: ')
value  = int(line)
    
filepath = input('Filepath: ')

try:   
    file = open(filepath, 'w+')
    file.write(line)
    file.close

except FileNotFound as e:
    print('Sorry, it is error')

