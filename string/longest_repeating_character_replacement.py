Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.



class Solution:
    def characterReplacement(self, s, k):
        # idea, use sliding window, move end and obtain the freq of each letter. get the max_cnt, if end-start+1-max_cnt > k, need to reduce count of start by 1, and move start forward. update the max_len. Time O(n), Space O(1).
        # only 26 letters, can use array; other case, can use Counter
        count = collections.Counter() # count = [0] * 26
        start, max_cnt, max_len = 0, 0, 0
        for end in range(len(s)):
            count[s[end]] += 1 # count[ord(s[end]) - ord('A')] += 1
            max_cnt = max(max_cnt, count[s[end]])
            while end - start + 1 - max_cnt > k: # need to reduce the sliding window
                count[s[start]] -= 1 # reduce the count of start letter
                start += 1 # move forward start
            max_len = max(max_len, end - start + 1)
        return max_len