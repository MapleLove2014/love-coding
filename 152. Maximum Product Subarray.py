class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        # key point is negative numbers
        # if even then two loops is the same value
        # if odd we need traverse two sides and compare which product is bigger
        # cause the product cross the odd negative number is absolutely small

        p = 1
        best = -2**31
        for n in nums:
            if p == 0:
                p = 1
            p *= n
            best = max(best, p)
        p = 1
        
        for n in reversed(nums):
            if p == 0:
                p = 1
            p *= n
            best = max(best, p)
        return best




