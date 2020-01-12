# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 08:33:12 2019

@author: Mateusz.Jaworski
"""

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit
    return s.isdigit


a_str = input('Podaj wspolczynnik A: ')
b_str = input('Podaj wspolczynnik B: ')
c_str = input('Podaj wspolczynnik C: ')

if not ( check_int(a_str) and check_int(b_str) and check_int(c_str)):
    print('Values A, B, C must be integer')
    
else:
        
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
        
    if a == 0:
            print('a can not be as a 0')
    else:
        delta = b**2 - 4 * a * c
            
        if delta < 0:
            print('lack of solution')
        elif delta == 0:
            x1 = -b / (2*a)
            print('x1= %.2f' % x1)
        else:
            x1 = (-b-delta**0.5)/(2*a)
            x2 = (-b+delta**0.5)/(2*a)
            print("there are two solutions: %.2f and %.2f" % (x1,x2))

