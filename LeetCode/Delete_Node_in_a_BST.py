# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        if(key > root.val):
            root.right=self.deleteNode(root.right,key)
        elif(key < root.val):
            root.left=self.deleteNode(root.left,key)
        elif(key == root.val):
            if root.right is None:
                temp=root.left
                root=None
                return temp
            elif(root.left is None):
                temp=root.right
                root=None
                return temp
            else:
                temp=self.minValue(root.right)
                root.val=temp.val
                root.right=self.deleteNode(root.right,temp.val)
            return root
        return root
            
    def minValue(self,root):
        currvalue=root
        while(currvalue.left is not None):
            currvalue=currvalue.left
        return currvalue
