
'''
Created on 13-Jul-2020

@author: dibyajyoti

'''

import sys

class MaxHeap:

    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.size = 0
        self.heap=[0]*(self.maxsize+1)
        self.heap[0]=sys.maxsize
        self.front=1

    def insert(self,element):
        if(self.size >= self.maxsize):
            return "Heap is full"
        self.size+=1
        self.heap[self.size]=element
        current=self.size

        while(self.heap[current] > self.heap[self.parent(current)]):
            self.swap(current,self.parent(current))
            current=self.parent(current)

    def parent(self,pos):
        return pos//2

    def leftchild(self,pos):
        return pos*2

    def rightchild(self,pos):
        return (2*pos)+1

    def leafnode(self,pos):
        if pos >= (self.size//2) and pos <=self.size:
            return True
        return False

    def swap(self,current,parent):
        self.heap[current],self.heap[parent]= self.heap[parent],self.heap[current]

    def print(self):
        for i in range(1,(self.size//2)+1):
            print("PARENT : " + str(self.heap[i]) + " LEFT CHILD : " + str(self.heap[2*i])
                  + " RIGHT CHILD : " + str(self.heap[(2*i)+1]))

    ''' function to heapify the nodes'''
    def maxheapify(self,pos):
        if not self.leafnode(pos):
            if(self.heap[pos] < self.heap[self.leftchild(pos)] or
                    self.heap[pos] < self.heap[self.rightchild(pos)]):

                #heapify the left child and swap the max value with left

                if(self.heap[self.leftchild(pos)] > self.heap[self.rightchild(pos)]):
                    self.swap(pos,self.leftchild(pos))
                    self.maxheapify(self.leftchild(pos))
                #heapify the right child and swap the max value with right
                else:
                    self.swap(pos,self.heap[self.rightchild(pos)])
                    self.maxheapify(self.rightchild(pos))

    ''' function to fetch max value in heap'''
    def extractmax(self):
        popped=self.heap[self.front]
        self.heap[self.front]=self.heap[self.size]
        self.size-=1
        self.maxheapify(self.front)
        return popped

maxheap=MaxHeap(15)
maxheap.insert(5)
maxheap.insert(3)
maxheap.insert(17)
maxheap.insert(10)
maxheap.insert(84)
maxheap.insert(19)
maxheap.insert(6)
maxheap.insert(22)
maxheap.insert(9)
maxheap.print()
print("The max value is : " + str(maxheap.extractmax()))
maxheap.print()
