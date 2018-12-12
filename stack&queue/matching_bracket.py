A string of brackets is correctly matched if you can pair every opening bracket
up with a later closing bracket, and vice versa. For example, "(()())" is correctly
matched, and "(()" and ")(" are not. Implement a function which takes a string of
brackets and returns the minimum number of brackets you'd have to add to the string
to make it correctly matched. For example, "(()" could be correctly matched by
adding a single closing bracket at the end, so you'd return 1. ")(" can be correctly
matched by adding an opening bracket at the start and a closing bracket at the end,
so you'd return 2. If your string is already correctly matched, you can just return
0.


import queue

def bracket_match(bracket_string):

  right, total = 0, 0

  q = queue.LifoQueue()

  for i in range(len(bracket_string)):
    q.put(bracket_string[i])

  while not q.empty():
    char = q.get()
    if char == ')':
      right += 1
    else:
      if right > 0: right -= 1
      else: total += 1

  return total + right


a = '(()())'
b = '((())'
c = ')('

print( bracket_match(a), bracket_match(b), bracket_match(c) )
