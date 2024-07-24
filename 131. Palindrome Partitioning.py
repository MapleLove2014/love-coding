class Solution:
    def partition(self, s: str):
        def b(i, s, ps):
            if i == len(s):
                return [ps] if ps else []
            r = []
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    r += b(j + 1, s, ps + [s[i:j+1]])
            return r
        return b(0, s, [])
s = Solution()
print(s.partition("aab"))