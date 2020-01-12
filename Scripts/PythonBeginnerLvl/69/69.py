# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:15:45 2019

@author: Mateusz.Jaworski
"""

minlikes = 400

minshare = 100

if minlikes >= 500 and minshare >= 100:
    print('Zniżka 10% na ubrania')
else:
    print('Nie ma zniżki')