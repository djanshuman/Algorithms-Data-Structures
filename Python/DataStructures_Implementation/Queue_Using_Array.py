'''
Created on 05-Jul-2020

@author: dibyajyoti
'''
'''Queue Implementation using Array'''

class QueueArray:
    
    def __init__(self,max_size):
        self.front=self.length=0
        self.rear=max_size-1
        self.elements=[None]*max_size
        self.max_size=max_size
        
    def isEmpty(self):
        if(self.length==0):
            print("Queue is empty")
            return True
    
    def isFull(self):
        if(self.max_size == self.length):
            print("Queue is full")
            return True
        
    def enqueue(self,e):
        
        if(self.isFull()== True):
            return
        else:
            self.rear=(self.rear+1) %self.max_size
            self.elements[self.rear]=e   
            self.length+=1  
    
                  
    def dequeue(self):
        if(self.isEmpty()== True):
            return
        else:
            print(self.elements[self.front])
            self.elements[self.front]=None
            self.front=(self.front+1)
            self.length-=1
                
    def display(self): 
        print(self.elements)
    
    def peek(self):
        return self.elements[self.front]
    
myQueue=QueueArray(5)
myQueue.enqueue("JOY")
myQueue.enqueue("MATT")
myQueue.enqueue("PAVEL")
myQueue.enqueue("JOHN")
myQueue.enqueue("ANSHUMAN")
myQueue.display()
print(myQueue.peek())
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.display()
myQueue.dequeue()
myQueue.dequeue()        
myQueue.display()
myQueue.dequeue()  
