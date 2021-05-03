class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotate(matrix, i):
            if i >= len(matrix) // 2:
                return
            if len(matrix) <= 1:
                return
            n = len(matrix) - i * 2

            for j in range(i, len(matrix) - i - 1):
                preElement = matrix[i][j]
                nextI = i
                nextJ = j
                while True:
                    
                    temp = nextJ
                    nextJ = len(matrix) - 1 - nextI
                    nextI = temp

                    temp = preElement
                    preElement = matrix[nextI][nextJ]
                    matrix[nextI][nextJ] = temp
                    if nextI == i and nextJ == j:
                        break
            rotate(matrix, i+1)
        rotate(matrix, 0)


                    