class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        dirh = [0, 1, 0, -1]
        dirv = [1, 0, -1, 0]
        diri = 0
        i = 0
        j = 0
        for num in range(1, n * n + 1):
            matrix[i][j] = num
            if i + dirh[diri] < 0 or i + dirh[diri] == n or j + dirv[diri] < 0 or j + dirv[diri] == n or matrix[i + dirh[diri]][j + dirv[diri]] != 0:
                diri = (diri + 1) % 4
            i = i + dirh[diri]
            j = j + dirv[diri]
        return matrix



