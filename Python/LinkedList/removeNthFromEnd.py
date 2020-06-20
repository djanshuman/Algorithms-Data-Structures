# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if(head is None):
            return False
        
        first=head  
        tail=head.next
        len_of_list=1
        pos=0
        temp=None
      
        if(tail is None):
            first=None
            head=first
            return head
          
        while(tail.next != None): 
            tail=tail.next
            len_of_list+=1
   
        first_to_traverse=(len_of_list-n)
    
        if(first_to_traverse < 0):
            temp=first.next
            first=temp
            head=first
     
        while(pos <first_to_traverse):
            first=first.next
            pos+=1
            
        if(pos==first_to_traverse):
            temp=first.next.next
            first.next=temp
           
        return head   
                
