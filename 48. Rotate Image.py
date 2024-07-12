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

    def rotate2(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def swap(matrix, i, j, p, q):
            t=matrix[i][j]
            matrix[i][j] = matrix[p][q]
            matrix[p][q] = t
        for i in range((len(matrix) + 1) // 2):
            for j in range(i, len(matrix[i]) -1 - i):
                x=i
                y=j
                for k in range(3):
                    yy=len(matrix) - 1 - x
                    x=y
                    swap(matrix, i, j, x, yy)
                    y = yy                
        # 1 列数->行数    len(matrix) -1 - 行数 = 列数
        # 2 列数->行数    len(matrix) -1 - 行数 = 列数
        # 3 列数->行数    len(matrix) -1 - 行数 = 列数
        # 4 列数->行数    len(matrix) -1 - 行数 = 列数

                    