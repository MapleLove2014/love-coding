class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def s(matrix, i, j, k, t, target, mem):
            if i > j or k > t:
                return False
            key = f"{i}-{j}-{k}-{t}"
            if key in mem:
                return mem[key]
            m = i + (j - i) // 2
            mc = k + (t - k) // 2
            if matrix[m][mc] == target:
                mem[key] = True
                return True
            r = False
            if matrix[m][mc] > target:
                r = s(matrix, i, m - 1, k, t, target, mem) or s(matrix, i, j, k, mc - 1, target, mem)
            else:
                r = s(matrix, m+1, j, k, t, target, mem) or s(matrix, i, j, mc + 1, t, target, mem) 
            mem[key] = r
            return r


        rs = len(matrix)
        cs = len(matrix[0])
        i = 0
        j = rs - 1 
        k = 0
        t = cs - 1

        return s(matrix, i, j, k, t, target, {})


    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        rs = len(matrix)
        cs = len(matrix[0])
        i = 0
        j = cs - 1
        while i < rs and j >= 0:
            if target == matrix[i][j]:
                return True
            if target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False




