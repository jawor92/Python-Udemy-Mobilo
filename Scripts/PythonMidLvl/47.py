# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:06:22 2019

@author: Mateusz.Jaworski
"""

def show_progress(how_many, character = '*'):
    line = how_many * character
    print(line)
    
show_progress(10, '+')

