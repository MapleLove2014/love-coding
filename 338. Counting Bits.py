class Solution:
    def countBits(self, num):
        if num == 0:
            return [0]
        f = [0] * (num + 1)
        f[1] = 1
        bits = 2
        for i in range(2, num + 1):
            if i >= (1 << bits):
                bits += 1
            mask = (1 << (bits - 1)) - 1
            f[i] = 1 + f[i & mask]
        return f

s = Solution()
print(s.countBits(5))
            