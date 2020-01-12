# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:49:20 2019

@author: Mateusz.Jaworski
"""

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

for x in colors:
    for y in figures:
        aCard = f.copy()
        aCard ['Color'] = x
        allCards.append(aCard)
        
import random

random.shuffle(allCards)

player1 = []
player2 = []

player1 = allCards[:12]
player2 = allCards[12:]