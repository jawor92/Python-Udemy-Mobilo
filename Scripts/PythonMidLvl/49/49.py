# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:29:01 2019

@author: Mateusz.Jaworski
"""

def calculate_paint(efficency_ltr_per_m2, *rooms):
    sum_rooms = sum(rooms)
    
    x = sum_rooms / efficency_ltr_per_m2
    
    print(x)
    return x

rooms = [10,15,25]

calculate_paint(0.25, *rooms)


print('-'*30)

