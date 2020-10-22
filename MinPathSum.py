class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        result = [[0] * n for i in range(m)]
        result[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    result[i][j] = result[i][j-1] + grid[i][j]
                elif j == 0 and i > 0:
                    result[i][j] = result[i-1][j] + grid[i][j]
                elif i > 0 and j > 0:
                    result[i][j] = min(result[i-1][j], result[i][j-1]) + grid[i][j]
        return result[m-1][n-1]
        