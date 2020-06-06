'''
Created on 07-Jun-2020

@author: dibyajyoti
'''
''' Implementing stack using List having fixed capacity to avoid amortized '''

class Empty(Exception):
    ''' Raise Error message for stack class'''
    pass

class Stack:
    
    def __init__(self,max_size):
        self._max_size=max_size
        self._elements=[None]*self._max_size
        self._top=-1
    
    def get_max_size(self):
        return self._max_size
    
    def isEmpty(self):
        if(self._top < 0):
            return True
        return False
    
    def push(self,e):
        if(self._top == self.get_max_size()-1):
            raise Empty("Stack is full")
        self._top+=1
        self._elements[self._top]=e
        
    def pop(self):
        if(self.isEmpty()):
            raise Empty("Stack is Empty")
        x=self._elements[self._top]
        self._top-=1
        self._elements[-1]=None
        return x
    
    def top(self):
        if(self.isEmpty()):
            raise Empty("Stack is Empty")
        return self._elements[self._top]
    
    def display(self):
        return self._elements

s=Stack(5)
s.push(10)
s.push(20)
print(s.display())
print(s.pop())
print(s.top())
print(s.display())
print(s.pop())
#print(s.pop())
s.push(89)
s.push(90)
s.push(88)
s.push(91)
print(s.display())
s.push(101)
print(s.display())
#s.push(105)
