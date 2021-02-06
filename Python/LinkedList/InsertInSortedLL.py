'''
Created on 06-Feb-2021

@author: dibyajyoti
'''
'''
Problem: Insert element in a sorted Linkedlist
We are allowing duplicate element in the linkedlIst.
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def prepend(self,value):
        node=Node(value)
        if(self.length==0):
            self.head=node
            self.tail=node
            self.length+=1
        else:
            if(value <= self.head.data):
                node.next=self.head
                self.head=node
                self.length+=1
                self.printLinkedList()
            else:
                print("Cannot prepend larger value in 0th position in sorted LL")
        
    def append(self,value):
        node=Node(value)
        if(self.length==0):
            self.head=node
            self.tail=node
            self.length+=1
        else:
            if(value >= self.tail.data):
                self.tail.next=node
                self.tail=node
                self.length+=1
                self.printLinkedList()
            else:
                print("Cannot append smaller value in end position in sorted LL")
        
    ''' Function to insert element at a particular position in sorted LL'''
    def insert_at_pos(self,pos,value):
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
            if(value >= leader.data and value <= follower.data):
                leader.next=node
                node.next=follower
                self.length+=1
                self.printLinkedList()
            else:
                print("Cannot insert smaller value between elements in sorted LL")
                
    ''' Function to insert an element in sorted LL'''    
    def insert_using_value(self,value):
        node=Node(value)
        currValue=self.head
        while(currValue):
            
            #Handling the append Case'''
            if(currValue.next==None):
                self.tail.next=node
                self.tail=node
                self.length+=1
                break
            #Handling the insert at any position in middle of LL#
            elif(value >= currValue.data and value <= currValue.next.data):
                follower=currValue.next
                currValue.next=node
                node.next=follower
                self.length+=1
                break
            #Handling the prepend case'''
            elif(value <= currValue.data):
                node.next=self.head
                self.head=node
                self.length+=1
                break
            else:
                currValue=currValue.next
        self.printLinkedList()
          
    def traverseToIndex(self,index):
        counter=0
        currValue=self.head
        while(counter!=index):
            currValue=currValue.next
            counter+=1
        return currValue    
            
        
    def printLinkedList(self):
        currValue=self.head
        list1=[]
        while(currValue):
            list1.append(currValue.data)
            currValue=currValue.next
        print(str(list1)+ " -> "+str(self.length))


ll=LinkedList()
ll.prepend(30)
ll.prepend(20)
ll.append(50)
ll.append(100)
ll.prepend(10)
ll.printLinkedList()
ll.insert_at_pos(0, 35)
ll.insert_at_pos(0, 5)
ll.insert_at_pos(3, 20)
ll.prepend(4)
ll.append(110)
ll.insert_using_value(5)
ll.insert_using_value(120)
ll.insert_at_pos(0, 4)
