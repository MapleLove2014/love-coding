class Solution:
    def grayCode(self, n: int):
        if n < 0:
            return []
        dp = [0]
        for i in range(1, n + 1):
            dp = dp + [x | 1 << (i - 1) for x in reversed(dp)]
        return dp

s = Solution()
print(s.grayCode(2))
print(s.grayCode(3))