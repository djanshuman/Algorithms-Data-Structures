"""
Date : Feb 17, 2026
"""


class UnionFind:
    def __init__(self,element):
        self.parent= dict()
        self.rank = dict()

        # if input can be list of element or just an integer
        if isinstance(element,int):
            for i in range(element):
                self.parent[i]= i
                self.rank[i] = 0
        else: #{0: 0, 1: 1, 2: 2, 3: 3, 4: 4} {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
            for ele in element:
                self.parent[ele] = ele
                self.rank[ele] = 0

    def find(self,i):

        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # 0,1
    def union(self,i,j):

        #find representative
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            #check which rank is smaller to make it child of other root.
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
                self.rank[root_j] +=1

            elif self.rank[root_j] < self.rank[root_i]:
                self.parent[root_j] = root_i
                self.rank[root_i] +=1
            # if both ranks are same:
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

    def connected(self,i,j):

        if self.find(i) == self.find(j):
            return True
        else:
            return False

    def get_sets(self):
        sets = {}
        for parent in self.parent:
            root = self.find(parent)
            if root not in sets:
                sets[root] =[]
            sets[root].append(parent)
        return sets

# kruskal algorithm logic
def kruskal_mst(edges,vertex):
    # sort with minimum weight edge
    edges.sort(key = lambda x : x[2],reverse = False)

    # traverse edges in sorted order
    ds = UnionFind(vertex)
    cost = 0
    count = 0
    for x,y,w in edges:
        #check if there is a no cycle formed, form the union and keep track of cost and edge count
        if ds.find(x) != ds.find(y):
            ds.union(x,y)
            cost += w
            count += 1
            print(f"Edges and Cost included are",str(x) + "---" + str(y) + " = "+ str(w))
            if count == vertex -1:
                break
    print("Total cost of Spanning true")
    return cost
if __name__ == "__main__":
    # Initialize DSU with elements 0 to 4
    '''
    ds = UnionFind(5)
    
    #print(ds.parent,ds.rank)
    # Perform union operations
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)
    #print(ds.parent,ds.rank)
    print("Is connected 2 & 0:",ds.connected(2,0))
    print("Is connected 2 & 3:",ds.connected(2,3))
    print("Representative of 2 is",ds.find(2))
    print("\n")
    print("Representative of 2 is ",ds.get_sets())'''
    edges = [[0, 1, 10], [1, 3, 15], [2, 3, 4], [2, 0, 6], [0, 3, 5]]
    print(kruskal_mst(edges,4))

