'''
Created on 19-Jul-2020

@author: dibyajyoti

The Breadh First Search Implementation along with Shortest Path and Parent checks done using dictionary
self.level=dict() -> Stores the distance from the searched vertex to rest all vertex.
self.parent=dict() -> Stores the parent of each vertex that can be traced and Shows the BFS traversal
order.
'''
from collections import defaultdict
class Breadthfirstsearch:

    def __init__(self):
        self.graph=defaultdict(list)
        self.level=dict()
        self.parent=dict()
        self.queue=[]

    def addedge(self,v,e):
        self.graph[v].append(e)

    def printGraph(self):
        for key in self.graph.keys():
            print(key,':',self.graph[key])

    def search(self,vertex):
        self.level={vertex:0}
        self.parent={vertex:None}
        self.queue.append(vertex)

        while(self.queue):
            v=self.queue.pop(0)
            for e in self.graph[v]:
                if e not in self.level and e!=None:
                    self.queue.append(e)
                    self.level[e]=self.level[v]+1
                    self.parent[e]=v
        return self.level,self.parent  # if interested to see only traversal order self.parent.keys()

'''
1. First Pattern
       0
    /  |  \ 
    1  2  3
    /\ |  |
   4 5 6  7 
   
2. Second Pattern
 
A : ['B', 'C']
B : ['A', 'D', 'E']
C : ['A', 'D']
D : ['B', 'C', 'E']
E : ['B', 'D']  

3. Third Pattern
   0 - 1 -7
 / |    /
8  3 - 2    6
 \ |    \  /
   4     5       
   
4. Fourth Pattern
          50
          /\
       30   70
       /\   /\
     20 40 60 80
                 \
                 100     
'''

bst=Breadthfirstsearch()
bst.addedge('A','B')
bst.addedge('A','C')
bst.addedge('B','A')
bst.addedge('B','D')
bst.addedge('B','E')
bst.addedge('C','A')
bst.addedge('C','D')
bst.addedge('D','B')
bst.addedge('D','C')
bst.addedge('D','E')
bst.addedge('E','B')
bst.addedge('E','D')
print("\n1.Printing Graphs Vertex and Edges:")
bst.printGraph()
print("\n1.Printing Graphs in BreadFirstSearch order :")
print(bst.search('A'))
print("\n")

bst=Breadthfirstsearch()
bst.addedge(0,1)
bst.addedge(0,2)
bst.addedge(0,3)
bst.addedge(1,4)
bst.addedge(1,5)
bst.addedge(2,6)
bst.addedge(2,7)
bst.addedge(3,7)
bst.addedge(4,None)
bst.addedge(5,None)
bst.addedge(6,None)
bst.addedge(7,None)
print("\n2.Printing Graphs Vertex and Edges:")
bst.printGraph()
print("\n2.Printing Graphs in BreadFirstSearch order :")
print(bst.search(0))
print("\n")

bst=Breadthfirstsearch()
bst.addedge(0,1)
bst.addedge(0,3)
bst.addedge(0,8)
bst.addedge(1,0)
bst.addedge(1,7)
bst.addedge(7,1)
bst.addedge(7,2)
bst.addedge(2,3)
bst.addedge(2,5)
bst.addedge(2,7)
bst.addedge(3,0)
bst.addedge(3,2)
bst.addedge(3,4)
bst.addedge(4,3)
bst.addedge(4,8)
bst.addedge(5,2)
bst.addedge(5,6)
bst.addedge(8,0)
bst.addedge(8,4)
bst.addedge(6,5)
print("\n3.Printing Graphs Vertex and Edges:")
bst.printGraph()
print("\n3.Printing Graphs in BreadFirstSearch order :")
print(bst.search(0))
print("\n")


bst=Breadthfirstsearch()
bst.addedge(50,30)
bst.addedge(50,70)
bst.addedge(30,20)
bst.addedge(30,40)
bst.addedge(70,60)
bst.addedge(70,80)
bst.addedge(80,100)
print("\n4.Printing Graphs Vertex and Edges:")
bst.printGraph()
print("\n4.Printing Graphs in BreadFirstSearch order :")
print(bst.search(50))
