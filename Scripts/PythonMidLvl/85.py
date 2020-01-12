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
        
    def show_info(self):
        
        print('Name of product: {}'.format(self.name.upper()))
        print('Kind: {}'.format(self.kind))
        print('Taste: {}'.format(self.taste))
        
        if len(self.addictions) > 0:
            print('Addictions:')
            for x in self.addictions:
                print('{}'.format(self.addictions))
        else:
            print('No addictions')
        
        if len(self.filling) > 0:
            print('Fillling:')
            for x in self.filling:
                print('{}'.format(self.filling))
        else:
            print('No fillings')
            
    def set_filling(self, filling):
        self.filling = filling
        
    def add_addictions(self, addictions):
        self.addictions = addictions
        
        

        
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], ' ')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')

bakery = []

bakery.append(cake01)
bakery.append(cake02)
bakery.append(cake03)

cake02.set_filling('cream')
cake03.add_addictions(['coco','chocko'])

print('Today is offer:')
print('\n')
for x in bakery:
    x.show_info()
    print('-'*10)