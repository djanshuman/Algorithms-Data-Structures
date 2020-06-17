'''
Created on 18-Jun-2020

@author: dibyajyoti
'''

'''
1. Python SingleLinkedList Implementation
2. Reverse a LinkedList

1->10->99->100
Reverse : 100->99->10->1 '''

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def printList(self):
        list1=[]
        currentValue=self.head
        while(currentValue!=None):
            list1.append(currentValue.data)
            currentValue=currentValue.next
        return list1,'Length = ' + str(self.length)
        
    def prepend(self,data):
        node= Node(data)
        if(self.head == None):
            self.head=node
            self.tail=self.head
            self.length+=1
        else:
            node.next=self.head
            self.head=node
            self.length+=1
        return self.printList()
    
    def append(self,data):
        node= Node(data)
        if(self.head == None):
            self.head=node
            self.tail=self.head
            self.length+=1
        else:
            self.tail.next=node
            self.tail=node
            self.length+=1
        return self.printList()
    
    def remove(self,index):
        if(self.length ==0):
            return "Empty LinkedList"
        else:
            if(index == 0):
                temp=self.head.next
                self.head=temp
            
            elif(index == (self.length)):
                leader=self.traverseToIndex(index-1)
                leader.next=None
        
            else:
                leader=self.traverseToIndex(index-1)
                temp=leader.next.next
                leader.next=temp
                
        self.length-=1
        return self.printList()
    
    def insert(self,index,data):
        node=Node(data)
        if(index==0):
            return self.prepend(data)
        if(index>=self.length):
            return self.append(data)
        
        leader=self.traverseToIndex(index-1)
        temp=leader.next
        leader.next=node
        node.next=temp
        self.length+=1
        return self.printList()
    
    def traverseToIndex(self,index):
        i=0
        currentValue=self.head
        while(i!=index):
            currentValue=currentValue.next
            i+=1
        return currentValue
    
    def reverse(self):
        first=self.head
        self.tail=self.head
        second=first.next
        while(second):
            temp=second.next
            second.next=first
            first=second
            second=temp
        self.head.next=None
        self.head=first
        return self.printList()
    
myLinkedList=LinkedList()
print(myLinkedList.prepend(99))
print(myLinkedList.append(10))
print(myLinkedList.append(89))
print(myLinkedList.prepend(8989))
print(myLinkedList.remove(2))
print(myLinkedList.insert(3, 4))
print(myLinkedList.insert(1, 55))
print(myLinkedList.reverse())
