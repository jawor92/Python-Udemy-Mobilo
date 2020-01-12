# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:38:16 2020

@author: Mateusz.Jaworski
"""

import requests
import os
import shutil
 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)

url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'

tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

save_url_to_file(url, file_path)

try:
    if os.path.exists(tmpfile_path):
        print('Removing: {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    
    print('Downloading: {}'.format(url))
    save_url_to_file(url, file_path)
    
    print('File path: {}'.format(file_path))
    shutil.copy(tmpfile_path, file_path)
        
except Exception as e:
    print('Error. Details: \n{}'.format(e))

finally: 
    print('End of excersie')
    
    
x=1/9,5