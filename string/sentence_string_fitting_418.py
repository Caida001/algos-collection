Given a rows x cols screen and a sentence represented by a list of words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word won't exceed 10.
1 ≤ rows, cols ≤ 20,000.


Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.


Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.


Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.



import math

class Solution:
  def wordsTyping(sentence, rows, cols):
    s = ' '.join(sentence) + " "
    start, l = 0, len(s)
    for i in range(rows):
      start += cols
      if s[start%l] == ' ':
        start += 1
      else:
        while start > 0 and s[(start-1) % l] != ' ':
          start -= 1

    return math.floor(start/l)


m = Solution
print(m.wordsTyping(["I", "had", "apple", "pie"], 4, 5))
