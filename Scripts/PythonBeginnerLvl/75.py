# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 21:00:22 2019

@author: Mateusz.Jaworski
"""

musclePain = False
fever = False
weakness = False    
isMan = False

if musclePain and fever and weakness or  isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif not (musclePain and fever) and weakness:
    print("Just take a rest!")
else:
    print("this only cold")
