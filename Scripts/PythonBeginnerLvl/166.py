# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:51:59 2019

@author: Mateusz.Jaworski
"""

import os
import time
import datetime


dir = input('Please input dir filepath: ')

if not os.path.isdir(dir):
    print('it is not a dir catalog')
else:
    file = input('Please input filename: ')
    
fullpath = os.path.join(dir,file)

print(fullpath)

if os.path.exists(fullpath):
    
    print('Last modification: ', time.localtime(os.path.getmtime(fullpath)))
    print('File size in KB: ', os.path.getsize(fullpath))
    print('Dir: ', os.getcwd())
    print('Relative path: ', os.path.relpath(fullpath))
