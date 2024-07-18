class Solution:
    def combine(self, n: int, k: int):
        def com(start, end, k, prefix):
            result = []
            if k == 0:
                return [prefix]
            if k > end - start + 1 or start > end:
                return []
            takeResult=com(start + 1, end, k - 1, prefix + [start])
            skipResult=com(start + 1, end, k, prefix)
            return result + takeResult + skipResult
        return com(1, n, k, [])
s = Solution()
print(s.combine(4, 2))

