''' Queue Implementation using Array and two pointers'''


class queueUsingArray:

    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.queue=[None]*self.maxsize
        self.front=-1
        self.rear=-1
        self.length=0

    def enqueue(self,ele):
        '''below condition is checked to reset pointers only when queue is empty post dequeueing and we want to enqueue a new element'''
        if(self.length ==0):
            self.front=-1
            self.rear=-1

        if self.isFull():
            print("Queue is full")
            return
        self.rear+=1
        self.queue[self.rear]=ele
        self.length+=1
        print(self.printQueue())

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            '''pointers are reset to ensure enqueue happens again on an empty queue'''
            self.front=-1
            self.rear=-1
            return
        ele=self.queue[self.front+1]
        self.queue[self.front+1]=None
        self.front+=1
        self.length-=1
        return "Element dequeued for Queue:" +str(ele)

    def isEmpty(self):
        if(self.front == self.rear):
            return True
        return False

    def isFull(self):
        if(self.length == self.maxsize):
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
    q = queueUsingArray(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(320)
    print(q.dequeue())
    print(q.printQueue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.printQueue())
    q.enqueue(100)
    print(q.findElement(1))
    q.enqueue(900)
    q.enqueue(30)
    q.enqueue(40)
    print(q.findElement(4))
    q.enqueue(50)
    print(q.printQueue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(10000)
    q.enqueue(100)
    q.enqueue(900)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q.findElement(0))
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.printQueue())