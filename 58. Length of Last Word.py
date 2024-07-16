class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        end = len(s) - 1
        while end >= 0:
            if s[end] != ' ':
                l += 1
            elif l > 0:
                return l
            end -= 1
        return l
    def lengthOfLastWord(self, s: str) -> int:
        
        l=0
        for ss in reversed(s):
            if ss != " ":
                l += 1
            elif l > 0:
                return l
            
        return l
s = Solution()
print(s.lengthOfLastWord('Hello World'))
print(s.lengthOfLastWord('   fly me   to   the moon  ') == 4)