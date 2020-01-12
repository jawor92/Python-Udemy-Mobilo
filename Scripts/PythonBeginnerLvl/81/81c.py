# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:25:34 2019

@author: Mateusz.Jaworski
"""

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i = 0
imax = len(texts) - 1

while i < imax:
    print(i, texts[i], texts[i+1])
    if len(texts[i]) == len(texts[i+1]):
        print('\tFound:', texts[i], '=',len(texts[i]), texts[i+1], '=', len(texts[i+1]))
    i+=1