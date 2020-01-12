# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:18:24 2019

@author: Mateusz.Jaworski
"""

from datetime import date
 
def DaysToEndOfYear(year = date.today().year,
                    month = date.today().month,
                    day = date.today().day):
    
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print('Counting from ', date_today,'days remaining', delta.days)
 
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(day = 23, month =12, year = 2023)
DaysToEndOfYear()
DaysToEndOfYear(year=2020)
DaysToEndOfYear(year=2020, month=10)
DaysToEndOfYear(day=1)