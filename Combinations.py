class Solution:
    def combine(self, n: int, k: int):
        if n < k:
            return []
        if n == k:
            return [[i for i in range(1, n+1)]]

        def doCombine(low, high, k, combination, results):
            if k == 0:
                results.append(combination)
                return
            for i in range(low, high + 1):
                doCombine(i + 1, high, k - 1, combination + [i], results)
        results = []
        doCombine(1, n, k, [], results)
        return results
s = Solution()
print(s.combine(4, 2))
print(s.combine(1, 1))