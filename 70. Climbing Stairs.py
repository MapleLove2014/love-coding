class Solution:
    def climbStairs(self, n):
        f = [0] * (n + 1)
        f[0] = 0
        f[1] = 1
        if n == 1:
            return f[1]
        f[2] = 2
        if(n == 2):
            return f[2]
        for i in range(3, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]
s = Solution()
print(s.climbStairs())