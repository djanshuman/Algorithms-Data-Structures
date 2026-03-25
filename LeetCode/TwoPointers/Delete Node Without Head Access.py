'''
https://algo.monster/courses/foundation/delete_node_without_head

Delete Node Without Head Access
Problem
Given the head of a linked list and a position, delete the node at that position without having direct access to the previous node. You must delete the node by only accessing the node itself.

This problem simulates a scenario where you're given a pointer to a node in the middle of a linked list and asked to delete it without access to the head or previous nodes.

Input:

head: the head node of a singly linked list
position: an integer representing the position of the node to delete (1-indexed)
Output:

Return the head of the modified linked list
Constraints:

The list has at least 2 nodes
The node to delete is not the last node
Position is valid (1 <= position < length of list)
Examples:

Example 1:

Input: head = [1, 2, 3, 4], position = 2
Output: [1, 3, 4]
Explanation: Delete node at position 2 (value 2)
Example 2:

Input: head = [4, 5, 1, 9], position = 3
Output: [4, 5, 9]
Explanation: Delete node at position 3 (value 1)
'''
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def delete_node_without_head(head, position):
    currvalue = head
    for _ in range(position - 1):
        currvalue = currvalue.next
    
    currvalue.val = currvalue.next.val
    currvalue.next = currvalue.next.next
    return head
    

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
    position = int(input())
    res = delete_node_without_head(head, position)
    print(" ".join(format_list(res)))


