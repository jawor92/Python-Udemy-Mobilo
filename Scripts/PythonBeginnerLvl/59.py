# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:59:01 2019

@author: Mateusz.Jaworski
"""

countries =["fr","pl","us","ru","ru"] 


countries.append('PL')
countries.insert(2, 'spain')
countries.remove('ru')
countries.sort()
countries.reverse()
countries.pop(0)

print(countries.index('pl'))

print(countries.count('pl'))

newList = ['FIN', 'NOR']

countries.extend(newList)

newCopyList = countries.copy()

newCopyList.clear()
print(newCopyList)