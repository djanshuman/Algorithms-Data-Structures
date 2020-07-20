'''
Created on 21-Jul-2020

@author: dibyajyoti

The Depth First Search Implementation of a Graph traversal.
'''
from collections import defaultdict


class Depthfirstsearch:

    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self, v, e):
        self.graph[v].append(e)

    def printGraph(self):
        for key in self.graph.keys():
            print(key, ':', self.graph[key])

    def dfs_util(self,vertex,visited):
        visited[vertex]=True
        print(vertex,end=" ")

        for i in self.graph[vertex]:
            if visited[i]==False:
                self.dfs_util(i,visited)

    def dfs(self,vertex):
        visited=[False]*(max(self.graph)+30)
        self.dfs_util(vertex,visited)

'''In above code usually it is passed as (max(self.graph)+1) but as we are passing multiple pattern so +30 is done to 
prevent index out of range issue.Choose any number as per your input size.

1. First Pattern

   0 - 1 -7
 / |    /
8  3 - 2    6
 \ |    \  /
   4     5       

2. Second Pattern
          50
          /\
       30   70
       /\   /\
     20 40 60 80
                 \
                 100   
3. Third Pattern

    0---->1---
    ^        |
    \\   /   |
     \\
      2      3--  
            ^  |
            |__| 
       
'''


bst = Depthfirstsearch()
bst.addedge(0, 1)
bst.addedge(0, 3)
bst.addedge(0, 8)
bst.addedge(1, 0)
bst.addedge(1, 7)
bst.addedge(7, 1)
bst.addedge(7, 2)
bst.addedge(2, 3)
bst.addedge(2, 5)
bst.addedge(2, 7)
bst.addedge(3, 0)
bst.addedge(3, 2)
bst.addedge(3, 4)
bst.addedge(4, 3)
bst.addedge(4, 8)
bst.addedge(5, 2)
bst.addedge(5, 6)
bst.addedge(8, 0)
bst.addedge(8, 4)
bst.addedge(6, 5)
print("\n1.Printing Graphs Vertex and Edges:")
bst.printGraph()
print("\n1.Printing Graphs in DepthFirstSearch order :")
bst.dfs(0)
print("\n")

bst = Depthfirstsearch()
bst.addedge(50, 30)
bst.addedge(50, 70)
bst.addedge(30, 20)
bst.addedge(30, 40)
bst.addedge(70, 60)
bst.addedge(70, 80)
bst.addedge(80, 100)
print("\n2.Printing Graphs Vertex and Edges:")
bst.printGraph()
print("\n2.Printing Graphs in DepthFirstSearch order :")
bst.dfs(50)
print("\n")

bst = Depthfirstsearch()
bst.addedge(0, 1)
bst.addedge(0, 2)
bst.addedge(1, 2)
bst.addedge(2, 0)
bst.addedge(2, 3)
bst.addedge(3, 3)
print("\n3.Printing Graphs Vertex and Edges:")
bst.printGraph()
print("\n3.Printing Graphs in DepthFirstSearch order :")
bst.dfs(2)
