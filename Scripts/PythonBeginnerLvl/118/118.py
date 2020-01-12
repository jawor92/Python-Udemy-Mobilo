# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:32:41 2019

@author: Mateusz.Jaworski
"""

import random

for i in range (10):
    print(random.randint(1,100))
    

print ('----------------')

number1 = random.randint(1,100)
print('Numer 1 to: ', number1)
counter = 1
number2 = random.randint(1,100)

while number1 != number2:
    counter+=1
    number2 = random.randint(1,100)
    print(counter, number2)
    
print('Ilosc prob: ', counter, '. Libcza 1 to:', number1, '. Liczba 2 to: ', number2)

print ('-----------')

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
print(countries)
print('\n')

groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber+=1
        print('---Grupa %d---' % (groupNumber))
    print(countries[i])
    