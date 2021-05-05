class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value


def insert(root,val):
    if root is None:
        return Node(val)

    if(val > root.data):
        root.right=insert(root.right,val)

    elif(val < root.data):
        root.left=insert(root.left,val)

    return root

def lookup(root,val):
    if root is None:
        return False

    if (val == root.data):
        return "element found"
    elif(val > root.data):
        return lookup(root.right,val)
    elif(val < root.data):
        return lookup(root.left,val)
    return False

def inorder(root):
    if root is None:
        return False
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def preOrder(root):
    if root is None:
        return False
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return False
    preOrder(root.left)
    print(root.right,end=" ")
    preOrder(root.data)

def delete(root,val):
    if root is None:
        return False
    if(val > root.data):
        root.right=delete(root.right,val)
    elif(val < root.data):
        root.left=delete(root.left,val)

    else:
        #only one child case
        if(root.left is None):
            temp=root.right
            root=None
            return temp
        elif(root.right is None):
            temp=root.left
            root=None
            return temp

        temp=minValue(root.right)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
    return root


def minValue(root):
    if root is None:
        return False

    while(root.left is not None):
        root=root.left
    return root

def maxValue(root):
    if root is None:
        return False

    while (root.right is not None):
        root = root.right
    return root

root=None
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
print("\nPreOrder traversal of tree")
preOrder(root)
print("\n")
print(lookup(root,130))
delete(root,50)
preOrder(root)
