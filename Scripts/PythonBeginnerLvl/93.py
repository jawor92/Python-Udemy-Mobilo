# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:26:28 2019

@author: Mateusz.Jaworski
"""

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for x in range (0,11):
    if x %2 == 0:
        print(string_A)
    else:
        print(string_B)

print ('----- NEW -----')

for i in range (0,9):
    print(i*'x')
    
print ('----- NEW -----')

for i in range (0,9):
    if i %2 == 0:
        print(i*'x')
    else:
        print(i*'o')
