# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#1->2->2->1  TRUE
#1->2->2 FALSE

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if((head==None) or (head.next==None)):       
            return True
    
        arr=[]
        first=head   
        arr.append(first.val)
        second=first.next
        while(second):
            arr.append(second.val)
            temp=second.next
            second.next=first
            first=second
            second=temp
        head.next=None
        head=first
        
        i=0
        currentValue=head
        while(head):
            if head.val == arr[i]:
                i+=1
                head=head.next
                continue
            else:
                return False
        return True

      
