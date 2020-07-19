'''
Created on 19-Jul-2020

@author: dibyajyoti
'''

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

def InOrder(root,list1):

    if root.left:
        InOrder(root.left,list1)
    list1.append(root.data)
    if root.right:
        InOrder(root.right,list1)
    return list1

def PreOrder(root,list1):
    list1.append(root.data)
    if root.left:
        PreOrder(root.left,list1)
    if root.right:
        PreOrder(root.right,list1)
    return list1

def PostOrder(root,list1):
    if root.left:
        PostOrder(root.left,list1)
    if root.right:
        PostOrder(root.right,list1)
    list1.append(root.data)
    return list1
'''
         50
         /\
      30   70
      /\   /\
    20 40 60 80
                \
                100
'''
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
root = insert(root, 100)
print("\nInorder Traversal Method of a BST",InOrder(root,[]))
print("Pre-Order Traversal Method of a BST",PreOrder(root,[]))
print("Post-Order Traversal Method of a BST",PostOrder(root,[]))
