# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:41:16 2019

@author: Mateusz.Jaworski
"""

colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

allCards=[]

for x in colors:
    for y in figures:
        allCards.append(x,y)
        
print(allCards)
