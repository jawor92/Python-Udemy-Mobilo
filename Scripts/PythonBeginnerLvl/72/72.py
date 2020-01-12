# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:16:34 2019

@author: Mateusz.Jaworski
"""

likes = 500
sharing = 100

numlikes = 300
numsharing = 900

if numlikes >= likes and numsharing >= sharing:
    print('sprzedaz znizkowa')
else:
    if numlikes < likes and numsharing >= sharing:
        print('za malo likeow')
    else:
        print('za malo sharingow')
                 
                 

                    
                        