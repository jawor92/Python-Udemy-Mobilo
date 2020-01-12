# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:58:57 2020

@author: Mateusz.Jaworski
"""
cake_01 = {
        'taste' : 'vanilia',
        'glaze' : 'chocolade',
        'text' : 'Happy Brithday',
        'weight' : 0.7
        }

cake_02 = {
        'taste' : 'tee',
        'glaze' : 'lemon',
        'text' : 'Happy Python Coding',
        'weight' : 1.3
        }
 
def show_cake_info(func):
    
    cakes = [cake_01, cake_02]
    for x in cakes:
        print('{} cake with {} glaze with text "{}" of {} kg'.format(x['taste'], x['glaze'], x['text'], x['weight']))
 
show_cake_info(cake_01)
show_cake_info(cake_02)
