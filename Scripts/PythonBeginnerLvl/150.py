# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:36:29 2019

@author: Mateusz.Jaworski
"""

from datetime import date
from datetime import timedelta

def WorkingDay(year = date.today().year, \
               month = date.today().month, \
               day = date.today().day):

    day = date(year, month, day)
    
    if day.weekday == 5:
        workingday = day + timedelta (days=2)
    elif day.weekday == 6:
        workingday = day + timedelta (days=1)
    else:
        workingday=day
    
    print(WorkingDay)
    
    return

WorkingDay()

