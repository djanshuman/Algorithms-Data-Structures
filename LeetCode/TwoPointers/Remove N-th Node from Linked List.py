'''
https://algo.monster/courses/foundation/remove_nth_node

Remove N-th Node from Linked List
Problem
Given the head of a linked list and an integer n, remove the n-th node from the list (1-indexed) and return the head of the modified list.

Input:

head: the head node of a singly linked list
n: an integer representing the position of the node to remove (1-indexed)
Output:

Return the head of the modified linked list
Constraints:

The list has at least 1 node
n is a valid position in the list (1 <= n <= length of list)
Examples:

Example 1:

Input: head = [1, 2, 3], n = 1
Output: [2, 3]
Explanation: Remove the 1st node (value 1), return [2, 3]
Example 2:

Input: head = [1, 2, 3], n = 2
Output: [1, 3]
Explanation: Remove the 2nd node (value 2), return [1, 3]
Example 3:

Input: head = [1, 2, 3], n = 3
Output: [1, 2]
Explanation: Remove the 3rd node (value 3), return [1, 2]
'''

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_nth_node(head: Node, n: int) -> Node:
    # WRITE YOUR BRILLIANT CODE HERE
    if head is None or n < 1:
        return head

    dummy = Node(0)
    dummy.next = head
    curr = dummy

    for _ in range(n-1):
        if curr.next is None:
            return head
        curr = curr.next
    curr.next = curr.next.next
    return dummy.next

    

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

def format_list(node):
    if node is None:
        return
    yield str(node.val)
    yield from format_list(node.next)

if __name__ == "__main__":
    head = build_list(iter(input().split()), int)
    n = int(input())
    res = remove_nth_node(head, n)
    print(" ".join(format_list(res)))


