'''
Created on 14-Jun-2020

@author: dibyajyoti
'''

def PrintRecur(arr1):
    dict1=dict()
    for i in arr1:
        if i not in dict1.keys():
            dict1[i]=True
        else:
            return i
    
    return "Undefined"

arr1=[2,5,5,2]
print(PrintRecur(arr1))
#O(n)

