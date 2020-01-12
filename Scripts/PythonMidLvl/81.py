# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:31:29 2020

@author: Mateusz.Jaworski
"""

class Car:
    
    def __init__(self, brand, model, isAirBagOK, isPaitingOK, isMechanicOK):
        
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaitingOK = isPaitingOK
        self.isMechanicOK = isMechanicOK
        
car01 = Car('Seat', 'Ibiza', True, True, True)

car02 = Car('Opel', 'Corsa', True, True, True)

print(car01.brand, car01.model, car01.isAirBagOK)

