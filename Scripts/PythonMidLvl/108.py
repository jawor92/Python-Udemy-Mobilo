# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:18:39 2020

@author: Mateusz.Jaworski
"""

import random

class MemoryClass:
    
    list_of_already_items = []
    
    def __init__(self, func):
        
        print('>>>> this is an init of MemoryClass')
        
        self.func = func

cars = ['Opel', 'Toyota', 'Fiat', 'Ford', 'Renault', 'Mercedes', 'BMW', 'Peugeot', 'Porsche', 'Audio', 'VW', 'Mazda']

@MemoryClass
def SelectTodayPromotion(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectTodayShow(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectFreeAccesories(list_of_cars):
    return random.choice(list_of_cars)

print('Promotion: {}'.format(SelectTodayShow(cars)))
print('Show: {}'.format(SelectTodayShow(cars)))
print('Free accesories: {}'.format(SelectFreeAccesories(cars)))