Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class StackMin:
    def __init__(self):
        self.stack = []


    def push(self, el):
        if len(self.stack) > 0:
            self.stack.append([el, min(el, self.stack[-1][1])])
        else:
            self.stack.append([el, el])

    def pop(self):
        res = self.stack[-1][0]
        self.stack = self.stack[:-1]
        return res

    def min(self):
        return self.stack[-1][1] 
