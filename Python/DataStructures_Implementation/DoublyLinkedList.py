'''
Created on 06-Feb-2021

@author: dibyajyoti
'''

'''
1. Doubly Linked List Implementation
2. Reverse a Doubly linked List
3. Delete element based on given index
4. Delete element using a value
'''

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class DoubleLinkedListNew:
    
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
 
    ''' Prepend an element in DoublyLinkedList''' 
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
      
    ''' Append an element in DoublyLinkedList'''   
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
        
    ''' Insert an element in a given position''' 
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
            
    ''' Remove an element in a given index''' 
    def remove(self,index):
        if(index==0):
            newhead=self.head.next
            newhead.prev=None
            self.head=newhead
            self.length-=1
        elif(index==(self.length)-1):
            newtail=self.tail.prev
            newtail.next=None
            self.tail=newtail
            self.length-=1
        else:
            counter=0
            currValue=self.head
            while(counter!=index):
                currValue=currValue.next
                counter+=1
            currValue.prev.next=currValue.next
            currValue.next.prev=currValue.prev
            self.length-=1
        self.printLinkedList()
        
    ''' Remove element in DoublyLinkedList using Value'''
    def remove_by_value(self,value):
        currValue=self.head
        while(currValue):
            if(value==currValue.data):
                if(currValue==self.head):
                    self.head=currValue.next
                    self.head.prev=None
                    self.length-=1
                    break
                elif(currValue==self.tail):
                    self.tail=currValue.prev
                    self.tail.next=None
                    self.length-=1
                    break
                else:
                    currValue.prev.next=currValue.next
                    currValue.next.prev=currValue.prev
                    self.length-=1
                    break     
            currValue=currValue.next
        self.printLinkedList()
        
    ''' Fetch item based on index'''            
    def getItem(self,index):
        if(index >=0 and index < (self.length)):
            counter=0
            currValue=self.head
            while(counter!=index):
                currValue=currValue.next
                counter+=1
            return "index:"+str(index)+", data :"+str(currValue.data)
        else:
            return "Enter a valid index"
        
    ''' Print element in reverse way'''   
    def print_reverseLL(self):
        currValue=self.tail
        list1=[]
        while(currValue!=None):
            list1.append(currValue.data)
            currValue=currValue.prev
        return list1
   
    ''' Reverse a DoublyLinkedList'''
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
        
        
doublylinkedList= DoubleLinkedListNew()
doublylinkedList.prepend(20)
doublylinkedList.prepend(40)
doublylinkedList.prepend(50)
doublylinkedList.append(70)
doublylinkedList.append(88)
doublylinkedList.prepend(120)
doublylinkedList.insert(5, 99)
doublylinkedList.remove(3)   
print(doublylinkedList.getItem(4))
doublylinkedList.insert(4,34)   
doublylinkedList.insert(2,909)
doublylinkedList.remove(6)
doublylinkedList.remove(1)
doublylinkedList.remove(3)   
doublylinkedList.reverse()
doublylinkedList.insert(3, 100)
doublylinkedList.reverse()
doublylinkedList.append(118)
doublylinkedList.prepend(85)
print(doublylinkedList.print_reverseLL())
doublylinkedList.remove_by_value(40)
doublylinkedList.insert(5, 35)
doublylinkedList.insert(1,182)
doublylinkedList.prepend(107)
doublylinkedList.append(81)
doublylinkedList.reverse()
doublylinkedList.remove(3)
doublylinkedList.remove(9) 
doublylinkedList.insert(3,17)
doublylinkedList.remove_by_value(120)
doublylinkedList.remove_by_value(88)
doublylinkedList.remove_by_value(81)
doublylinkedList.remove_by_value(85)
