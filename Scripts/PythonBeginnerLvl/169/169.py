# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:04:46 2019

@author: Mateusz.Jaworski
"""

import os
import time
import datetime

data_input_catalog = r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\Python\169\data_input'
data_output_catalog = r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\Python\169\data_output'

today = datetime.date.today()

today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))

is_input_catalog_ok = os.path.exists(data_input_catalog)
is_output_catalog_ok = os.path.exists(data_output_catalog)

is_today_output_catalog_ok = not os.path.isdir(today_output_catalog) and not os.path.isfile(today_output_catalog)

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
    
else:
    print('We can not continue!')
        
    if not is_input_catalog_ok:
            print('Input catalog %s must exist' % data_input_catalog)
    if not is_output_catalog_ok:
            print('Output catalog %s must exist' % data_output_catalog)
    if not is_today_output_catalog_ok:
            print('Today output catalog %s must exist' % today_output_catalog)

