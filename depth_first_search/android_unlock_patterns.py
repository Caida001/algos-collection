Description
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9,
 count the total number of unlock patterns of the Android lock screen, which
 consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any
other keys, the other keys must have previously selected in the pattern. No
jumps through non selected key is allowed.
The order of keys used matters.
android unlock
Explanation:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Have you met this question in a real interview?
Example
Given m = 1, n = 1, return 9.


class Solution:
    """
    @param m: an integer
    @param n: an integer
    @return: the total number of unlock patterns of the Android lock screen
    """
    def numberOfPatterns(self, m, n):
        # Write your code here
        res = 0
        visited = [False] * 10
        jumps = [[0 for i in range(10)] for j in range(10)]
        jumps[1][3] = jumps[3][1] = 2
        jumps[4][6] = jumps[6][4] = 5
        jumps[7][9] = jumps[9][7] = 8
        jumps[1][7] = jumps[7][1] = 4
        jumps[2][8] = jumps[8][2] = 5
        jumps[3][9] = jumps[9][3] = 6
        jumps[1][9] = jumps[9][1] = jumps[3][7] = jumps[7][3] = 5

        i = m
        while i <= n:
            res += self.dfs(visited, jumps, 1, i-1)*4
            res += self.dfs(visited, jumps, 2, i-1)*4
            res += self.dfs(visited, jumps, 5, i-1)
            i += 1

        return res

    def dfs(self, visited, jumps, cur, remain):
        if remain < 0: return 0
        if remain == 0: return 1
        visited[cur] = True
        res = 0
        i = 1
        while i <= 9:
            if not visited[i] and (jumps[cur][i] == 0 or visited[jumps[cur][i]]):
                res += self.dfs(visited, jumps, i, remain-1)
            i += 1

        visited[cur] = False
        return res 
