class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        j = 0
        for i in range(len(t)):
            if j >= len(s):
                return True
            if s[j] == t[i]:
                j += 1
        return False if j < len(s) else True

s = Solution()
print(s.isSubsequence('abc', 'ahbgdc'))