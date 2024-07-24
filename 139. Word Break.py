class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i] = True
                continue
            for j in range(i):
                if (dp[j] and s[j+1:i+1] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]
s = Solution()
print(s.wordBreak("a", ["a"]))
print(s.wordBreak("applepenapple", ["apple","pen"]))
print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

            


            
                