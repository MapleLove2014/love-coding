class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return len(s) == len(t) and sorted(s) == sorted(t)
    

    def isAnagram2(self, s: str, t: str) -> bool:
        return len(s) == len(t) and sorted(s) == sorted(t)