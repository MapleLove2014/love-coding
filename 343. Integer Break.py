import sys

class Solution:
    def integerBreak(self, n):
        f = [0] * ( n + 1 )
        f[1] = 1
        for i in range(2, n + 1):
            maxProduct = 1
            for j in range(1, i - 1):
                maxProduct = max(maxProduct, j * max(f[i - j], i - j))
            f[i] = maxProduct
        return f[-1]

s = Solution()
print(s.integerBreak(10))
print(s.integerBreak(2))