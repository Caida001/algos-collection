Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

def sortStack(stack):
    res = []
    while(len(stack) > 0):
        item = stack.pop()
        while len(res) > 0 and item < res[-1]:
            stack.append(res.pop())
        res.append(item)

    return res
