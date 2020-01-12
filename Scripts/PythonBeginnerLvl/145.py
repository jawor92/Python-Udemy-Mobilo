# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:47:12 2019

@author: Mateusz.Jaworski
"""
def NewYear():
    from datetime import date
    current_day=day.today()
    current_year = current_day.year
    newyear = date(current_year,12,31)
    delta = newyear - day
    print(delta.days)
    return

NewYear()