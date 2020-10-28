class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        localMin = localMax = 1
        globalMax = min(nums)
        for n in nums:
            newLocalMax = max(n, n*localMin, n*localMax)
            newLocalMin = min(n, n*localMin, n*localMax)
            globalMax = max(globalMax, newLocalMax)
            localMax = newLocalMax
            localMin = newLocalMin
        return globalMax

s = Solution()
print(s.maxProduct([2,3,-2,4]) == 6)
print(s.maxProduct([-2, 0, -1]) == 0)
print(s.maxProduct([-5, 2, 3, -2]) == 60)