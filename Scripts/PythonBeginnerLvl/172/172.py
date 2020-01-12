# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:34:05 2019

@author: Mateusz.Jaworski
"""

file=open("C:\\Users\\Mateusz.Jaworski\\Desktop\\Prywatne\\Python\\172\\test.txt", "r", encoding="utf-8")

content = file.read()

print(content)

file.close()

with open("C:\\Users\\Mateusz.Jaworski\\Desktop\\Prywatne\\Python\\172\\test.txt", "r", encoding="utf-8") as file:
    content2 = file.read()
    print(content2)
    