# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if((head==None) or (head.next==None)):       
            return head
        
        first=head    
        second=first.next
        while(second):
            temp=second.next
            second.next=first
            first=second
            second=temp
        head.next=None
        head=first
        return head
        
