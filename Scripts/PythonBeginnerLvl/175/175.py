# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:24:07 2019

@author: Mateusz.Jaworski
"""

filename = 'C:\\Users\\Mateusz.Jaworski\\Desktop\\Prywatne\\Python\\175\\output.txt'

line = 'Europe'

cities = ['Paris', 'Warsaw', 'Berlin', 'Madrid']

file = open(filename, 'w')

file.write(line)
file.write('\n')
#file.writelines(cities)

for city in cities:
    file.write(city + '\n')

file.close