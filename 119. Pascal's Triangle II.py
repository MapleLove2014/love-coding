class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        result = [[1]]
        
        for i in range(1, rowIndex + 1):

            row = [ 1 ] * (len(result[-1]) + 1)
            for j in range(1, len(row) - 1):

                left = 0 if j-1 == len(result[-1]) else result[-1][j-1]
                right = 0 if j == len(result[-1]) else result[-1][j]
                row[j] = left + right
            result.append(row)
        return result[-1]
    def getRow2(self, rowIndex: int):
        r = []
        for i in range(rowIndex+1):
            rr = [1]*(i+1)
            for x in range(1, i):
                rr[x]=r[x-1] + r[x]
            r = rr
        return rr

