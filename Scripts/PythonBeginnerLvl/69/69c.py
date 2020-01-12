# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:31:51 2019

@author: Mateusz.Jaworski
"""

diskSize = 140
diskSizedUsed = 133
fileSize = 1

if fileSize + diskSizedUsed <= diskSize:
    print('Odpowiednia ilosc miejsca na dysku')
else:
    print('Brak miejsca na dysku')