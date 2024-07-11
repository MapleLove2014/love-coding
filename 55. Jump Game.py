class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # dp[i] -> whether you are able to jump to index i
        # dp[i] = 
        dp = [False] * len(nums)

        dp[0] = True

        for i in range(1, len(nums)):

            for j in range(i-1, -1, -1):

                if j + nums[j] >= i and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]
    
    def canJump2(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if dp[j] and nums[j] >= i - j:
                    dp[i] = True
                    break
        return dp[-1]






