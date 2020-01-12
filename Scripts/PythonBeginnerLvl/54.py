# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:52:28 2019

@author: Mateusz.Jaworski
"""

message='Zalacz plik "cv.doc". Nastepnie akceptuj'

print(message.find('"')+1)

print(message[message.find('"')+1:])

temp=message[message.find('"')+1:]

print(temp[:temp.find('"')])