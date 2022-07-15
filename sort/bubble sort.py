from curses.ascii import SO


class Solution:



    def bubbleSort(self, arr):

        if not arr or len(arr) <= 1:
            return arr
        for i in range(len(arr) - 1):
            for j in range(1, len(arr) - i):
                if arr[j-1] > arr[j]:
                    arr[j-1],arr[j] = arr[j], arr[j-1]
        return arr


s = Solution()
print(','.join(map(str, s.bubbleSort([5,4,3,2,1]))))

print(','.join(map(str, s.bubbleSort([5,1,3,2,1]))))
