Given a n,m which means the row and column of the 2D matrix and an array of pair
A( size k). Originally, the 2D matrix is all 0 which means there is only sea in
the matrix. The list pair has k operator and each operator has two integer A[i].x,
 A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island.
 Return how many island are there in the matrix after each operator.

Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].

Notice
0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent,
 we consider them in the same island. We only consider up/down/left/right adjacent.



class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):

        res = []
        count = 0
        roots = [-1 for _ in range(m*n)]
        dirs = [[0,-1], [-1, 0], [0,1], [1,0]]
        for pos in operators:
            id = m * pos.x + pos.y
            if roots[id] == -1:
                roots[id] = id
                count += 1
            for dir in dirs:
                x = pos.x + dir[0]
                y = pos.y + dir[1]
                cur_id = m * x + y
                if x < 0 or x >= n or y < 0 or y >= m or roots[cur_id] == -1: continue
                p = self.findRoot(roots, cur_id)
                q = self.findRoot(roots, id)
                if p != q:
                    roots[p] = q
                    count -= 1
            res.append(count)

        return res

    def findRoot(self, roots, id):
        if id == roots[id]:
            return id
        else:
            self.findRoot(roots, roots[id])
