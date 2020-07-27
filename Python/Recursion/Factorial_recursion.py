'''
Created on 27-Jul-2020

@author: dibyajyoti
'''

def factorial(result,number):
    if number == 0:
        return result
    result=result*number
    return factorial(result,number-1)
print(factorial(1,5))
