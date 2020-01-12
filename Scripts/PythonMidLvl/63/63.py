# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:31:30 2019

@author: Mateusz.Jaworski
"""

def CreateFuncWithWrapperLogFile(logFile):
    def CreateFuncWithWrapper(func):
        def func_wrapper(*args, **kwargs):
            
            file = open(logFile, 'a')
            
            file.write('Name of employer: {}'.format(args[0]))
            
            file.write('\n')
            
            file.write('Salary: {}'.format(args[1]))
            
            file.write('\n')
            
            file.write(' '.join('{} = {}'.format(x,y) for (x,y) in kwargs.items()))
            
            file.write('\n')
            
            result = func(*args, **kwargs)
            
            file.close
            
            return result
        
        return func_wrapper
    
    return CreateFuncWithWrapper
            

@CreateFuncWithWrapperLogFile(r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\PythonMidLvl\Scripts\63salary.txt')
def ChangeSalary(employer, salary, isbonus = False):
    print('Nazwisko {}. Pensja: {}. Premia: {}'.format(employer, salary, isbonus))
    return 

@CreateFuncWithWrapperLogFile(r'C:\Users\Mateusz.Jaworski\Desktop\Prywatne\PythonMidLvl\Scripts\63position.txt')
def ChangePosition(employer, position):
    print('Nazwisko: {}. Pozycja: {}.'.format(employer, position))
    return

print(ChangeSalary('Kowalski', 2000, isbonus = True))

print(ChangeSalary('Nowak', 5000, isbonus = False))

print(ChangePosition('Golda','Starszy sprzedawca'))

print(ChangePosition('Jaworski','Szef'))


