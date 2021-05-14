class stackUsingArray:

    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.stack=[None]*maxsize
        self.top=-1

    def push(self,ele):
        if self.isFull():
            print("Stack is full")
            return
        self.top+=1
        self.stack[self.top]=ele
        s.printStack()

    def pop(self):
        if self.isEmpty():
            return self.top

        ele=self.stack[self.top]
        self.stack[self.top]=None
        self.top-=1
        return "Popped element:"+str(ele)

    def isFull(self):
        if self.top == self.maxsize -1:
            return True
        return False

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def peek(self,pos):
        if(pos > 0 and pos <= self.maxsize):
            return "element at position "+str(pos)+" is "+str(self.stack[(self.top-pos)+1])
        else:
            return "Return a valid position (1 - Maxsize of stack)"

    def findTopElement(self):
        return "Top Element of stack:"+str(self.stack[self.top])

    def length_of_stack(self):
        if self.isEmpty():
            return 0
        else:
            return (self.top)+1

    def printStack(self):
        list1=[]
        if self.isEmpty():
            return self.stack
        ind=0
        while(ind < (self.top+1)):
            list1.append(self.stack[ind])
            ind+=1
        print(list1,":length of stack:",self.length_of_stack())

if __name__ == '__main__':
    s = stackUsingArray(5)
    s.push(10)
    s.push(20)
    s.push(23)
    s.push(100)
    s.push(234)
    print(s.pop())
    s.printStack()
    s.push(190)
    s.push(223)
    print(s.peek(4))
    print(s.findTopElement())


