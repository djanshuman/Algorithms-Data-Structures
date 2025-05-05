""" Node Class"""


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


'''Linked List Operation Class'''


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index - 1)
        if temp:
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            self.print_list()
            return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        prev = self.get(index - 1)
        temp = prev.next
        if prev:
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

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
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        self.print_list()
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        self.print_list()
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.data = value
            return True
        return False

    def print_list(self):
        temp = self.head
        list1 = []
        while temp is not None:
            list1.append(temp.data)
            temp = temp.next
        print(list1, 'Length = ' + str(self.length))

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


ll = LinkedList(10)
ll.prepend(20)
ll.print_list()
ll.append(100)
ll.print_list()
ll.pop()
ll.pop()
ll.pop()
ll.prepend(99)
ll.prepend(90)
ll.append(100)
ll.print_list()
print(ll.get(0))
ll.pop()
ll.pop()
ll.set_value(0, 9999)
ll.print_list()
ll.prepend(99)
ll.prepend(90)
ll.append(100)
ll.print_list()
ll.set_value(-1, 10000)
ll.print_list()
ll.insert(4, 78)
ll.print_list()
ll.remove(1)
ll.print_list()
ll.reverse()
ll.print_list()

'''
LL Operations:

1. Append
2. prepend
3. pop
4. print list
5. pop_first
6. get
7. set_value
8. insert
9. remove
10.reverse
'''
