# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:47:34 2019

@author: Mateusz.Jaworski
"""

'''import os
import urllib.request

data_dir = r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\kurs Python 2 SZ\19'

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://www.abc.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for page in pages:
    
    full_name = '{}.html'.format(page['name'])
    
    path = os.path.join(data_dir, full_name)
    
    urllib.request.urlretrieve(page['url'], path)
    
    print('{}'.format(page['name']))'''
    
    
import urllib.request
import os
 
data_dir = 'c:/temp'
pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]
 
for page in pages:
 
    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)
 
        print("Processing: {}  => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve (page["url"], path)
        print('...done')
        
    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break
 
else:
    print('All pages downloaded successfully!!!')
    

    


    
