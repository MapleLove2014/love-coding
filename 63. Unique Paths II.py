class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp=[[0]*(len(obstacleGrid[0])+1) for _ in range(len(obstacleGrid)+1)]
        dp[1][1] = 1
        for i in range(1, len(obstacleGrid) + 1):
            for j in range(1, len(obstacleGrid[i-1]) + 1):
                dp[i][j] = dp[i][j] + dp[i-1][j] + dp[i][j-1] if obstacleGrid[i-1][j-1] == 0 else 0
        return dp[-1][-1]
