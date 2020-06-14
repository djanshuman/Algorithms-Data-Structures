'''
Created on 11-Jun-2020

@author: dibyajyoti
'''

#from time import time
#start= time()
def CommonElements(arr1,arr2):
    
    dict1=dict()
    for i in arr1:
        dict1.update({i:True})
        #dict1[i]=True

    for j in arr2:
        if j in dict1.keys():
            return True
    return False


arr1=['a','v','b','c']
arr2=['w','f','a','q']
print(CommonElements(arr1, arr2))
#end= time()
#print((end-start)/len(arr1))
