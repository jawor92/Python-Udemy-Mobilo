# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:51:57 2019

@author: Mateusz.Jaworski
"""

cargo = [40, 20, 4, 5, 30, 8, 2, 7, 3, 19, 32, 40, 20, 35, 15, 32, 9]
cargo.sort()
cargo.reverse()
print(cargo)


boxCapacity = 90
box = []

i = 0

while i < len(cargo) and (boxCapacity - sum(box)) >= min(cargo):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

print('The coollected items sum is:', sum(box))
print('The elements are:', box)


