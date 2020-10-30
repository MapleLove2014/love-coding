class Solution:
    def nthUglyNumber(self, n):
        if n == 1:
            return 1
        un = [0] * (n + 1)
        un[1] = 1
        p2 = 1
        p3 = 1
        p5 = 1

        for i in range(2, n+1):
            cun = min(un[p2] * 2, un[p3] * 3, un[p5] * 5)
            un[i] = cun
            if cun == un[p2] * 2:
                p2 += 1
            if cun == un[p3] * 3:
                p3 += 1
            if cun == un[p5] * 5:
                p5 += 1
        return un[-1]

s = Solution()
print(s.nthUglyNumber(10))




