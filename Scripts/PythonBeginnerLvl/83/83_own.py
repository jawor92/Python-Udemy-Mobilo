# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:04:19 2019

@author: Mateusz.Jaworski
"""

cargo = [40, 20, 4, 5, 30, 8, 2, 7, 3, 19, 32, 40, 20, 35, 15, 32, 9]
cargo.sort()
cargo.reverse()

print(cargo)

i = 0
boxCapacity = 90
box = [ ] 

while i < len(cargo) and (boxCapacity - sum(box)) > min(cargo):
    if (boxCapacity - sum(box)) > cargo[i]:
        box.append(cargo[i])
    i+=1

print('Suma paczki:', sum(box))
print('Paczki:', box)