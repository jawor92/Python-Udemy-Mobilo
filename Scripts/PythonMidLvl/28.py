# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:04:34 2019

@author: Mateusz.Jaworski
"""

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

listOfInt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

dict_denominations = dict(zip(banknotes_coins, listOfInt))

print(dict_denominations)

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1
 
dict_denominations[50] += 1
dict_denominations[20] += 40
dict_denominations[5] += 1
dict_denominations[2] += 2
 
dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for keys in dict_denominations:
    print('Nominal:', keys, 'Sumaryczna ilosc:', dict_denominations[keys])
    
print('-'*20)

print(dict_denominations.get(20)) #pobranie konkretnej wartoci dla key=20

