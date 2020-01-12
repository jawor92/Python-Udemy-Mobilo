# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 18:25:37 2020

@author: Mateusz.Jaworski
"""

import os
import functools
from datetime import datetime as dt

def wrapper_wtih_log_file(logged_action, log_file_path):
    
    def wrapper_with_log_to_known_file(func):
        
        def the_real_wrapper(path):
            
            file = open(path, 'a')
            
            if create_file == True:
                
                file.write('Action FILE_CREATE executed on {} on {}'.format(path, dt.datetime.now()))
            
            else:
 
                file.write('Action FILE_DELETED executed on {} on {}'.format(path, dt.datetime.now()))
            
            
            return path
        
        return the_real_wrapper
    
    
    return wrapper_with_log_to_known_file
 
@wrapper_wtih_log_file
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")

@wrapper_wtih_log_file
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)
 
 
create_file(r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\PythonMidLvl\Scripts\64\dummy_file.txt')
delete_file(r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\PythonMidLvl\Scripts\64\dummy_file.txt')
create_file(r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\PythonMidLvl\Scripts\64\dummy_file.txt')
delete_file(r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\PythonMidLvl\Scripts\64\dummy_file.txt')

