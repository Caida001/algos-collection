Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.



def numSquares(self, n):
    if n < 2:
        return n
    lst = []
    i = 1
    while i * i <= n:
        lst.append( i * i )
        i += 1
    cnt = 0
    toCheck = {n}
    while toCheck:
        cnt += 1
        temp = set()
        for x in toCheck:
            for y in lst:
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x-y)
        toCheck = temp

    return cnt



_f = [0]
def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    f = self._f
    while len(f) <= n:
        temp = f[-1]
        j = 1
        while j*j <= len(f):
            temp = min(temp,f[-j*j])
            j += 1
        f.append(temp + 1)
    return f[n]
