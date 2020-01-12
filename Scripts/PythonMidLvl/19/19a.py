# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:45:02 2019

@author: Mateusz.Jaworski
"""

import urllib.request
import os
 
data_dir = r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\kurs Python 2 SZ\19'
pages = [
    { 'name': 'wp',      'url': 'http://www.wp.pl/'},
    { 'name': 'onet', 'url': 'http://www.onet.abc.def.pl/' },
    { 'name': 'interia',       'url': 'http://www.interia.pl/'} ]
 
for x in pages:
    
    try:
        
        full_name = '{}.html'.format(x['name'])
        
        path_to_save = os.path.join(data_dir, full_name)
        
        urllib.request.urlretrieve(x['url'], path_to_save)
        
        print(path_to_save)
        
    except:
        print('Wrong adress {}'.format(x['name']))
        
        break
    
    
    
