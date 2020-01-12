# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:52:04 2019

@author: Mateusz.Jaworski
"""

persons = ['Elizabeth', 'Anna', 'John']

domain = 'bentley.com'

for person in persons:
    email = person + '@' + domain
    print('Mail for\t', person, '\tis\t', email)
else:
    print('--- End of list ----')