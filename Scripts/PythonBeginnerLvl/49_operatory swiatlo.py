# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:12:34 2019

@author: Mateusz.Jaworski
"""

isAutomaticMode = True ##pokretlo ustawioe na AUTO
is80PercentLight = False ##is 80% light or above 80%
isDirectLight = False ##direct light - light must be on
isRainy = False ##rainy, fogg etc - light must be on

turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)


print("Automatic mode:  ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
