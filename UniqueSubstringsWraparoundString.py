class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        if len(p) == 1:
            return 1
        count = [0] * 26
        count[ord(p[0]) - ord('a')] = 1
        prevChar = p[0]
        maxLenEndWithC = 1
        for c in p[1:]:
            if ord(c) - ord(prevChar) == 1 or ord(prevChar) - ord(c) == 25:
                maxLenEndWithC += 1
            else:
                maxLenEndWithC = 1
            prevChar = c
            count[ord(c) - ord('a')] = max(count[ord(c) - ord('a')], maxLenEndWithC)
        
        return sum(count)

s = Solution()
print(s.findSubstringInWraproundString('abcdbcd'))
print(s.findSubstringInWraproundString('zab'))

