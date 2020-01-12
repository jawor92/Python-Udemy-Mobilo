# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:58:37 2019

@author: Mateusz.Jaworski
"""
import sys

file_path = r'C:\\Users\\Mateusz.Jaworski\\Desktop\\Prywatne\\Python\\179\\orders.csv'
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        try:
            pharmace = order[0]
            item = order[1]
            amount = int(order[2])
            
            print('Order from drugstore "%s", item "%s", amount %d' % (pharmace, item, amount))
        
        except:
            print('Issue with %s' % line)
            print('Type of issue: %s' % sys.exc_info, [0])
 
print("Processing finished")


