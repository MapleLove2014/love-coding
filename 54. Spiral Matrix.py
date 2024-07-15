class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def trace(matrix, i, j, result):
            ilimit = len(matrix) - i - 1
            jlimit = len(matrix[0]) - j - 1
            
            if i > ilimit or j > jlimit:
                return

            ii = i
            jj = j
            # -------->
            while jj <= jlimit:
                result.append(matrix[ii][jj])
                jj += 1
            jj -= 1
            ii += 1
            if ii > ilimit:
                return
            while ii <= ilimit:
                result.append(matrix[ii][jj])
                ii += 1
            ii -= 1
            jj -= 1
            if jj < j:
                return
            while jj >= j:
                result.append(matrix[ii][jj])
                jj -= 1
            jj += 1
            ii -= 1
            while ii > i:
                result.append(matrix[ii][jj])
                ii -= 1
            trace(matrix, i+1, j+1, result)

        result = []
        trace(matrix, 0, 0, result)
        return result


    def simplify(self, matrix):


        dirh = [0, 1, 0, -1]
        dirv = [1, 0, -1, 0]

        di = 0

        r = len(matrix)
        c = len(matrix[0])
        seen = [[False] * c for _ in range(r)]
        result = []
        i = 0
        j = 0
        for _ in range(c * r):
            result.append(matrix[i][j])
            seen[i][j] = True
            if i + dirh[di] < 0 or j + dirv[di] < 0 or i + dirh[di] == r or j + dirv[di] == c or seen[i + dirh[di]][j + dirv[di]]:
                di = (di + 1) % 4
            i = i + dirh[di]
            j = j + dirv[di]
        return result
    
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        x=0
        y=0
        d=[[0,1], [1,0], [0, -1], [-1,0]]
        di=0
        result = []
        for _ in range(len(matrix) * len(matrix[0])):
            result.append(matrix[x][y])
            matrix[x][y] = True
            if x + d[di][0] < 0 or y + d[di][1] < 0 or x+d[di][0] == len(matrix) or y+d[di][1] == len(matrix[0]) or matrix[x+d[di][0]][y+d[di][1]] == True:
                # change direction
                di += 1
                di = di % 4
            x = x + d[di][0]
            y = y + d[di][1]
        return result