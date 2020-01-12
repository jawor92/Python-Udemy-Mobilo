# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:05:40 2019

@author: Mateusz.Jaworski
"""

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for proj, lead in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(proj, lead))
    
print('-'*15)

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for proj, date, lead in zip(projects, dates, leaders):
    
    print('The leader of "{}" project, started {} is {}'.format(proj, date, lead))
    
print('-'*15)

for i, (proj, date, lead) in enumerate(zip(projects, dates, leaders)):
    print('{}: The leader of "{}" project, started {} is {}'.format(i+1, proj, date,lead))

