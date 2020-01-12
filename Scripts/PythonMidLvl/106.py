# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:00:55 2020

@author: Mateusz.Jaworski
"""

class NoDuplicates:
    
    def __init__(self):
        self.list = []
    
    def __call__(self, new_items):
        
        for x in new_items:
            if not x in self.list:
                self.list.append(x)

my_no_dup_list = NoDuplicates()

print(my_no_dup_list.list)

my_no_dup_list(['keyboard','mouse'])
print(my_no_dup_list.list)