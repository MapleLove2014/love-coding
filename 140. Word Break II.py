class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        dp = [ [] for _ in range(len(s))]
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i] += [-1]
            for j in range(i):
                if (dp[j] and s[j+1:i+1] in wordDict):
                    dp[i] += [j]
        def make(s, ss, dp, i):
            if i < 0:
                return [ss]
            r = []
            for x in dp[i]:
                r += make(s, ss + [s[x+1:i+1]], dp, x)
            return r
                
        if dp[-1]:
            return [ " ".join(reversed(ss)) for ss in make(s, [], dp, len(s)-1)]
        return []

s = Solution()
print(s.wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))
                
