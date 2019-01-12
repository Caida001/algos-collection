Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.


class Node(object):
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None

class Stack(object):
    def __init__(self, threshold):
        self.threshold = threshold
        self.size = 0
        self.top = None
        self.bottom = None

    def isFull(self):
        return self.size == self.threshold

    def isEmpty(self):
        return self.size == 0

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def push(self, v):
        if self.size == self.threshold: return False
        self.size += 1
        n = Node(v)
        if self.size == 1: self.bottom = n
        self.join(n, self.top)
        self.top = n
        return True

    def pop(self):
        if not self.top: return None
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value

    def removeBottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom: self.bottom.below = None
        self.size -= 1
        return b.value


class StackPlates:
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []

    def getLastStack(self):
        if not self.stacks: return None
        return self.stacks[-1]

    def isEmpty(self):
        last = self.getLastStack()
        return not last or last.isEmpty()

    def push(self, el):
        last = self.getLastStack()
        if last and not last.isFull():
            last.push(el)
        else:
            stack = Stack(self.threshold)
            stack.push(el)
            self.stacks.append(stack)

    def pop(self):
        last = self.getLastStack()
        if not last:
            return None
        el = last.pop()
        if last.size == 0: del self.stacks[-1]
        return el

    def popAt(self, index):
        return self.shift(index, True)

    def shift(self, index, removeTop):
        stack = self.stacks[index]
        removed = stack.pop() if removeTop else stack.removeBottom()
        if stack.isEmpty():
            del self.stacks[index]
        elif len(self.stacks) > index + 1:
            el = self.shift(index+1, False)
            stack.push(el)
        return removed
