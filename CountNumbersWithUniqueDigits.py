class Solution:
    def countNumbersWithUniqueDigits(self, n):
        f = [0] * (n+1)
        f[0] = 1
        for i in range(1, n+1):
            f[i] = 9 * self.make(i) + f[i-1]
        return f[-1]

    def make(self, n):
        seq = 9
        product = 1
        while n - 1 > 0:
            product *= seq
            n -= 1
            seq -= 1
        return product

s = Solution()
print(s.countNumbersWithUniqueDigits(1))
print(s.countNumbersWithUniqueDigits(2))
print(s.countNumbersWithUniqueDigits(3))