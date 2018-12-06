Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest = []
        maxLen = 0

        for c in s:
          if c in longest:
            maxLen = max(maxLen, len(longest))
            longest = longest[longest.index(c)+1:]
          longest.append(c)

        maxLen = max(maxLen, len(longest))
        return maxLen


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        j = maxLen = 0
        dict = {}

        for i, char in enumerate(s):
          if char in dict and j <= dict[char]:
            j = dict[char] + 1
          else:
            maxLen = max(maxLen, i - j + 1)
          dict[char] = i

        return maxLen
