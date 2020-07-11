'''
Created on 11-Jul-2020

@author: dibyajyoti
'''


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val
        self.height = 1


class AVL_Tree:

    def insert(self, root, key):
        if root is None:
            return Node(key)

        elif (key < root.data):
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        ''' update height of tree'''
        root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))

        ''' get the balance factor'''
        balance = self.getbalance(root)

        ''' comparison for possible 4 cases'''

        if (balance > 1 and key < root.left.data):
            return self.rightrotate(root)

        if (balance > 1 and key > root.left.data):
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)

        if (balance < -1 and key > root.right.data):
            return self.leftrotate(root)

        if (balance < -1 and key < root.right.data):
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)
        return root

    def getheight(self, root):
        if root is None:
            return 0
        return root.height

    def getbalance(self, root):
        if root is None:
            return 0
        return self.getheight(root.left) - self.getheight(root.right)

    def leftrotate(self, root):
        y=root.right
        temp=y.left

        '''perform rotation'''
        y.left=root
        root.right=temp

        '''update height'''
        root.height=1+max(self.getheight(root.left),self.getheight(root.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))

        return y

    def rightrotate(self, root):
        y = root.left
        temp = y.right

        ''' perform rotation'''
        y.right = root
        root.left = temp

        ''' update height'''
        root.height = 1 + max(self.getheight(root.left), self.getbalance(root.right))
        y.height = 1 + max(self.getheight(y.left), self.getheight(y.right))

        return y

    def PreOrder(self,root):

        if root is not None:
            print("{0} ".format(root.data), end="")
            self.PreOrder(root.left)
            self.PreOrder(root.right)


"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""

mytree = AVL_Tree()
root = None
root = mytree.insert(root, 10)
root = mytree.insert(root, 20)
root = mytree.insert(root, 30)
root = mytree.insert(root, 40)
root = mytree.insert(root, 50)
root = mytree.insert(root, 25)
# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
mytree.PreOrder(root)

