class Solution:

    def find(self, arr, k):

        if not arr or len(arr) == 0:
            return -1
        
        def doFind(arr, i, j, k):
            if i > j:
                return -1
            mid = i + (j - i) // 2
            if arr[mid] == k:
                return mid
            
            if k < arr[mid]:
                if k <= arr[j] and arr[mid] > arr[j]:
                    return doFind(arr, mid + 1, j, k)
                else:
                    return doFind(arr, i, mid - 1, k)
                    
            else:
                if k >= arr[i] and arr[i] > arr[mid]:
                    return doFind(arr, i, mid - 1, k)
                else:
                    return doFind(arr, mid + 1, j, k)
            return -1

        return doFind(arr, 0, len(arr) - 1, k)

s = Solution()
print(s.find([3, 4, 1, 2], 3) == 0)
print(s.find([3, 1, 2], 3) == 0)
print(s.find([3, 1, 2], 1) == 1)
print(s.find([3, 1, 2], 2) == 2)
print(s.find([10, 11, 12, 13, 1, 2, 3, 4], 10) == 0)
print(s.find([10, 11, 12, 13, 1, 2, 3, 4], 12) == 2)
print(s.find([10, 11, 12, 13, 1, 2, 3, 4], 13) == 3)
print(s.find([10, 11, 12, 13, 1, 2, 3, 4], 1) == 4)
print(s.find([10, 11, 12, 13, 1, 2, 3, 4], 4) == 7)
