# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 20:36:48 2020

@author: Mateusz.Jaworski
"""

class Cake:
 
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)
        
    def __str__(self):
        return ('{} - {} - {}'.format(self.kind, self.taste, self.additives))
 
    def __iadd__(self, other):
        
        self.additives.append(other)
        
        return self
    

    
       
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

print(cake01)