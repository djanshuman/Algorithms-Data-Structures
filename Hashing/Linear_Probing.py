'''
Created on 28-May-2020

@author: dibyajyoti
'''
''' Open Addressing method for Hashing . Below is the Linear probing implementation'''


def OpenAddressing(list1):
    for i in range(0,len(list1)):
        print(i ,"->",list1[i])

def hash_calc(key):
    
    return key % len(list1)

def insert(key):
    
    # Check if list is already full
    if(list1.count(-1)==0):
        print("hashtable is already full , cannot insert " +str(key))
        return
        
    index= hash_calc(key)

    if(list1[index]==key):
        print("Element "+str(key)+"already present in the hash table")
        return
        
    if(list1[index] == -1):
        list1[index]=key
        print("Element "+str(key)+" is inserted in hash table at index "+ str(index))
    else:
        while(list1[index]!= -1):
            if(index == len(list1)-1):
                index=0
            index+=1
        list1[index]=key
        print("Element "+str(key)+" is inserted in hash table at index "+ str(index))

def Search(key):
    index=hash_calc(key)  
    j=0
    if(list1[index]==key):
        print( "Element found at "+ str(index) +" , "+str(key))
        return True
    else:
        while(list1[index]!=-1 and j!=len(list1)):
            if(list1[index]==key):
                print("Element found at "+ str(index) +" , "+ str(key))
                return True
            elif(index == len(list1)-1):
                index=0
                j+=1
            index+=1
            j+=1
        print(str(key) +" not found")
        return False
    
        
def remove(key):
    
    ''' Search the element if it is present in hash table then we will proceed for remove'''
    index=hash_calc(key)
    j=0
    
    if(list1[index] == key):
        list1[index]=-2
        print("removed " + str(key)+" at index " +str(index))
    else:
        while(list1[index]!= -1 and j!=len(list1)):
            if(list1[index]==key):
                list1[index] =-2
                print("removed " + str(key)+" at index " +str(index))
                break
            elif(index == len(list1) -1):
                index=0
                j+=1
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
#insert(69)
insert(66)
insert(89)
insert(3)
print("\n")
OpenAddressing(list1)
remove(3)
OpenAddressing(list1)
insert(65)
print("\n")
OpenAddressing(list1)
remove(99)
print("\n")
OpenAddressing(list1)
Search(99)
remove(69)
print("\n")
OpenAddressing(list1)
Search(20)
Search(69)
remove(20)
print("\n")
OpenAddressing(list1)
insert(909)
insert(9091)
print("\n")
OpenAddressing(list1)
Search(1)
remove(69)
remove(99)
print("\n")
OpenAddressing(list1)
