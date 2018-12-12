553. Bomb Enemy
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.

Example
Given a grid:

0 E 0 0
E 0 W E
0 E 0 0
return 3. (Placing a bomb at (1,1) kills 3 enemies)

Notice
You can only put the bomb at an empty cell.



class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0]) if m else 0
        result, rowkills = 0, 0
        colkills = [0 for i in range(n)]
        if m == 0 or n == 0: return 0

        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == "W":
                    rowkills = 0
                    for k in range(j, n):
                        if grid[i][k] == "W":
                            break
                        if grid[i][k] == "E":
                            rowkills += 1

                if i == 0 or grid[i-1][j] == "W":
                    colkills[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == "W":
                            break
                        if grid[k][j] == "E":
                            colkills[j] += 1

                if grid[i][j] == "0" and rowkills + colkills[j] > result:
                    result = rowkills + colkills[j]

        return result
                
