class Solution:
    def findTargetSumWays(self, nums, S) -> int:
        maxTarget = sum(nums)
        if maxTarget < abs(S):
            return 0
        dp = [[0] * (2 * maxTarget + 1) for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(-maxTarget, maxTarget + 1):
                if i == 0:
                    if j != nums[i] and j != -nums[i]:
                        dp[i][j] = 0
                    elif j == nums[i] and j == 0:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = (0 if abs(j - nums[i]) > maxTarget else dp[i-1][j - nums[i]]) + (0 if abs(j + nums[i]) > maxTarget else dp[i-1][j + nums[i]])
        return dp[len(nums)-1][S]

s = Solution()
print(s.findTargetSumWays([0, 0, 1], 1))
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(s.findTargetSumWays([1], 2))
print(s.findTargetSumWays([1, 0], 1))
