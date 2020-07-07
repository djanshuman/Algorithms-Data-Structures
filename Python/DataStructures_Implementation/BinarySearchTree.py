'''
Created on 05-Jul-2020

@author: dibyajyoti
'''
''' Functionalities : Insert, Delete, Lookup, Maxvalue, minValue'''


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinarySearchTree:
    
    def __init__(self):
        self.root=None
        
        
    def insert(self,value):
        node=Node(value)
        
        if(self.root==None):
            self.root=node
             
        else:
            currValue=self.root
            while(True):
                if(value < currValue.data):
                    #left
                    if(currValue.left==None):
                        currValue.left=node
                        return
                    else:
                        currValue=currValue.left
                
                else:
                    #right
                    if(currValue.right==None):
                        currValue.right=node
                        return
                    else:
                        currValue=currValue.right
                        
    def lookup(self,value):

        if(self.root==None):
            return False
        else:
            currvalue=self.root
            while(currvalue):
                if(value < currvalue.data):
                    currvalue=currvalue.left    
                    
                elif(value > currvalue.data):
                    currvalue=currvalue.right
                    
                elif(currvalue.data==value):
                    return True           
            return False
           
    ''' In-Order traversal with a helper method''' 
                 
    def print_tree(self):
        if(self.root!=None):
            self.print_logic(self.root)
            
    def print_logic(self,curr_node):
        if(curr_node!=None):
            self.print_logic(curr_node.left)
            print(str(curr_node.data))
            self.print_logic(curr_node.right)
            
    ''' Find max and min value of BST'''
            
    def minValue(self,node):
        currValue=node
        while(currValue.left!=None):
            currValue=currValue.left
        return  currValue
    
    def maxValue(self,root):
        node=root
        while(node.right!=None):
            node=node.right
        return node
    
    def find_max_min_Value(self):
        
        if(self.root==None):
            return False
        else:
            max_val=self.maxValue(self.root)
            min_val=self.minValue(self.root)
            
        print(max_val,min_val)
        
    def delete(self,root,key):
        if(root==None):
            return False
        
        if(key > root.data):
            root.right=self.delete(root.right, key)
        elif(key < root.data):
            root.left=self.delete(root.left, key)
        else:
            
            if(root.left is None):
                temp=root.right
                root=None
                return temp
            elif(root.right is None):
                temp=root.left
                root=None
                return temp
            temp=self.minValue(root.right)
            root.data=temp.data
            root.right=self.delete(root.right, key)
        return root
        
mybst=BinarySearchTree()
mybst.insert(9)
mybst.insert(4)
mybst.insert(20)
mybst.insert(3)
mybst.insert(6)
mybst.insert(15)
mybst.insert(30)
print(mybst.lookup(3))
mybst.print_tree()
#mybst.find_max_min_Value()
