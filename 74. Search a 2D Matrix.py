class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        

        def findRow(matrix, start, end, target):
            if start > end:
                return -1
        
            mid = (end + start) // 2
            if target >=matrix[mid][0] and target <= matrix[mid][-1]:
                return mid
            if target < matrix[mid][0]:
                return findRow(matrix, start, mid - 1, target)
            else:
                return findRow(matrix, mid + 1, end, target)
        
        def findInRow(row, i, j, target):
            if i > j:
                return False
            mid = (i + j) // 2
            if row[mid] == target:
                return True
            if row[mid] > target:
                return findInRow(row, i, mid - 1, target)
            return findInRow(row, mid + 1, j, target)

        r = findRow(matrix, 0, len(matrix) - 1, target)
        return r >= 0 and findInRow(matrix[r], 0, len(matrix[r])-1, target)


s = Solution()
print(s.searchMatrix([[1]], 0))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))