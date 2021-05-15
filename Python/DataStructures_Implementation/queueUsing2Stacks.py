'''Implementation of Queue FIFO using two Stacks. Stacks are implemented using LinkedList
Note: To implement FIFO logic for stack1, we are popping from stack1 and pushing into stack2. Then popping from stack2
'''
'''Note : if stack2 is not empty then queueOperationUsing2Stacks() function will not work in FIFO mode as we will pop as LIFO.
To have stack2 behave as FIFO we have to pop all elements into a new stack3 and pop from it'''

'''For stack1'''
class Node1:
    def __init__(self,val):
        self.data1=val
        self.next1=None

'''For stack2'''
class Node2:
    def __init__(self,val):
        self.data2=val
        self.next2=None

class queueUsing2Stacks:

    def __init__(self,maxsize):
        self.maxsize_s1=maxsize
        self.maxsize_s2=maxsize
        self.top1=None
        self.tail1=None
        self.top2=None
        self.tail12=None
        self.length1=0
        self.length2=0

    '''push into stack1'''
    def push_s1(self,ele):
        if self.isFull1():
            print("Stack1 is full")
            return False

        node = Node1(ele)
        if(self.length1==0):
            self.top1=node
            self.tail1=node
            self.length1+=1
        else:
            node.next1=self.top1
            self.top1=node
            self.length1+=1
        print(self.printStack1())

    '''push into stack2'''
    def push_s2(self,ele):
        if self.isFull2():
            print("Stack2 is full")
            return False

        node = Node2(ele)
        if(self.length2==0):
            self.top2=node
            self.tail2=node
            self.length2+=1
        else:
            node.next2=self.top2
            self.top2=node
            self.length2+=1
        print(self.printStack2())

    def pop_1(self):
        if self.isEmpty1():
            print("Stack1 is empty")
            return None

        ele=self.top1.data1
        self.top1=self.top1.next1
        self.length1-=1
        return ele

    def pop2(self):
        if self.isEmpty2():
            print("Stack2 is empty")
            return None

        ele = self.top2.data2
        self.top2 = self.top2.next2
        self.length2 -= 1
        return ele

    '''shifting function, pop from stack1 and push into s2'''
    def push_s1Tos2(self):
        len=self.length1
        id=0
        while(id!=len):
            self.push_s2(self.pop_1())
            id+=1
        return True

    def isEmpty1(self):
        if(self.top1==None):
            return True
        return False

    def isFull1(self):
        if(self.length1==self.maxsize_s1):
            return True
        return False

    def isEmpty2(self):
        if(self.top2==None):
            return True
        return False

    def isFull2(self):
        if(self.length2==self.maxsize_s2):
            return True
        return False

    def printStack1(self):
        curr=self.top1
        list1=[]
        while(curr!=None):
            list1.append(curr.data1)
            curr=curr.next1
        return "Elements in stack1=> " + str(list1)

    def printStack2(self):
        curr = self.top2
        list2 = []
        while (curr!= None):
            list2.append(curr.data2)
            curr = curr.next2
        return "Elements in stack2=> " + str(list2)

    '''Functionality implementation and using of helper function to drive logic'''
    def queueOperationUsing2Stacks(self):
        if(self.length2==0):
            if(self.length1==0):
                return "Both Stacks are Empty"
            else:
                flag=self.push_s1Tos2()
                if flag==True:
                    return self.pop2()
                return False
        else:
            return self.pop2()

if __name__ == '__main__':
    s1 = queueUsing2Stacks(5)
    s1.push_s1(10)
    s1.push_s1(20)
    s1.push_s1(30)
    s1.push_s1(40)
    s1.push_s1(400)
    s1.push_s1(50)
    s1.push_s2(90)
    s1.push_s2(120)
    s1.push_s2(300)
    s1.push_s2(120)
    s1.push_s2(909)
    s1.push_s2(120)
    s1.push_s2(323)
    print(s1.printStack1())
    print(s1.printStack2())
    print(s1.queueOperationUsing2Stacks())
    print(s1.queueOperationUsing2Stacks())
    print(s1.queueOperationUsing2Stacks())
    print(s1.queueOperationUsing2Stacks())
    print(s1.queueOperationUsing2Stacks())
    print(s1.queueOperationUsing2Stacks())
    print(s1.queueOperationUsing2Stacks())
    print(s1.queueOperationUsing2Stacks())
    print(s1.queueOperationUsing2Stacks())
    print(s1.queueOperationUsing2Stacks())
    print(s1.queueOperationUsing2Stacks())

