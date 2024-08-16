class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ns = right - left + 1
        res = 0
        for i in range(32):
            bs = 1 << i
            lb = left & bs
            rb = right & bs
            if ns > 2 ** i or lb == 0 or rb == 0:
                continue
            res = res | bs
        return res
s = Solution()
print(s.rangeBitwiseAnd(5, 7))



