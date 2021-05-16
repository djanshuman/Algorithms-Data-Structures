'''Implementation of Priority queue by defining separate priority for each element'''

'''In this version of priority queue we consider 1=High Priority and 2=Least priortity. 
Insertion to be done based on priority and deletion to be done only on mainQueue. 
If and only iff mainQueue is empty then only secondQueue element in dequeued as per FIFO'''

class PriorityQueue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.queue=dict()
        self.mainQueue=[None]*self.maxsize
        self.lengthMQ=0
        self.lengthSQ=0
        self.secondQueue=[None]*self.maxsize
        self.front=0
        self.rear=0
        self.front1 = 0
        self.rear1 = 0


    '''Main Enqueue Logic driver code'''
    def enqueueLogic(self,ele):

        for key in ele.keys():
            if ele[key]==1:
                self.enqueue_mainQ(key)
            elif ele[key]==2:
                self.enqueueSecondQ(key)
        self.printQ()
        return ("Enter a valid priority of 1 or 2")

    def enqueue_mainQ(self,ele):
        if self.isFull_mainQ():
            print("Main Queue is full")
            return None
        self.rear=(self.rear+1)%self.maxsize
        self.mainQueue[self.rear]=ele
        self.lengthMQ+=1

    def dequeue_mainQ(self):
        if(self.isEmpty_mainQ()):
            print("Main Queue is Empty")
            return None

        self.front = (self.front + 1) % self.maxsize
        ele=self.mainQueue[self.front]
        self.mainQueue[self.front]=None
        self.lengthMQ-=1
        return ele

    def enqueueSecondQ(self, ele):
        if self.isFullSecondQ():
            print("Second Queue is full")
            return None
        self.rear1=(self.rear1+1)%self.maxsize
        self.secondQueue[self.rear1]=ele
        self.lengthSQ+=1

    def dequeueSecondQ(self):
        if (self.isEmptySecondQ()):
            print("Second Queue is Empty")
            return None

        self.front1 = (self.front1 + 1) % self.maxsize
        ele = self.secondQueue[self.front1]
        self.secondQueue[self.front1] = None
        self.lengthSQ -= 1
        return ele

    def isEmpty_mainQ(self):
        if(self.front==self.rear):
            return True
        return False

    def isEmptySecondQ(self):
        if(self.front1==self.rear1):
            return True
        return False

    def isFull_mainQ(self):
        if(self.front==(self.rear+1)%self.maxsize):
            return True
        return False

    def isFullSecondQ(self):
        if(self.front1==(self.rear1+1)%self.maxsize):
            return True
        return False

    def printQ(self):
        print("Main Queue=>"+ str(self.mainQueue),"Second Queue =>"+ str(self.secondQueue))

    '''Priority wise Dequeue'''
    def priorityWiseDequeue(self):
        if(self.lengthMQ ==0):
            if(self.secondQueue ==0):
                print("Both Queues are Empty")
            else:
                ele=self.dequeueSecondQ()
                if ele !=None:
                    return "Dequeued Element from Second Queue =>" +str(ele)
        else:
            ele=self.dequeue_mainQ()
            if ele !=None:
                return "Dequeued Element from Main Queue =>" + str(ele)

if __name__ == '__main__':
    p = PriorityQueue(10)
    ele={'A': 1, 'B':1,'C':2,'D':2,'E':2,'F':1,'G':1,'H':2,'I':1,'J':1}
    p.enqueueLogic(ele)
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    ele1={'Z':1,'L':2,'M':1,'N':1}
    p.enqueueLogic(ele1)
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    ele2 = {'A': 1, 'D': 1, 'Q': 2, 'P': 2}
    p.enqueueLogic(ele2)
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    ele2 = {'A': 1, 'V': 1, 'T': 2, 'Z': 2}
    p.enqueueLogic(ele2)
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())
    print(p.priorityWiseDequeue())