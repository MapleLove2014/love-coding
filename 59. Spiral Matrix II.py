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
    def generateMatrix2(self, n: int):
        
        m=[[0]*n for i in range(n)]
        i=0
        j=-1
        d=[[0,1], [1,0], [0,-1], [-1,0]]
        di=0
        for v in range(1, n**2 + 1):
            if i+d[di][0] < 0 or i+d[di][0] == n or j+d[di][1] < 0 or j+d[di][1]==n or m[i+d[di][0]][j+d[di][1]] > 0:
                di = (di + 1) % 4
            i += d[di][0]
            j += d[di][1]
            m[i][j] = v
        return m


