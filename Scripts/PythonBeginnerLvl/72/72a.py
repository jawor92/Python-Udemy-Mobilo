# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:30:52 2019

@author: Mateusz.Jaworski
"""

likes = 500
shares = 100

minlikes = 1666
minshares = 1666

if minlikes >= likes and minshares >= shares:
    print('sprzedaz')
elif minlikes < likes and minshares >= shares:
    print('za malo likeów')
elif minlikes >= likes and minshares < shares:
    print('malo sharow')
else:
    print('za malo like i sharow')