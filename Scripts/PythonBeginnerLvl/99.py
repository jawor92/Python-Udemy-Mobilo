# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:30:40 2019

@author: Mateusz.Jaworski
"""

text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'

newText = text.split(' ')
boxText = ''
counter = 0


print(newText)

for x in range(0, len(newText)):
    
        if counter >=  20:
            
            boxText = x + ' '             
            print(boxText)
            break
        else:
            print('None')

