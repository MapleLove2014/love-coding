class Solution:
    def minimumTotal(self, triangle) -> int:
        dp = [[0] * (len(triangle[-1]) + 1) for _ in range(len(triangle) + 1)]
        for r in reversed(range(len(triangle))):
            for i in range(len(triangle[r])):
                dp[r][i] = triangle[r][i] + min(dp[r+1][i], dp[r+1][i+1])
        return dp[0][0]
s = Solution()
print(s.minimumTotal([[-10]]))
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))

