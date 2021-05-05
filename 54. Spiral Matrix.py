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