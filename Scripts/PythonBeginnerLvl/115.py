# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:36:35 2019

@author: Mateusz.Jaworski
"""

import math

degree1 = 360

radian=pi*degree/180

print("%d degree is %f radians" % (degree1, radian))

degree2 = 45

radian=pi*degree/180

print("%d degree is %f radians" % (degree2, radian))

math.radians(degree1)
math.radians(degree2)
print('%d, %d' % (math.radians(degree1), math.radians(degree2)))

small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38
small_pizza_price = 11.5
big_pizza_price = 15.6
family_pizza_price = 22

area_small = pi * pow(small_pizza_r,2)
m_price_small = area_small / small_pizza_r
print('Powierzchnia malej pizzy:', area_small, 'm2.')
print('Cena 1m2 pizzy small wynosi:', m_price_small)