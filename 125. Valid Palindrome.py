class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        return s == s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        ss = [t for t in filter(lambda c: (ord(c)>=97 and ord(c) <= 122) or (ord(c)>=48 and ord(c) <= 57), s.lower())]
        return ss == ss[::-1]
s = Solution()
print(s.isPalindrome("abc Ba"))