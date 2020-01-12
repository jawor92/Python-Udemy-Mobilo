# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:27:18 2019

@author: Mateusz.Jaworski
"""

persons = ['Elizabeth', 'Saura@sales.bentley.com', 'Vlad', 'Jarek', 'Mateusz@bentley.com']

domain = 'bentley.com'

emails = []


for person in persons:
    if '@' in person:
        emails.append(person)
        continue
    
    email = person + '@' + domain
    emails.append(email)
    
print(emails)
