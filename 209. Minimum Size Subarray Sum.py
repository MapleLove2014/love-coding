class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        left = 0
        currentSum = 0
        minLen = len(nums) + 1
        for i in range(len(nums)):
            currentSum += nums[i]
            while currentSum >= target:
                minLen = min(minLen, i - left + 1)
                currentSum -= nums[left]
                left += 1
        return 0 if minLen > len(nums) else minLen

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(6, [10, 2, 3]))


