class Solution:
    def uniquePaths(self, m, n):
        result = [[0] * (n+1) for i in range(m+1)]
        result[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j > 1:
                    result[i][j] = result[i][j-1]
                elif j == 1 and i > 1:
                    result[i][j] = result[i-1][j]
                elif i > 1 and j > 1:
                    result[i][j] = result[i-1][j] + result[i][j-1]
        return result[m][n]
s = Solution()
print(s.uniquePaths(7, 3) == 28)