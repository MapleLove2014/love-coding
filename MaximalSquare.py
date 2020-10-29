class Solution:
    def maximalSquare(self, matrix):
        maxExtend = [[0] * len(matrix[0]) for _ in range(len(matrix)) ]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '0':
                    if i != 0:
                        maxExtend[i-1][j] = 1 if matrix[i-1][j] == '1' else 0
                    if j != 0:
                        maxExtend[i][j-1] = 1 if matrix[i][j-1] == '1' else 0
                    maxExtend[i][j] = 0
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '0':
                    continue
                if maxExtend[i][j] == 1:
                    result = max(result, 1)
                else:
                    result = max(result, self.search(matrix, i, j))
        return result

    def search(self, matrix, i, j):
        if i == len(matrix) - 1 or j == len(matrix[i]):
            return 1
        extend = 0
        while True:
            if extend >= min(len(matrix) - i, len(matrix[i]) - j):
                break
            isBreak = False
            for jj in range(j, j + extend + 1):
                if matrix[i+extend][jj] != '1':
                    isBreak = True
                    break
            if isBreak:
                break
            for ii in range(i, i + extend + 1):
                if matrix[ii][j + extend] != '1':
                    isBreak = True
                    break
            if isBreak:
                break
            extend += 1
        return extend * extend

    def maximalSquareDP(self, matrix):
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                    continue
                dp[i][j] = min(0 if i == 0 else dp[i-1][j], 0 if j == 0 else dp[i][j-1], 0 if i == 0 and j == 0 else dp[i-1][j-1]) + 1
                result = max(result, dp[i][j] * dp[i][j])
        return result




s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(s.maximalSquare([["1","0"]]))
print(s.maximalSquare([["1","1"],["1","1"]]))
print(s.maximalSquare([["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]))

print(s.maximalSquareDP([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(s.maximalSquareDP([["1","0"]]))
print(s.maximalSquareDP([["1","1"],["1","1"]]))
print(s.maximalSquareDP([["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]))