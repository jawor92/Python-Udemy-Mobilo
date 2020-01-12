# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:49:21 2019

@author: Mateusz.Jaworski
"""

def saved(*args):
    
    path = r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\PythonMidLvl\Scripts\49bplik.txt'
    
    file = open(path, "a")
    
    for x in args:
        file.write(x + ', ')
    
    file.write('\n')
    
    file.close
    
    return

saved('Starting processing forecasting')
saved('ERROR', 'Not enough data', 'invoices', '2020')


