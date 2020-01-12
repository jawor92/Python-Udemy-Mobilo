# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:09:49 2020

@author: Mateusz.Jaworski
"""

class MailToSantaClaus:
 
    def __init__(self, presents):
        self.presents = presents.copy()
 
    def show_presents(self):
        print(self.presents)
 
mail = MailToSantaClaus(['Teddy Bear', 'Teddy Bear House'])

mail.show_presents()