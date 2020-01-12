# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:29:55 2019

@author: Mateusz.Jaworski
"""

from itertools import combinations
 
color_list = ['red', 'orange', 'green', 'violet', 'blue', 'yellow']
 
def selected_colors(color_list, n):
    return(color_list[:n].copy())
 
for i in range (1 , len(color_list)+1):
    print(list(combinations(color_list,i)))