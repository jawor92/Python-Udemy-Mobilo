# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:47:16 2019

@author: Mateusz.Jaworski
"""

workDays = [19, 21, 22, 21, 20, 22]


enumerateDays = list(enumerate(workDays))

print(enumerateDays)

for pos, value in enumerateDays:
    print('Position: ', pos, 'Value:', value)
    
print('-'*10)

months=['I', 'II', 'III', 'IV', 'V', 'VI']

monthdays = list(zip(months, workDays))

print(monthdays)

for m, d in monthdays:
    print('Months:', m, 'Days:', d)
    
print('-'*10)

for pos, (m,d) in enumerate(monthdays):
    print('Position:', pos, ', Month:', m, ', Days:', d)