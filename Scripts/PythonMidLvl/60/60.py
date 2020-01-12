# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:31:30 2019

@author: Mateusz.Jaworski
"""

import datetime

def CreateFuncWithWrapper(func):
    def func_with_wrapper(*args,**kwargs):
        #print('Function "{}" started at {}'.format(func.__name__, datetime.datetime.now().isoformat))
        print('Followin arguments were used:')
        print(args, kwargs)
        result = func(*args, **kwargs)
        result = args[1]
        print('Function returned: {}'.format(result))
        return result
    return func_with_wrapper


@CreateFuncWithWrapper
def ChangeSalary(employer, salary, isbonus = False):
    print('Name of employer {}. Salary: {}. Is Bonus: {}'.format(employer, salary, isbonus))
    return salary

print(ChangeSalary('Kowalski', 2000, isbonus = 'tak'))

