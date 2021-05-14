''' Circular Queue Implementation using Array'''
'''front= (front+1) %size
   rear=(rear+1)%size'''


class circularQueue:

    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.queue=[None]*self.maxsize
        self.front=0
        self.rear=0
        self.length=0

    def enqueue(self,ele):

        if self.isFull():
            print("Queue is full")
            return
        self.rear=(self.rear+1)%self.maxsize
        self.queue[self.rear]=ele
        self.length+=1
        print(self.printQueue())

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        self.front=(self.front+1)%self.maxsize
        ele=self.queue[self.front]
        self.queue[self.front]=None
        self.length-=1
        return "Element dequeued for Queue:" +str(ele)

    def isEmpty(self):
        if(self.front == self.rear):
            return True
        return False

    def isFull(self):
        if(self.front == (self.rear+1)%self.maxsize):
            return True
        return False

    def findElement(self,pos):
        if(pos <= 0 or pos >= self.maxsize):
            return "enter valid pos between 1 and maxsize"
        return "Element at "+str(pos)+" pos is " +str(self.queue[self.front+pos])

    def printQueue(self):
        ind=0
        list1=[]
        while(ind!=self.maxsize):
            list1.append(self.queue[ind])
            ind+=1
        return "Queue => "+str(list1)

if __name__ == '__main__':
    q = circularQueue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print(q.findElement(4))
    print(q.findElement(1))
    print(q.findElement(3))
    print(q.dequeue())
    print(q.printQueue())
    q.enqueue(190)
    print(q.dequeue())
    q.enqueue(200)
    print(q.findElement(1))
    print(q.dequeue())
    print(q.dequeue())
    print(q.printQueue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(500)
    print(q.findElement(1))
    q.enqueue(600)
    print(q.findElement(2))
    q.enqueue(20)
    q.enqueue(30)
    print(q.dequeue())
    q.enqueue(40)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.printQueue())
    q.enqueue(55)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(88)