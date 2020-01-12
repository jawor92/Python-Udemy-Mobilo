# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:24:13 2019

@author: Mateusz.Jaworski
"""

initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year = 0
capital = initialCapital

while year < maxTimeYears:
    year+=1
    
    capital = (1 + percent) * capital
    roundedCapital = round(capital,2)
    print('Kwota odestki + kapitał po roku', year, 'wynosi', roundedCapital)
    print('Odestki po roku:', year, 'wynosza', round(roundedCapital - initialCapital,2))
    
print('Kwota zarobiona w ciągu 10 lat w banku:', round(roundedCapital - initialCapital,2))
    