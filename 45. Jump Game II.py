class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):

            # jump from index j
            for j in range(i):
                if nums[j] >= i - j:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

