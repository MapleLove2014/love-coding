class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return sum([i for i in range(n+1)]) - sum(nums)
