class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n > 0:
            c += n % 2
            n = n // 2
        return c

    def hammingWeight2(self, n: int) -> int:
        l = 0
        for i in range(32):
            p = 1 << i
            pbit = n & p
            l += pbit >> i
        return l