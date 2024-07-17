class Solution:
    def minPathSum(self, grid) -> int:
        dp=[[0] * (len(grid[0])+1) for _ in range(len(grid) + 1)]
        for i in range(1, len(grid)+1):
            for j in range(1, len(grid[0])+1):
                dp[i][j] = grid[i-1][j-1] + (max(dp[i][j-1], dp[i-1][j]) if i == 1 or j == 1 else min(dp[i][j-1], dp[i-1][j]))
        return dp[-1][-1]
s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))