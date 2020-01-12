# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:53:23 2019

@author: Mateusz.Jaworski
"""

rating = 1
 
'''if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')'''
    

print('very good' if rating == 5 else 'good' if rating == 4 else 'weak')