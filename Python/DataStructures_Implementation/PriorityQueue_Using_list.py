'''
Created on 11-Jul-2020

@author: dibyajyoti

PriorityQueue using List
'''
class PriorityQueue(object):
    def __init__(self):
        self.queue=[]

    def empty(self):
        if len(self.queue) ==0:
            return True

    def enqueue(self,element):
        self.queue.append(element)

    def printQueue(self):
        print(self.queue)

    def dequeue(self):
        max=0
        for i in range(len(self.queue)):
            if(self.queue[i] > self.queue[max]):
                max=i
        value=self.queue[max]
        del[self.queue[max]]
        return value

if __name__ == "__main__":
    pq=PriorityQueue()
    pq.enqueue(12)
    pq.enqueue(1)
    pq.enqueue(14)
    pq.enqueue(7)
    #pq.printQueue()
    while(pq.empty()!=True):
        print(pq.dequeue())
