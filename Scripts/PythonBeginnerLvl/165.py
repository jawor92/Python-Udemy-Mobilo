# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:09:00 2019

@author: Mateusz.Jaworski
"""

import os
import time
import datetime

print('Current directory is: ', os.getcwd())

currentDir = os.getcwd()
filename = '165.py'
fullpath = os.path.join(currentDir,filename)
print(fullpath)

relativePath = '157.py'
print('\nThe absolute path is: ', os.path.abspath(relativePath))

print('\nIs file existing? ', os.path.exists(relativePath))

if os.path.exists(relativePath):
    
    print('\n Last modify data is: ', os.path.getatime(relativePath))
    print('\n Last modify data is: ', time.localtime(os.path.getctime(relativePath)))
    print('\n Last modify data is: ', time.localtime(os.path.getmtime(relativePath)))
    print('\n Last modify data is: ', time.localtime(os.path.getatime(relativePath)))