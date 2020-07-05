'''
Created on 05-Jul-2020

@author: dibyajyoti
'''
'''Queue Implementation using LinkedList'''

class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
        
class QueueLinkedList:
    
    def __init__(self):
        self.front=self.rear=None
        self.length=0
        
    def isEmpty(self):
        if(self.front==None):
            return True
        
    def enqueue(self,e):
        node=Node(e)
        
        if(self.rear==None):
            self.rear=self.front=node
            self.length+=1
            
        else:
            self.rear.next=node
            self.rear=node
            self.length+=1
    
     
    def dequeue(self):
        
        if(self.isEmpty()):
            return "Empty Queue"
        
        if(self.front==self.rear):
            temp=self.front.data
            self.rear=self.front=None
            self.length-=1
            return temp
            
        else:
            temp=self.front
            self.front=self.front.next
            self.length-=1
            return temp.data
            
        if(self.front==None):
            self.rear=None
            
    def display(self): 
        if(self.isEmpty()!=True):
            currValue=self.front
            list1=[]
            while(currValue!=None):
                list1.append(currValue.data)
                currValue=currValue.next
            print(list1,"->",self.length)
        else:
            print("Empty Queue")
    
    def peek(self):
        return self.front.data
    
myQueue=QueueLinkedList()
myQueue.enqueue("JOY")
myQueue.enqueue("MATT")
myQueue.enqueue("PAVEL")
#myQueue.enqueue("SAMEER")
#myQueue.display()
print(myQueue.dequeue())
print(myQueue.dequeue())
myQueue.display()
#print(myQueue.peek())
        
        
