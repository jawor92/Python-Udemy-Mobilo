# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:39:19 2019

@author: Mateusz.Jaworski
"""

import os

webaddresses = []

line = input('Please input webadress: ')

while line != ' ':
    
    webaddresses.append(line)
    
    line = input('Please add webadress: ')
    
print(webaddress)
    

dirname = os.getcwd()

filename = input('Please add filename: ')

filepath = os.path.join(dirname, filename)

file = open(filepath, 'w')

filename.write(webaddresses)

file.close

for x in webaddresses:
    file.write(webaddress + '\n')
file.close()