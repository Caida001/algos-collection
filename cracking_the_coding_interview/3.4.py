Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack2.append(x)

    def pop(self):
        if not self.stack1:
            while len(self.stack2) > 0: self.stack1.append(self.stack2.pop())

        return self.stack1.pop()

    def peek(self):
        if not self.stack1:
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())
        return self.stack1[0]

    def empty(self):
        if(len(self.stack1) == 0) and (len(self.stack2) == 0): return True
        return False 
