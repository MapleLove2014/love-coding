class Solution:
    def PredictTheWinner(self, nums):
        if not nums or len(nums) <= 1:
            return True
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(dp)):
            dp[i][i] = nums[i]
        for iteration in range(1, len(dp)):
            i = 0
            for j in range(iteration, len(dp)):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
                i += 1
        return dp[0][len(dp) - 1] >= 0

s = Solution()
print(s.PredictTheWinner([1,2,3,4]))
print(s.PredictTheWinner([1,2,223,4]))
print(s.PredictTheWinner([1,222,4]))
