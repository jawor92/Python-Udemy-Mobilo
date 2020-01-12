# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:10:28 2019

@author: Mateusz.Jaworski
"""

marketing = ['loayality program', 'client promotion', 'marketer reseach']

marketing.append('public relation')

marketing.insert(2,'investor relations')

emailMarketing = marketing.copy()

emailMarketing.sort()


internalEmail = ['internal communication']

emailMarketing.extend(internalEmail)

print(emailMarketing)

NewList = tuple(emailMarketing)

print(NewList)