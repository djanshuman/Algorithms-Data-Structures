'''
Created on 14-Mar-2026

@author: dibyajyoti
'''

class CircularQueue:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.queue = [None] * self.maxsize
        self.front = -1
        self.rear = -1

    def print_queue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        ll = []
        index = self.front
        while True:
            ll.append(self.queue[index])
            if index == self.rear:
                break
            index = (index + 1) % self.maxsize
        print(ll)

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.maxsize == self.front

    def enqueue(self,ele):
        if self.isFull():
            print("Queue is full")
            return
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.maxsize
        self.queue[self.rear] = ele

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        ele = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.maxsize
        return ele

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
        return (self.rear - self.front + self.maxsize) % self.maxsize + 1

if __name__ == "__main__":
    q = CircularQueue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.print_queue()
    print(q.peek_front())
    print(q.peek_rear())
    print(q.length_of_queue())

    print("\n--- dequeue two ---")
    print(q.dequeue())
    print(q.dequeue())
    q.print_queue()

    print("\n--- enqueue two more (wrap around) ---")
    q.enqueue(60)
    q.enqueue(70)
    q.print_queue()
    print(q.length_of_queue())
