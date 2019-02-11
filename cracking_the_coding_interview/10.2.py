Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
each other.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strs:
          ans[tuple(sorted(s))].append(s)
        return ans.values()