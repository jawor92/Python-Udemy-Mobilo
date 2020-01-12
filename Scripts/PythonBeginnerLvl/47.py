# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:08:48 2019

@author: Mateusz.Jaworski
"""

name='Mateusz'
age=27
dayInYear=365
print(name,'is',age,'years old, so it is about',365*27,'days.')

message='{0:s} is {1:d} years old ,so it is about {2:d} days.'
print(message.format('Mateusz', age, age*dayInYear))