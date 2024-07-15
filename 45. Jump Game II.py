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
    def jump2(self, nums: List[int]) -> bool:
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if dp[j] >= 0 and nums[j] >= i - j:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

