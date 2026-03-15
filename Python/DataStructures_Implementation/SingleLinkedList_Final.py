'''
Created on 14-Mar-2026

@author: dibyajyoti
'''


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def prepend(self,value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def append(self,value):
        node = Node(value)
        if self.length == 0:
            return self.prepend(value)
        else:
            self.tail.next = node
            self.tail = node
            self.length +=1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head =  self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        temp = self.get(index-1)
        if temp:
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length +=1
            return True
        return False

    def remove(self,index):
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -=1
        return temp

    def reverse(self):
        if self.length <= 1:
            return self
        temp = self.head
        self.head = self.tail
        self.tail = temp
        index = self.length
        before = None
        for _ in range(index):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return self

    # --- 1. Detect Cycle ---
    def has_cycle(self):
        slow= self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # --- 2. Find Middle ---
    def find_middle_node(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # --- 3. Find Cycle Start ---
    def detect_cycle_start(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.prepend(2)
    my_linked_list.prepend(3)
    my_linked_list.append(4)
    my_linked_list.append(43)
    my_linked_list.prepend(5)
    my_linked_list.print_list()
    print("\n")
    my_linked_list.reverse()
    my_linked_list.print_list()
    cycle_node = my_linked_list.head.next.next
    my_linked_list.tail.next = cycle_node
    print(my_linked_list.has_cycle())
    print("\n")
    print(my_linked_list.detect_cycle_start().value)
    print("\n")
    my_linked_list.tail.next = None
    print("\n")
    print(my_linked_list.find_middle_node().value)

