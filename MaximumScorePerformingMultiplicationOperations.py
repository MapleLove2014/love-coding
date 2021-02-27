import sys
class Solution:
    # score(i,j)表示nums[i...j]范围内能获得的最大分数
    # 
    # dp[i][k]表示前面选i个，选k个multiplier能获得的最大分数
    def maximumScore(self, nums, multipliers) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[False] * m for _ in range(m)]
        def getScore(i, j):
            usedNumber = i + 1 + (n - j) - 1
            if usedNumber > m:
                return 0
            k = usedNumber - 1
            if dp[i][k] != False:
                return dp[i][k]
            dp[i][k] = max(nums[i] * multipliers[k]+ getScore(i + 1, j), nums[j] * multipliers[k] + getScore(i, j-1))
            return dp[i][k]

        if not multipliers or len(multipliers) == 0:
            return 0
        if not nums or len(nums) == 0:
            return 0
        
        return getScore(0, n-1)

    def bottomUpDp(self, nums, multipliers):
        n = len(nums)
        m = len(multipliers)

        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for k in range(1, m+1):
            for i in range(k + 1):
                j = k - i
                dp[i][j] = max(
                    -sys.maxsize if i == 0 else dp[i-1][j] + nums[i-1] * multipliers[k-1],
                    -sys.maxsize if j == 0 else dp[i][j-1] + nums[n-j] * multipliers[k-1]
                )
        score = -sys.maxsize
        for i in range(m + 1):
            score = max(score, dp[i][m-i])
        return score




s = Solution()
print(s.maximumScore([1,2,3], [1,2,3]))
print(s.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))
print(s.bottomUpDp([1,2,3], [1,2,3]))
print(s.bottomUpDp([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))
print(s.bottomUpDp([172,-967,-632], [3,-536]))


