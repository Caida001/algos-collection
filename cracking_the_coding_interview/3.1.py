Three in One: Describe how you could use a single array to implement three stacks.

class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * stacksize * self.numstacks
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.indexOfTop(stacknum)]
        self.array[self.indexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.indexOfTop(stacknum)]

    def isEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def isFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def indexOfTop(self, stacknum):
        return stacknum * self.stacksize + self.sizes[stacknum] - 1
