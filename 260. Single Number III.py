class Solution:
    def singleNumber(self, nums):
        xa = 0
        for x in nums:
            xa = x ^ xa
        fb = 0
        for i in range(32):
            if xa & (1 << i):
                fb = (1 << i)
                break
        f = 0
        for x in nums:
            if x & fb:
                f = f ^ x
        return [f, f^xa]
    
s = Solution()
print(s.singleNumber([1,2,1,3,2,5]))
