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
    

    def minSubArrayLen2(self, target: int, nums: list[int]) -> int:
        i = 0
        s = 0
        r = len(nums) + 1
        for j in range(len(nums)):
            s += nums[j]
            while s >= target:
                r = min(r, j - i + 1)
                s -= nums[i]
                i += 1
        return 0 if r > len(nums) else r

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(6, [10, 2, 3]))


