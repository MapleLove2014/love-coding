class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        values = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                values[i] = max(values[i], nums[i])
            elif i == 1:
                values[i] = max(values[i-1], nums[i])
            else:
                values[i] = max(values[i-2] + nums[i], values[i-1])
        return values[-1]

s = Solution()
print(s.rob([2,7,9,3,1]))
        