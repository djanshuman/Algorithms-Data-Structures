''' The following code implements BreadFirstSearch in a Binary Tree in both Iterative and Recursive manner '''

class Node:

    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key

def insert(node,value):
    if node is None:
        return Node(value)

    if (value > node.data):
        node.right=insert(node.right,value)
    elif(value < node.data):
        node.left=insert(node.left,value)

    return node

def lookup(node,value):
    if node is None:
        return False

    if node.data == value:
        return True
    elif value > node.data:
        return lookup(node.right,value)
    elif value < node.data:
        return lookup(node.left,value)
    return False

def delete(node,value):
    if node is None:
        return False
    elif value > node.data:
        node.right=delete(node.right,value)
    elif(value < node.data):
        node.left=delete(node.left,value)
    else:
        if node.left is None:
            temp=node.right
            root=None
            return temp
        elif(node.right is None):
            temp=node.left
            root=None
            return temp
        temp=minvalue(node.right)
        node.data=temp.data
        node.right=delete(node.right,temp.data)

    return node

def minvalue(root):
    currvalue=root
    while(currvalue.left is not None):
        currvalue=currvalue.left
    return currvalue

def maxvalue(root):
    currvalue=root
    while(currvalue.right is not None):
        currvalue=currvalue.right
    return currvalue.data

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def BreadFirstSearch(root):
    if root is None:
        return
    currvalue=root
    visited=[]
    queue=[]
    visited.append(currvalue.data)
    queue.append(currvalue)

    while(len(queue) > 0):
        q=queue.pop(0)

        if(q.left is not None):
            visited.append(q.left.data)
            queue.append(q.left)
        if( q.right is not None):
            visited.append(q.right.data)
            queue.append(q.right)

    return visited

def BFS_recursive(queue,mylist):
    if len(queue) == 0:
        return mylist
    currnode=queue[0]
    mylist.append(currnode.data)
    s=queue.pop(0)
    if (s.left is not None):
        queue.append(s.left)
    if (s.right is not None):
        queue.append(s.right)

    return BFS_recursive(queue,mylist)


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
root = insert(root, 100)
print("\nInorder traversal of tree")
inorder(root)
print("\nDoing Look up on tree for value 70")
print(lookup(root, 70))
print("Deleting 70 node from the tree")
#delete(root,70)
inorder(root)
print("\nDeleting 50 node from the tree")
#delete(root,50)
inorder(root)
print("\nDeleting 30 node from the tree")
#delete(root,30)
inorder(root)
print("\nMax value of Tree:",maxvalue(root))
print("Comm'on Boy lets execute our BFS",BreadFirstSearch(root))
print("BFS Recursive Way",BFS_recursive([root],[]))
