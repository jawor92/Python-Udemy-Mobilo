# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:41:47 2019

@author: Mateusz.Jaworski
"""

def Animals(*animals):
    
    txt_cat = 'catcatcat'
    
    txt_dog = 'dogdogdog'
    
    txt_rat = 'ratratrat'
    
    for x in animals:
        if x == 'cat':
            print(txt_cat)
        elif x == 'dog':
            print(txt_dog)
        elif x == 'rat':
            print(txt_rat)
        else:
            print('Cannot recognize %s' % x)
    return
    
Animals('cat')


