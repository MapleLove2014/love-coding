class Solution:
    def wordBreak(self, s, wordDict):
        print('处理新任务：{}'.format(s))
        if not s or  not wordDict or len(wordDict) == 0:
            return False
        minLen = len(min(wordDict, key=len))
        maxLen = len(max(wordDict, key=len))
        if len(s) < minLen:
            return False
        if len(s) == minLen and s in wordDict:
            return True

        result = [-1] * len(s)
        self.doIt(s, wordDict, 0, result, maxLen)
        return result[0]

    def doIt(self, s, wordDict, i, result, maxLen):
        if i >= len(s):
            return False
        if result[i] != -1:
            return result[i]
        yes = False
        for j in range(1, maxLen + 1):        
            if yes or i+j > len(s):
                break
            self.doIt(s, wordDict, i + j, result, maxLen)
            if s[i:i+j] in wordDict:
                yes |= True if i+j == len(s) else result[i+j]   
        result[i] = yes
        print('完成{}计算'.format(i))
        return result[i]

s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]) == True)
print(s.wordBreak("applepenapple", ["apple", "pen"]) == True)
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False)
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == False)



        
        