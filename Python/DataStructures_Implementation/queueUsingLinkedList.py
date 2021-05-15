
'''Queue Implementation using LinkedList'''

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class queueUsingLinkedList:

    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.front=None
        self.rear=None
        self.length=0


    def enqueue(self,ele):
        if self.isFull():
            print("Queue is full")
            return
        node=Node(ele)
        node.next=None

        if(self.front==None):
            self.front=node
            self.rear=node
            self.length+=1
        else:
            self.rear.next=node
            self.rear=node
            self.length+=1
        print(self.printQueue())

    def dequeue(self):

        if self.isEmpty():
            print("Queue is Empty")
            return
        else:
            temp=self.front.data
            self.front=self.front.next
            self.length-=1
            return "Element dequeued from Queue: "+str(temp)

    def isEmpty(self):
        if(self.front == None):
            return True
        return False

    def isFull(self):
        if self.length == self.maxsize:
            return True
        return False

    '''below operation will take O(n)'''
    def atPosition(self,pos):
        if pos<=0 or pos > self.maxsize:
            return "Enter a valid position between 1 to Maxsize"

        if pos <=self.length:
            curr=self.front
            ind=1
            while(ind!=pos):
                ind+=1
                curr=curr.next
            return "Element at pos "+str(pos)+"=>"+str(curr.data)
        else:
            return "There is no element for the given position => "+str(pos)

    def printQueue(self):
        curr=self.front
        list1=[]
        while(curr!=None):
            list1.append(curr.data)
            curr=curr.next
        return "Queue =>"+str(list1)

if __name__ == '__main__':
    q = queueUsingLinkedList(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q.dequeue())
    print(q.printQueue())
    q.enqueue(100)
    print(q.dequeue())
    print(q.dequeue())
    print(q.printQueue())
    print(q.dequeue())
    print(q.atPosition(4))
    print(q.dequeue())
    print(q.atPosition(1))
    print(q.dequeue())
    print(q.dequeue())
    print(q.printQueue())
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q.atPosition(3))