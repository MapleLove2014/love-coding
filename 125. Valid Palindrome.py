class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        return s == s[::-1]

s = Solution()
print(s.isPalindrome("abc Ba"))