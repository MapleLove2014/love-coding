class Solution:
    def partition(self, s: str):
        dp = [[False] * len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i+1][j-1]:
                        dp[i][j] = True

        results = []
        def lookup(i, s, dp, result, results):
            if i == len(s):
                results.append(result)
                return
            for j in range(i, len(s)):
                if dp[i][j]:
                    lookup(j + 1, s, dp, result + [s[i:j+1]], results)

        lookup(0, s, dp, [], results)
        return results

s = Solution()
print(s.partition("aab"))
print(s.partition("a"))
