'''
Created on 05-Jun-2020

@author: dibyajyoti
'''

def check_anagram(str1,str2):
    
    count1=0
    dict1=dict()
    dict2=dict()
    
    if(len(str1) != len(str2)):
        return False
    else:
        for i in str1:
            dict1.update({i.lower():str1.count(i)})
        for j in str2:
            dict2.update({j.lower():str2.count(j)})
        
        
        for i in dict1.keys():
            if i in dict2 and dict1.get(i) == dict2.get(i):
                continue
            else:
                return False
        return True

str1="SilENT"
str2="LISteH"
print(check_anagram(str1, str2))
