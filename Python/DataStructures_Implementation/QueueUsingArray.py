'''
Created on 14-Mar-2026

@author: dibyajyoti
'''


class QueueUsingArray:

    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.queue = [None] * self.maxsize
        self.front = -1
        self.rear = -1

    def enqueue(self,ele):
        if self.isFull():
            print ("Queue is full")
            return
        if self.isEmpty():
            self.front +=1
        self.rear +=1
        self.queue[self.rear] = ele

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        ele = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:  # last element
            self.front = -1
            self.rear = -1
        else:
            self.front +=1
        return ele

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.rear == self.maxsize -1

    def print_queue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print(self.queue[self.front : self.rear +1])

    def peek_front(self):
        if self.isEmpty():
            return "Queue is Empty"
        return "Front element is: " + str(self.queue[self.front])


    def peek_rear(self):
        if self.isEmpty():
            return "Queue is Empty"
        return "Rear element is: " + str(self.queue[self.rear])

    def length_of_queue(self):
        if self.isEmpty():
            return 0
        return self.rear - self.front + 1


if __name__ == "__main__":
    q = QueueUsingArray(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.print_queue()
    print(q.length_of_queue())
    print(q.peek_front())
    print(q.peek_rear())
