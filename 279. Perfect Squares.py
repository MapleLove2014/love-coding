import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            for t in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], 1 + dp[i - t**2])
        return dp[-1]

s = Solution()
print(s.numSquares(12))
