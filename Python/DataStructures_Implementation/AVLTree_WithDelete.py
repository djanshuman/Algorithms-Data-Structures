'''
Created on 11-Feb-2021

@author: dibyajyoti
'''

''' AVL Height balance tree Implementation 
    1. Insert and Delete operation'''


class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTreeNew:

    def insert(self, root, value):

        '''Step: 1 -> Insert data to node'''
        if root is None:
            return Node(value)
        if (value > root.data):
            root.right = self.insert(root.right, value)
        elif (value < root.data):
            root.left = self.insert(root.left, value)

        '''Step: 2 -> Update height of node'''
        root.height = 1 + max(self.getheight(root.right), self.getheight(root.left))

        '''Step: 3 -> Check balance factor of the node'''
        balance = self.getbalance(root)

        '''Step:4 -> Check 4 condition for violation LL,RR,LR,RL'''

        if balance > 1 and value < root.left.data:
            return self.rightrotate(root)

        if balance < -1 and value > root.right.data:
            return self.leftrotate(root)

        if balance > 1 and value > root.left.data:
            root.left=self.leftrotate(root.left)
            return self.rightrotate(root)
        if balance < -1 and value < root.right.data:
            root.right=self.rightrotate(root.right)
            return self.leftrotate(root)

        return root

    def delete(self,root,value):

        if root is None:
            return root

        if(value > root.data):
            root.right=self.delete(root.right,value)
        elif(value < root.data):
            root.left=self.delete(root.left,value)

        else:

            '''check for single child or no child'''
            if(root.left is None):
                temp=root.right
                root=None
                return temp
            elif(root.right is None):
                temp=root.left
                root=None
                return temp

            '''in case of both child nodes'''
            temp=self.minvalue(root.right)
            root.data=temp.data
            root.right=self.delete(root.right,temp.data)

        if root is None:
            return root

        root.height=1+max(self.getheight(root.right),self.getheight(root.left))
        balance=self.getbalance(root)


        #LL
        if balance > 1 and self.getbalance(root.left) >= 0:
            return self.rightrotate(root)
        #RR
        if balance < -1 and  self.getbalance(root.right) <=0:
            return self.leftrotate(root)

        # RL
        if balance < -1 and self.getbalance(root.right) > 0:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)
        #LR
        if balance > 1 and self.getbalance(root.left) < 0:
            root.left=self.leftrotate(root.left)
            return self.rightrotate(root)

        return root

    def minvalue(self,root):
        currValue=root
        while(currValue.left is not None):
            currValue=currValue.left
        return currValue

    def getheight(self, root):
        if root is None:
            return 0
        return root.height

    def getbalance(self, root):
        if root is None:
            return 0
        return self.getheight(root.left) - self.getheight(root.right)

    def leftrotate(self, root):
        temp = root.right
        temp_lchild = temp.left

        '''perform left rotation'''
        temp.left = root
        root.right = temp_lchild

        root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))
        temp.height = 1 + max(self.getheight(temp.left), self.getheight(temp.right))

        return temp

    def rightrotate(self, root):
        temp = root.left
        temp_rchild = temp.right

        '''perform right rotation'''
        temp.right = root
        root.left = temp_rchild

        root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))
        temp.height = 1 + max(self.getheight(temp.left), self.getheight(temp.right))

        return temp

    def preOrder(self, root):
        if root is not None:
            print(root.data),
            self.preOrder(root.left)
            self.preOrder(root.right)


avltree = AVLTreeNew()
root = None
'''
root = avltree.insert(root, 10)
root = avltree.insert(root, 20)
root = avltree.insert(root, 30)
root = avltree.insert(root, 40)
root = avltree.insert(root, 50)
root = avltree.insert(root, 25)
'''
root = avltree.insert(root, 9)
root = avltree.insert(root, 5)
root = avltree.insert(root, 10)
root = avltree.insert(root, 0)
root = avltree.insert(root, 6)
root = avltree.insert(root, 11)
root = avltree.insert(root, -1)
root = avltree.insert(root, 1)
root = avltree.insert(root, 2)
avltree.preOrder(root)
print("\n")
root=avltree.delete(root,10)
avltree.preOrder(root)
