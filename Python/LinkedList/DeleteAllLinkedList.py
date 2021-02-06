'''
Created on 07-Feb-2021

@author: dibyajyoti
'''
'''
Delete All Elements in a linkedList and reduce the length of LL'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class DeleteAllLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def printLinkedList(self):
        currValue=self.head
        list1=[]
        while(currValue):
            list1.append(currValue.data)
            currValue=currValue.next
        print(str(list1)+ " -> "+str(self.length))
    
        
    def prepend(self,value):
        node=Node(value)
        if(self.length==0):
            self.head=node
            self.tail=node
            self.length+=1
        else:
            node.next=self.head
            self.head=node
            self.length+=1
        return self.printLinkedList()
        
    def append(self,value):
        node=Node(value)
        if(self.length==0):
            self.head=node
            self.tail=node
            self.length+=1
        else:
            self.tail.next=node
            self.tail=node
            self.length+=1
        return self.printLinkedList()
        
    def insert(self,pos,value):
        node=Node(value)
        if(pos < 0):
            print("Insert a valid position starting from 0 index")
            return
        
        if(pos==0):
            self.prepend(value)
        elif(pos >(self.length)-1):
            self.append(value)
        else:
            leader=self.traverseToIndex(pos-1)
            follower=leader.next
            leader.next=node
            node.next=follower
            self.length+=1
            return self.printLinkedList()
            
    def traverseToIndex(self,index):
        counter=0
        currValue=self.head
        while(counter!=index):
            currValue=currValue.next
            counter+=1
        return currValue    
    
    ''' Delete all element in LinkedList and reduce the length'''
    def remove_all(self):
        currValue=self.head
        while(currValue!=self.tail):
            currValue.data=None
            self.length-=1
            currValue=currValue.next
        self.head=self.tail=None
        self.length-=1
        return self.printLinkedList()          
    
ll=DeleteAllLinkedList()
ll.prepend(30)
ll.prepend(20)
ll.append(50)
ll.append(100)
ll.prepend(51)
ll.insert(2, 33)
ll.remove_all()
ll.insert(7, 35)
ll.insert(3, 100)
ll.remove_all()
