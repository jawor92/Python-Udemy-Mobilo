# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:02:56 2019

@author: Mateusz.Jaworski
"""

days = ['mon','tue','wed','thu','fri','sat','sun']

workday=days.copy()

print(workday)

workday.remove('sun')
workday.remove('sat')
print(workday)