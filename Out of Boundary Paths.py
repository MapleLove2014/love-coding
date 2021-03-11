class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[[0] * n for _ in range(m)] for _ in range(N+1)]
        dirs = [-1, 0, 1, 0, -1]
        modN = pow(10, 9) + 7
        for step in range(1, N+1):
            for x in range(m):
                for y in range(n):
                    paths = 0
                    for d in range(len(dirs)-1):
                        ii = x + dirs[d]
                        jj = y + dirs[d+1]
                        if ii < 0 or jj < 0 or ii >= m or jj >= n:
                            paths += 1
                        else:
                            paths += dp[step - 1][ii][jj]
                    dp[step][x][y] = paths % modN
        return dp[N][i][j]







s = Solution()

print(s.findPaths(2, 2, 2, 0, 0))
print(s.findPaths(1, 3, 3, 0, 1))
print(s.findPaths(8, 50, 23, 5, 26))