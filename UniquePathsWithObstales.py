class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        result = [[0] * (n) for i in range(m)]
        result[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    result[i][j] = 0
                elif i == 0 and j > 0:
                    result[i][j] = result[i][j-1]
                elif j == 0 and i > 0:
                    result[i][j] = result[i-1][j]
                elif i > 0 and j > 0:
                    result[i][j] = result[i-1][j] + result[i][j-1]
        return result[m-1][n-1]