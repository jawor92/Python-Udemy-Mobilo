# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:12:08 2019

@author: Mateusz.Jaworski
"""

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for x in data:
   Elements = x.split(':')
   if Elements[0] == 'Error':
       print(Elements[0].upper())
       print(Elements[1].lower())
   else:
        print('No error in list Element0')