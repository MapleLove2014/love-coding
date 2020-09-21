import sys
class Solution:
    def maxSubArray(self, nums):
        f = [-sys.maxsize] * (len(nums))
        result = -sys.maxsize
        for i in range(len(nums)):
            if i == 0:
                f[i] = nums[i]
            else:
                f[i] = max(f[i-1] + nums[i], nums[i])
            if f[i] > result:
                result = f[i]
        return result

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))