'''Implementation of double ended queue using Array'''

class dequeueUsingArray:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.queue=[None]*self.maxsize
        self.front=-1
        self.rear=-1
        self.length=0

    def front_enqueue(self,ele):
        if self.isFull():
            print("Queue is full")
            return
        self.front+=1
        while(self.queue[self.front]!=None):
            self.front+=1
        self.queue[self.front]=ele
        self.length+=1
        self.printQueue()

    def rear_enqueue(self,ele):
        if self.isFull():
            print("Queue is full")
            return
        self.rear += 1
        while(self.queue[self.rear]!=None):
            self.rear += 1
        self.queue[self.rear] = ele
        self.length += 1
        self.printQueue()

    def front_dequeue(self):
        if self.isEmpty():
            print("queue is Empty")
            return

        ele=self.queue[self.front]
        self.queue[self.front]=None
        self.front-=1
        self.length-=1
        return "Element dequeued from front=>"+str(ele)

    def rear_dequeue(self):
        if self.isEmpty():
            print("queue is Empty")
            return
        ele=self.queue[self.rear]
        self.queue[self.rear]=None
        self.rear-=1
        self.length-=1
        return "Element dequeued from rear=>" + str(ele)

    def isEmpty(self):
        if self.rear == self.front or self.length <=0:
            self.front=-1
            self.rear=-1
            return True
        return False

    def isFull(self):
        if self.length ==self.maxsize:
            return True
        return False


    def printQueue(self):
        ind=0
        list1=[]
        while(ind!=self.length):
            list1.append(self.queue[ind])
            ind+=1
        print("Queue=>"+str(self.queue))

if __name__ == '__main__':
    q = dequeueUsingArray(5)
    q.front_enqueue(10)
    q.front_enqueue(20)
    q.rear_enqueue(30)
    q.rear_enqueue(40)
    q.rear_enqueue(50)
    q.rear_enqueue(60)
    print(q.front_dequeue())
    print(q.front_dequeue())
    print(q.printQueue())
    print(q.rear_dequeue())
    print(q.printQueue())
    print(q.rear_dequeue())
    print(q.printQueue())
    print(q.rear_dequeue())
    print(q.printQueue())
    print(q.rear_dequeue())
    print(q.rear_dequeue())
    print(q.front_dequeue())
    print(q.front_dequeue())
    print(q.printQueue())
    q.rear_enqueue(30)
    q.rear_enqueue(40)
    q.rear_enqueue(50)
    q.rear_enqueue(60)
    q.rear_enqueue(6000)
    q.rear_enqueue(6000)
    print(q.rear_dequeue())
    print(q.printQueue())
    q.front_enqueue(54)
    q.front_enqueue(542)
    print(q.rear_dequeue())
    print(q.rear_dequeue())
    print(q.rear_dequeue())
    print(q.rear_dequeue())
    print(q.rear_dequeue())
    print(q.rear_dequeue())
    print(q.printQueue())