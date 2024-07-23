class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        
        for i in range(1, numRows):

            row = [ 1 ] * (len(result[-1]) + 1)
            for j in range(1, len(row) - 1):

                left = 0 if j-1 == len(result[-1]) else result[-1][j-1]
                right = 0 if j == len(result[-1]) else result[-1][j]
                row[j] = left + right
            result.append(row)
        return result
    def generate2(self, numRows: int):
        r = [[0]*numRows]
        for i in range(numRows):
            rr = [1]*(i+1)
            for x in range(1, i):
                rr[x]=r[-1][x-1] + r[-1][x]
            r.append(rr)
        return r[1:]



