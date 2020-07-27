'''
Created on 27-Jul-2020

@author: dibyajyoti
'''

def factorial_iterative(number):

    result=1
    while (number !=0):
        result=result*number
        number=number-1
    return result

print(factorial_iterative(5))
