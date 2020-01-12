# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:18:26 2019

@author: Mateusz.Jaworski
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:46:49 2019

@author: Mateusz.Jaworski
"""
import time

def wrapper_time(func):
    
    def a_wrapped_function(*args, **kwargs):
        
        time_start = time.time()
        
        v = func(*args, **kwargs)
        
        time_stop = time.time()
        
        print('Funkcja {} wykonana w czasie {}'.format(func.__name__, time_stop - time_start))
        
        return v
    
    return a_wrapped_function
       
@wrapper_time
def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v
    
print(get_sequence(10))
