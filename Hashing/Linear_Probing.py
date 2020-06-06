'''
Created on 28-May-2020

@author: dibyajyoti
'''

def OpenAddressing(list1):
    for i in range(0,len(list1)):
        print(i ,"->",list1[i])

def hash_calc(key):
    
    return key % len(list1)

def insert(key):
    
    # Check if list is already full
    if list1.count(-1) == 0:
        print("List is full " + str(key) + " Cannot be inserted to the array")
        
    index=hash_calc(key)
    
    #Check if key is already part of list
    if(list1[index] == key):
        print(str(key)+" Already existing in the pos")
      
    if list1[index] == -1:
        list1[index]=key
   
    else:
        while(list1[index] != -1):   
            if(list1[index] == -2 and index!=len(list1)-1):
                index+=1                 
            elif(index == len(list1)-1):
                #to circle back and find empty slot
                index=0
            else:    
                index+=1
        list1[index]=key
                
def Search(key):
        
        index=hash_calc(key)
        j=index-1
    
        if list1[index] == key:
            return "Element found at index",index
        else:
            while(list1[index] != -1 ):
                if(index ==len(list1)-1):
                    index=0
                    j=0
                else:
                    if(list1[index] == key):
                        return"found at index",index   
                    else:
                        index+=1
                        j+=1
            return "Not found"
        
def remove(key):
    index=hash_calc(key)
    j=index
    if list1[index] == key:
        list1[index] = -2
    else:
        if(j ==index):
            j=1
        while(list1[index] != -1 and j!=index):
            if(index ==len(list1)-1):
                index=1
                j=0
            else:
                if(list1[index] == key):
                    list1[index] = -2 
                    break
                else:
                    index+=1
                    j+=1
    
list1=[]
for i in range(10):
    list1.append(-1)
    
insert(10)
insert(20)
insert(90)
insert(6)
insert(99)
insert(69)
#insert(66)
insert(89)
insert(3)
OpenAddressing(list1)
remove(3)
OpenAddressing(list1)
#insert(65)
OpenAddressing(list1)
remove(99)
OpenAddressing(list1)
print(Search(69))
#remove(69)
#OpenAddressing(list1)
print(Search(20))
#remove(20)
OpenAddressing(list1)
insert(909)
OpenAddressing(list1)
print(Search(89))
remove(69)
#print("\n")
OpenAddressing(list1)
