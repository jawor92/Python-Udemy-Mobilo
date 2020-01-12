# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:19:21 2019

@author: Mateusz.Jaworski
"""

while True:
    
    filesizeStr = input ('Enter the max file size (MB): ')
    
    if filesizeStr.isdecimal():
        filesizeInt = int(filesizeStr)
        break

print('The max size is: %d' % (filesizeInt)) \

print('Size in KB is %d' % (filesizeInt * 1024))

