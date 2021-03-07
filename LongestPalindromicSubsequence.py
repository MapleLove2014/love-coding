class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]

s = Solution()
print(s.longestPalindromeSubseq('bbbab'))
print(s.longestPalindromeSubseq('cbbd'))
