'''
Created on 06-Feb-2021

@author: dibyajyoti
'''

'''
 Reverse a Doubly linked List
'''

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class ReverseDoublyLL:
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def printLinkedList(self):
        list1=[]
        currValue=self.head
        while(currValue):
            list1.append(currValue.data)
            currValue=currValue.next
        print(str(list1) +"->"+str(self.length))
 
    def prepend(self,data):
        node= Node(data)
        
        if(self.length==0):    
            self.head=node
            self.tail=node
            self.length+=1
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
            self.length+=1
        self.printLinkedList()
        
    def append(self,data):
        node= Node(data)
        
        if(self.length==0):    
            self.head=node
            self.tail=node
            self.length+=1
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
            self.length+=1
        self.printLinkedList()
        
    def insert(self,pos,data):
        if(pos==0):
            self.prepend(data)
        elif(pos >(self.length)-1):
            self.append(data)
        else:
            node=Node(data)
            counter=0
            currValue=self.head
            while(counter!=pos):
                currValue=currValue.next
                counter+=1
            leader=currValue.prev
            leader.next=node
            node.next=currValue
            node.prev=leader
            currValue.prev=node
            self.length+=1
        self.printLinkedList()
            

    def reverse(self):
        
        first=self.head
        self.tail=self.head
        second=first.next
        while(second):
            temp=second.next
            second.next=first
            first.prev=second
            first=second
            second=temp
            
        self.head=first
        self.tail.next=None
        self.printLinkedList()
        
        
doublylinkedList= ReverseDoublyLL()
doublylinkedList.prepend(20)
doublylinkedList.prepend(40)
doublylinkedList.append(88)
doublylinkedList.prepend(120)
doublylinkedList.insert(5, 99)
doublylinkedList.insert(4,34)   
doublylinkedList.insert(2,909)  
doublylinkedList.reverse()
doublylinkedList.insert(3, 100)
doublylinkedList.reverse()
doublylinkedList.append(118)
doublylinkedList.prepend(85)
