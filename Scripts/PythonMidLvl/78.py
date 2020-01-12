# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:31:29 2020

@author: Mateusz.Jaworski
"""

car01 = {
        'carBrand' : 'Seat',
        'carModel' : 'Ibiza',
        'carIsAirBagOK' : True,
        'carIsPaintingOK' : True,
        'carIsMechanicOK' : True
        }

car02 = {
        'carBrand' : 'Opel',
        'carModel' : 'Corsa',
        'carIsAirBagOK' : True,
        'carIsPaintingOK' : False,
        'carIsMechanicOK' : True
        }

def isCarDamage(func):
    return not (func['carIsAirBagOK'] and func['carIsPaintingOK'] and func['carIsMechanicOK'])

print(isCarDamage(car01))
print(isCarDamage(car02))

car_list = [car01, car02]

for x in car_list:
    print('{} {}, is damaged: {}'.format(x['carBrand'], x['carModel'], x['carIsPaintingOK']))