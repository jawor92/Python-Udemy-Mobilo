# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:56:00 2019

@author: Mateusz.Jaworski
"""

'''def Do(action, param):
    print(action)
    print(param)
    return

Do('buy', 'shoe')

def Do2(action, *param):
    print(action)
    print(param)
    for x in param:
        print('param is:', x)
    return

Do2('buy', 'shoe', 'sock')'''

def Do3(action, what, **param):
    print(action)
    print(what)
    print(param)
    for x in param:
        print(x, '=', param[x])
    return

Do3('buy', 'shoe', size = 45, color = 'black', type = 'sport')