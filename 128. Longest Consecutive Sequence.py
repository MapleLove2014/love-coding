class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        d=set(nums)
        gl = 0
        for n in d:
            if n-1 not in d:
                # n is a start number
                l = 1
                while n+l in d:
                    l += 1
                gl = max(l, gl)
        return gl


    
s = Solution()
print(s.longestConsecutive([100,4,2,200,1,3,2]))
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))





