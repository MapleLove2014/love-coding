class Solution:
    def restoreIpAddresses(self, s: str):
        
        def search(s, i, prefix):
            if i >= len(s):
                return [prefix] if len(prefix) == 4 else []
            if len(s) - i > (4 - len(prefix)) * 3:
                return []
            r = []
            r += search(s, i + 1, prefix + [s[i]])
            if s[i] != "0" and i < len(s) - 1:
                r += search(s, i + 2, prefix + [s[i:i+2]])
                r += search(s, i + 3, prefix + [s[i:i+3]]) if i < len(s) - 2 and int(s[i:i+3]) <= 255 else [] 
            return r
        return [ ".".join(x) for x in search(s, 0, [])]
                
                
s = Solution()
print(s.restoreIpAddresses("25525511135"))


