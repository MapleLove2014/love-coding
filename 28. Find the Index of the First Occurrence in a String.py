# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    # hello ll
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            j =  0
            while j < len(haystack) and j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
            if j == len(needle):
                return i
        return -1