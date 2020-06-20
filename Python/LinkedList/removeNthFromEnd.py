'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
'''

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
        '''To check Empty node'''
        if(head is None):
            return False
        
        '''We are mainting two pointers first and tail. We will fix the first pointer and traverse tail till last'''
        first=head  
        tail=head.next
        len_of_list=1
        pos=0
        temp=None
        
        '''To check if Input is single element'''
        if(tail is None):
            first=None
            head=first
            return head
          
        '''To calculate the length of LL and store in len_of_list variable. Here we reach the tail node'''
        while(tail.next != None): 
            print(1)
            tail=tail.next
            len_of_list+=1
    
        ''' To know until which node our First pointer should travel for deletion. Note length of list will always be (len-1)'''
        first_to_traverse=(len_of_list-n)
        
        '''If first element deletion is targeted '''
        if(first_to_traverse < 0):
            temp=first.next
            first=temp
            head=first
            
        '''We traverse our first pointer to the previous node of to be deleted node .Pos counter validates that'''
        while(pos <first_to_traverse and first_to_traverse!=0):
            first=first.next
            pos+=1
            
        '''Deletion happens and pointer shifting'''
        if(pos==first_to_traverse or first_to_traverse==0):
            temp=first.next.next
            first.next=temp
            
        return head
