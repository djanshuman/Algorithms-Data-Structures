def Hashing(hashTable):
    
    for i in range(len(hashTable)):
        print(i)
        for j in hashTable[i]:
            print("-->", end = " ") 
            print(j)
            
def find_key(key):
    return key%len(hashTable)


def insert(hashTable,key,value):
    key_1=find_key(key)
    hashTable[key_1].append(value)
    
    
hashTable=[]
for i in range(10):
    hashTable.append([])


#insert(hashTable, 10, "Delhi")
#insert(hashTable, 20, "bhubaneswar")
#insert(hashTable, 66, "Ahmedabad")
#insert(hashTable, 43, "Kolkata")
insert(hashTable, 10, 'Allahabad') 
insert(hashTable, 25, 'Mumbai') 
insert(hashTable, 20, 'Mathura') 
insert(hashTable, 9, 'Delhi') 
insert(hashTable, 21, 'Punjab') 
insert(hashTable, 21, 'Noida') 
Hashing(hashTable)
