'''
Created on 07-Jul-2020

@author: dibyajyoti.nayak
'''
''' Functionalities : Insert, Delete, Lookup, Maxvalue, minValue'''

class Node:
    
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
        
def minvalue(node):
    currvalue=node
    while(currvalue.left is not None):
        currvalue=currvalue.left
    return currvalue

''' To Call maxvalue function independently , just change the lines: while(currvalue is not None) -> while(currvalue.right is not None):
return currvalue -> return currvalue.data
Same changes applicable for minvalue with left node. But delete function has to be changed accordingly.
'''

def maxvalue(node):
    currvalue=node
    while(currvalue is not None):
        currvalue=currvalue.right
    return currvalue
      
def insert(node,value):
    
    if node is None:
        return Node(value)
    
    if(value > node.data):
        node.right=insert(node.right,value)
    elif(value < node.data):
        node.left=insert(node.left,value)
        
    return node
    
def delete(node,value):
    
    if(node is None):
        return False
    
    elif(value > node.data):
        node.right=delete(node.right,value)
    elif(value < node.data):
        node.left=delete(node.left,value)
    else:
        ''' In case of Node with single child or no child'''
        if(node.left is None):
            temp=node.right
            node=None
            return temp
        elif(node.right is None):
            temp=node.left
            node=None
            return temp
        else:
            ''' In case of node with two child'''
            temp=minvalue(node.right)
            node.data=temp.data
            node.right=delete(node.right,temp.data)
    return node

def inorder(node):
    if(node is not None):
        inorder(node.left)
        print(node.data),
        inorder(node.right)
        
def lookup(node,value):
    if node is None:
        return False
    currvalue=node
    while(currvalue):
        if(value > currvalue.data):
            currvalue=currvalue.right
        elif(value < currvalue.data):
            currvalue=currvalue.left
        elif(currvalue.data == value):
            return True
    return False


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
print("\nDoing Look up on tree")
print(lookup(root, 70))
print("Deleting 70 node from the tree")
delete(root,70)
inorder(root)
print("\nDeleting 50 node from the tree")
delete(root,50)
inorder(root)
print("\nDeleting 30 node from the tree")
delete(root,30)
inorder(root)

