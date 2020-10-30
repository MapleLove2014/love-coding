class Solution:
    def numSquares(self, n):
        f = [0] * (n+1)
        f[1] = 1
        for i in range(2, n+1):
            minSquares = i
            for e in range(1, n):
                square = e * e
                if square > i:
                    break
                if square == i:
                    minSquares = 1
                    break
                minSquares = min(minSquares, f[i - square] + 1)
            f[i] = minSquares
        return f[-1]

s = Solution()
print(s.numSquares(13))
print(s.numSquares(12))