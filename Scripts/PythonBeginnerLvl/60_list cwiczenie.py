# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:23:42 2019

@author: Mateusz.Jaworski
"""

hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']

hitsTitles.append('CHILD IN TIME' 'AGAIN')
hitsTitles.insert(2, 'HOTEL CALIFORNIA')
hitsTitles.insert(0, 'THE SOUND OF SILENCE')
hitsTitles.index('HOTEL CALIFORNIA')
hitsTitles.remove('HOTEL CALIFORNIA')

hitsToRead = hitsTitles.copy()

hitsToRead.reverse()

hitsToRead.sort()

hitsToRead.pop(0)

additionalSongs = ['NOTHING COMPARES 2 U' , 'WISH YOU WERE HERE']


hitsToRead.extend(additionalSongs)

print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))

hitsToRead.clear()

print(hitsToRead)

