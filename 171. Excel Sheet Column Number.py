class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # AB

        n = 0
        while columnTitle:
            n = n * 26 + (ord(columnTitle[0]) - ord('A') + 1)
            columnTitle = columnTitle[1:]
        return n

s = Solution()
print(s.titleToNumber('ZY'))