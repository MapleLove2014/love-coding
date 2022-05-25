from curses.ascii import SO


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        dr = {}
        for i in range(len(s)):
            sc = s[i]
            tc = t[i]
            if sc in d:
                if d[sc] != tc:
                    return False
            elif tc in dr:
                if dr[tc] != sc:
                    return False
            else:
                d[sc] = tc
                dr[tc] = sc
        return True

s = Solution()
print(s.isIsomorphic('title', 'paper'))               
print(s.isIsomorphic('foo', 'bar'))    
print(s.isIsomorphic('badc', 'babc'))               