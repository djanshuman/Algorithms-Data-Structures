'''
Created on 06-Jun-2020

@author: dibyajyoti
'''
''' Stack ADT Implementation using underlying Python List'''

class Empty(Exception):
    ''' Generates error message passed in ArrayStack class '''
    pass

class ArrayStack():
    
    def __init__(self):
        self._data=[]
    
    def __len__(self):
        return len(self._data)
    
    def push(self,e):
        self._data.append(e)
        
    def is_empty(self):
        return len(self._data) ==0
    
    def pop(self):
        if(self.is_empty()):
            raise  Empty("stack is empty")
        return self._data.pop()  
    
    def top(self):
        if(self.is_empty()):
            raise Empty("stack is empty")
        return self._data[-1]
    
s= ArrayStack()
s.push(10)
s.push(30)
s.push(890)
s.push(80)
#print(len(s))
print(s.pop())
#print(s.top())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())


