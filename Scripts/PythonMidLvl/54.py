# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 16:59:52 2019

@author: Mateusz.Jaworski
"""

def Bake(what):
    print('Baking {}'.format(what))

def Add(what):
    print('Adding {}'.format(what))
    
def Mix(what):
    print('Mixing {}'.format(what))
    
cookbox = [(Add, 'milk'), (Add,'fruits'), (Mix, 'all igridients'), (Bake, 'all baking')]

for activity, obj in cookbox:
    activity(obj)


print('-'*30)

def Cook(activity, obj):
    activity(obj)
    
for activity, obj in cookbox:
    Cook(activity, obj)
    
