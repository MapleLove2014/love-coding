class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        dp[1][1]=1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j] + dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

