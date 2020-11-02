class NumMatrix:

    def __init__(self, matrix):
        self.rowSums = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.rowSums[i][j] = matrix[i][j] if j == 0 else self.rowSums[i][j-1] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        rsum = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                rsum += self.rowSums[i][col2]
            else:
                rsum += self.rowSums[i][col2] - self.rowSums[i][col1-1]
        return rsum

s = NumMatrix([[-1]])
print(s.sumRegion(0, 0, 0, 0))


class NumMatrixCacheSmarter:
    def __init__(self, matrix):
        self.sums = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0:
                    self.sums[i][j] = matrix[i][j] if j == 0 else self.sums[i][j-1] + matrix[i][j]
                elif j == 0:
                    self.sums[i][j] = matrix[i][j] if i == 0 else self.sums[i-1][j] + matrix[i][j]
                else:
                    self.sums[i][j] = matrix[i][j] + self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        rsum = self.sums[row2][col2]
        if row1 > 0:
            rsum -= self.sums[row1 - 1][col2]
        if col1 > 0:
            rsum -= self.sums[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            rsum += self.sums[row1 - 1][col1 - 1]
        return rsum

ss = NumMatrixCacheSmarter([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(ss.sumRegion(1,1,2,2))
print(ss.sumRegion(2,1,4,3))
print(ss.sumRegion(1,2,2,4))
    