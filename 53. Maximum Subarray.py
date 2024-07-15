class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=0
        best=-2**31
        for n in nums:
            current = max(current + n, n)
            best = max(current, best)
        return best


