
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stackUsingLinkedList:

    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.tail=None
        self.top=None
        self.length=0

    def push(self,ele):
        if self.isFull():
            print("Stack is Full")
            return

        if(self.length==0):
            node = Node(ele)
            self.top=node
            self.tail=node
            self.length+=1

        else:
            node = Node(ele)
            nxt_node=self.top
            self.top=node
            node.next=nxt_node
            self.length+=1
        print(s.printStack())


    def pop(self):

        if(self.isEmpty()):
            return "Stack is Empty"

        if(self.length==1):
            element=self.top.data
            self.top=None
            self.tail=None
            self.length-=1
            return "Popped element of stack:"+str(element)
        elif(self.length >1):
            element = self.top.data
            self.top = self.top.next
            self.length -= 1
            return "Popped element of stack:" + str(element)

    def isEmpty(self):
        if self.top == None:
            return True
        return False

    def isFull(self):
        if self.length == self.maxsize:
            return True
        return False

    def printStack(self):
        if self.isEmpty():
            return self.top
        list1=[]
        ind=0
        currvalue=self.top
        while(currvalue!= None):
            list1.append(currvalue.data)
            currvalue=currvalue.next
        return "Elements in stack:"+str(list1)

    def findTopElement(self):
        return "Top element of stack"":"+str(self.top.data)

    def peek(self,pos):

        if (pos < 0 or pos > self.length):
            return "Enter a valid pos between 1 to length of stack"

        elif(pos > 0 and pos <=(self.length)):
            ind=1
            to_traverse=(self.length-pos)+1
            currvalue=self.top
            while(ind !=to_traverse):
                currvalue=currvalue.next
                ind+=1
            return currvalue.data


s=stackUsingLinkedList(5)
s.push(10)
s.push(20)
s.push(100)
s.push(334)
s.push(994)
s.push(233)
print(s.printStack())
print(s.pop())
print(s.printStack())
print(s.findTopElement())
print(s.peek(5))
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
s.push(20)
s.push(100)