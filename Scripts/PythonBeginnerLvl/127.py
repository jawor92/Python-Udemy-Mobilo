# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 09:26:58 2019

@author: Mateusz.Jaworski
"""

import time

print(time.time())

print(time.asctime(time.localtime(time.time())))

import calendar

print(calendar.month(1992,10))

calendar.setfirstweekday(6)

print(calendar.month(1992,10))

print(calendar.isleap(2020))

print(calendar.month(2019,12))