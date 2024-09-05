class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # [1,3,1] 
        # [3,0,6,1,5]
        c = sorted(citations)
        n = len(citations)
        h = 0
        for i in range(len(c)):
            ch = min(n-i, c[i])
            h = max(ch, h)
        return h
s = Solution()
print(s.hIndex([5,0,6,1,3]))
print(s.hIndex([1,3,1]))

