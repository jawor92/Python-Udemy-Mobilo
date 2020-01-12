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
        
    def Damaged(self):
        return not (self.isAirBagOK and self.isMechanicOK and self.isPaitingOK)
        
    def GetInfo(self):

        print('{} {}'.format(self.brand, self.model).upper())
        print('AirBag status: ----- {}'.format(self.isAirBagOK))
        print('Paiting status: ----- {}'.format(self.isPaitingOK))
        print('Mechanic status: ----- {}'.format(self.isMechanicOK))
        print('Is damaged: ----- {}'.format(self.Damaged))

        
        
car01 = Car('Seat', 'Ibiza', True, True, True)

car02 = Car('Opel', 'Corsa', True, True, True)
    

car01.GetInfo()
car01.Damaged()

