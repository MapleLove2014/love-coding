class Solution:
    def combinationSum4(self, nums, target):
        if not nums or target <= 0:
            return 0
        
        dp = [0] * (target + 1)
        dp[0] = 1
        sortedNums = sorted(nums)
        for i in range(1, target + 1):
            for n in sortedNums:
                if i >= n:
                    dp[i] += dp[i-n]
                else:
                    break
        return dp[-1]
        
s = Solution()
print(s.combinationSum4([1, 2, 3], 4))
        