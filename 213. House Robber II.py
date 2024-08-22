class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return self.doRob(nums)

    def doRob(self, nums):
        return max(self.robbing(0, nums, True, 0, 0), self.robbing(0, nums, False, 0, 0))

    def robbing(self, i, nums, robFirst, value1, value2):
        if i == 0:
            return self.robbing(i + 1, nums, robFirst, nums[i] if robFirst else 0, value2)
        if i == len(nums) - 1:
            return max(value1, value2 + (0 if robFirst else nums[i]))
        if i == 1:
            return self.robbing(i + 1, nums, robFirst, value1 if robFirst else max(value1, value2 + nums[i]), value1)
        return self.robbing(i + 1, nums, robFirst, max(value1, value2 + nums[i]), value1)


    def rob2(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [[0]*(len(nums) + 1) for _ in range(2)]
        dp[1][1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[0][i] = max(dp[0][i-2] + nums[i-1], dp[0][i-1])
            dp[1][i] = max(dp[1][i-2] + nums[i-1], dp[1][i-1])
        return max(dp[0][-1], dp[1][-2])

s = Solution()
print(s.rob([2, 3, 2]) == 3)
print(s.rob([1,2,3,1]) == 4)