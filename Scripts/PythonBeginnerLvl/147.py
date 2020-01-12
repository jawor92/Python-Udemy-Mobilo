# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:40:02 2019

@author: Mateusz.Jaworski
"""

def WorkingDay(year,month,day):

    from datetime import date
    from datetime import timedelta
    
    day = date(year,month,day)
    
    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday=day
    
    print('working day for', day,'is', workingday)
    
    return

WorkingDay(2020, 12, 3)
WorkingDay(day=25, year=1992, month=1)
    