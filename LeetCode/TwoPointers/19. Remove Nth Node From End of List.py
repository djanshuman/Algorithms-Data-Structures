'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # check input for empty case
        if head is None or n < 1:
            return head
        
        # create dummy node before head.
        dummy = ListNode(0)
        dummy.next = head

        #traverse fast n steps and return head if n > length
        fast = dummy
        for _ in range(n):
            if fast.next is None:
                return head
            fast = fast.next
        
        #assign slow to dummy and move slow and fast till fast reaches end
        slow = dummy
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        # Now slow and fast difference of places is n steps and slow.next is position to be deleted, delete the position
        slow.next = slow.next.next

        # return the head
        return dummy.next

