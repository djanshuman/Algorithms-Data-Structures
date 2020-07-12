
'''
Created on 13-Jul-2020

@author: dibyajyoti

'''
import sys

class MinHeap:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.size=0
        self.heap=[0]*(self.maxsize+1)
        self.heap[0]= -1*sys.maxsize
        self.FRONT=1

    def insert(self,element):
        if self.size >= self.maxsize:
            return "Heap is full"
        self.size+=1
        self.heap[self.size]=element
        current=self.size

        while(self.heap[current] < self.heap[self.parent(current)]):
            self.swap(current,self.parent(current))
            current=self.parent(current)

    def parent(self,pos):
        return pos//2

    def swap(self,curr_pos,parent_pos):
        self.heap[curr_pos],self.heap[parent_pos]=self.heap[parent_pos],self.heap[curr_pos]

    def leftchild(self,pos):
        return 2*pos

    def rightchild(self,pos):
        return (2*pos)+1


    def print(self):
        for i in range(1,(self.size//2)+1):
            print("PARENT : " + str(self.heap[i])+ " LEFT CHILD : " +
                  str(self.heap[2*i])+ " RIGHT CHILD : " + str(self.heap[2*i+1]))

    def minheap(self):
        for pos in range(self.size//2, 0 -1):
            self.minheapify(pos)

    def isleaf(self,pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return  False

    ''' function to heapify the nodes'''
    def minheapify(self,pos):

        #if the function is a non-leaf node and greater then any of its child'''
        if not self.isleaf(pos):
            if(self.heap[pos] > self.heap[self.leftchild(pos)] or
            self.heap[pos] > self.heap[self.rightchild(pos)]):

                #Swap with left child and heapify the left child'''

                if(self.heap[self.leftchild(pos)] < self.heap[self.rightchild(pos)]):
                    self.swap(pos,self.leftchild(pos))
                    self.minheapify(self.leftchild(pos))
                #'''Swap with right child and heapify the right child'''
                else:
                    self.swap(pos,self.heap[self.rightchild(pos)])
                    self.minheapify(self.rightchild(pos))

    ''' function to fetch min value in heap'''
    def extractmin(self):
        popped=self.heap[self.FRONT]
        self.heap[self.FRONT]=self.heap[self.size]
        self.heap[self.size]=0
        self.size-=1
        self.minheapify(self.FRONT)
        return popped

minHeap=MinHeap(15)
minHeap.insert(5)
minHeap.insert(3)
minHeap.insert(17)
minHeap.insert(10)
minHeap.insert(84)
minHeap.insert(19)
minHeap.insert(6)
minHeap.insert(22)
minHeap.insert(9)
minHeap.minheap()
minHeap.print()
print("The Min val is " + str(minHeap.extractmin()))
minHeap.print()
