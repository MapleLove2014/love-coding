class Solution:
    def combinationSum3(self, k: int, n: int):
        
        def find(k, n, used, result):
            if k > n:
                return
            if n == 0 and k == 0:
                result.append(list(used))
                return
            start = 1 if len(used) == 0 else used[-1]
            for i in range(start, 10):
                if i in used:
                    continue
                if i <= n:
                    used.append(i)
                    find(k - 1, n - i, used, result)
                    used.pop()
            

        result = []
        find(k, n, [], result)
        return result
s = Solution()
print(s.combinationSum3(3, 9))
print(s.combinationSum3(9, 45))