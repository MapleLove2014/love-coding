class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        d = 0
        nums = sorted(nums)
        p = nums[0]
        for n in nums:
            d = max(n - p, d)
            p = n
        return d
    
s = Solution()
print(s.maximumGap([3,6,9,1]))