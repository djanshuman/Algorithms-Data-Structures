'''
Created on 09-Feb-2021

@author: dibyajyoti
'''

'''
Stack Implementation Using LinkedList'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack:
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length=0
        
    def printStack(self):
        list1=[]
        currValue=self.top
        while(currValue):
            list1.append(currValue.data)
            currValue=currValue.next
        print(str(list1) +"-> Length:"+str(self.length))
    
    def push(self,value):
        newnode=Node(value)
        if(self.length==0):
            self.top=newnode
            self.bottom=newnode
            self.length+=1
        else:
            holdingPointer=self.top
            self.top=newnode
            newnode.next=holdingPointer
            self.length+=1
        self.printStack()
    
    def pop(self):
        
        if(self.length==0):
            return self.top
        
        elif(self.top==self.bottom):
            holdingPointer=self.bottom
            self.bottom=None
            self.top=None
            self.length-=1
            
        else:
            holdingPointer=self.top
            self.top=self.top.next
            self.length-=1
            
        return holdingPointer.data    
        
        
    def peek(self):
        if(self.length==0):
            return self.top
        else:
            return self.top.data
    

stack=Stack()
stack.push("Google")
stack.push("Udemy")
stack.push("LinKedIn")
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
stack.printStack()
print(stack.peek())
print(stack.peek())
stack.push("Uber")
stack.push("Netflix")
stack.push("Apple")
print(stack.pop())
stack.printStack()
