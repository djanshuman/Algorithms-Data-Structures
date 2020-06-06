'''
Created on 02-Jun-2020

@author: dibyajyoti
'''


def Search(alist,element):
    
    if(len(alist) ==0):
        return False
    else:
        mid=len(alist)//2
    
        if(alist[mid]==element):
            return True
        else:
            if(element > alist[mid]):
                return Search(alist[mid+1:], element)
            else:
                return Search(alist[:mid], element)

alist=[10,56,78,99,121,145]
print(Search(alist,78))
