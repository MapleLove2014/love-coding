# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 4
class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        while i <= j:
            mid = i + (j - i) // 2
            if isBadVersion(mid):
                if mid - 1 > 0:
                    if isBadVersion(mid - 1):
                        j = mid - 1
                    else:
                        return mid
                else:
                    return mid
            else:
                i = mid + 1
        return i
    
    def firstBadVersion2(self, n: int) -> int:
        i = 1
        j = n
        while i <= j:
            mid = i + (j - i) // 2
            if isBadVersion(mid):
                j = mid
            else:
                i = mid + 1
        return i


s = Solution()
print(s.firstBadVersion(5))