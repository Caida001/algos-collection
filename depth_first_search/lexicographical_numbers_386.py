Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may
be as large as 5,000,000.

class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []

        def dfs(curSum):
          if curSum > n:
            return
          res.append(curSum)
          curSum *= 10
          for i in range(10):
            dfs(curSum + i)

        for i in range(1, min(10, n+1)):
          dfs(i)
        return res
