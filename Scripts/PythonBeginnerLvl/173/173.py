# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:30:57 2019

@author: Mateusz.Jaworski
"""

file_path = r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\Python\173\test.csv'

with open (file_path, 'r') as file:
    
    for line in file:
        line = line.replace('\n', ' ')
        order = line.split(',')
        
        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' % order[0], order[1], order[2])
        else:
            print("Line %s malformed!!!" % line)
            
            
