'''
Created on 16-May-2020

@author: dibyajyoti
'''

def Binary_Iterative(alist,element):
    
    l=0
    h=len(alist)-1
    
    while(l<= h):
        mid=(l+h)//2
        if(element==alist[mid]):
            return True
        else:
            if(element > alist[mid]):
                l=mid+1
            else:
                h=mid-1
    return False

alist=[5,6,45,67,100,123,879]
print(Binary_Iterative(alist, 45))
