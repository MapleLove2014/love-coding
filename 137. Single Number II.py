class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        def s(nums, neg):
            bits = [0]*32
            for n in nums:
                for i in range(len(bits)):
                    if n & (1 << i):
                        bits[i] += 1
            res = 0
            for i in range(len(bits)):
                res |= (bits[i] % 3) << i
            return res * neg
        # one part will return 0
        return s([ abs(min(n, 0)) for n in nums ], -1) + s([ max(0, n) for n in nums ], 1)
    
s = Solution()
print(s.singleNumber([-2,-2,-2,-1]))