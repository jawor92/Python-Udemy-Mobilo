# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:43:17 2020

@author: Mateusz.Jaworski
"""

class Memory:
    
    def __init__(self, list):
        self.list_of_items = list
        
mem = Memory([])

print('List of items: {}'.format(mem.list_of_items))

mem.list_of_items.append('test')

print('List of items: {}'.format(mem.list_of_items))