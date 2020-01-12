# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:54:58 2019

@author: Mateusz.Jaworski
"""
import os

def lab13(path):
    
    with open(path, 'r', encoding='utf-8') as plik:
        
        zdanie = plik.read()
        
        podziel = zdanie.split()
        
        suma = len(podziel)
    
    return suma

path = r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\kurs Python 2 SZ\13\test.txt'

if os.path.isfile(path):
    
    print('Plik ma {0} wyrazy. Sciezka do pliku: {1}'.format(lab13(path), path))