class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        i = 0
        j = n - 1
        while  i <= j:
            mid = i + (j - i) // 2
            if n - mid == citations[mid]:
                return n - mid
            elif n - mid < citations[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return n - i
s = Solution()
print(s.hIndex([100, 101]))
print(s.hIndex([0,1,3,5,6]))
print(s.hIndex([1,1,3]))
        