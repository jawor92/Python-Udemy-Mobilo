# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:32:09 2020

@author: Mateusz.Jaworski
"""

class Cake:
    
    def __init__(self, name, kind, taste, addictions, filling):
        
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')

bakery = []

bakery.append(cake01)
bakery.append(cake02)
bakery.append(cake03)

print('Today is offer:')
print('\n')
for x in bakery:
    print('{}, main taste: {}, with additives: {}, filled with: {}'.format(x.name, x.taste, x.addictions, x.filling))
    print('\n')


