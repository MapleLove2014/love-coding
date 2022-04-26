class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 26
        # Z
        # 27
        # A...Z (26) AA
        title = ''
        while columnNumber > 0:
            last = (columnNumber - 1) % 26
            title = chr(ord('A') + last)  + title
            columnNumber = (columnNumber - 1) // 26

        return title
s = Solution()
print(s.convertToTitle(26))
print(s.convertToTitle(52))   # AZ
print(s.convertToTitle(701))  # ZY

# 701%26 = 25
# 701/26 = 26


# 52 % 26 = 0
# 52 / 26 = 2