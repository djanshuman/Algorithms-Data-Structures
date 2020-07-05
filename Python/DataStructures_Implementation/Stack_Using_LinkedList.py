'''
Created on 07-Jun-2020

@author: dibyajyoti
'''
''' Implementing stack using LinkedList '''


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    
    def __init__(self):
        self.head=None
        self.length=0
    
    def get_max_size(self):
        return self.length
    
    def isEmpty(self):
        if(self.head == None):
            return True
        return False
    
    def push(self,e):
        
        node= Node(e)
        
        if(self.head == None):
            self.head=node
            self.length+=1
        else:
        
            node.next=self.head
            self.head=node
            self.length+=1
        return self.display()
        
    def pop(self):
        
        if(self.isEmpty()):
            return "Stack is Empty"
        else:
            temp=self.head
            self.head=self.head.next
            self.length-=1
            temp.next=None
            return temp.data
    
    def top(self):
        
        if(self.isEmpty()):
            return None
        else:
            return self.head.data
    
    def display(self):
        
        if(self.isEmpty()):
            return "Stack Underflow"
        else:
            list1=[]
            currValue=self.head
            while(currValue!=None):
                list1.append(currValue.data)
                currValue=currValue.next
            print(list1,"->",self.length)

s=Stack()
s.push(10)
s.push(20)
s.push(90)
s.push(190)
#print(s.top())
print(s.pop())
s.display()
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())
s.push(10)
print(s.isEmpty())
print(s.get_max_size())
s.push(90)
s.push(190)
