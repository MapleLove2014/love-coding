class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # dp[0][0] == 0 empty->empty string do not need take any operation
        # dp[i][j] -> substring word1[0...i-1] -> substring word2[0...j-1]
        for i in range(1, len(word2) + 1):
            # convert empty string to substring word2[0...i-1] need i addition
            dp[0][i] = i
        for i in range(1, len(word1) + 1):
            # convert substring word1[0...i-1] to empty string need i deletion
            dp[i][0] = i
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    # no operation needs to take
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i-1][j] + 1:   word1[0...i-2] -> word2[0...j-1], delete character at position i-1 in word1
                    # dp[i][j-1] + 1:   word1[0...i-1] -> word2[0...j-2], insert character at position i in word1
                    # dp[i-1][j-1] + 1: word1[0...i-2] -> word2[0...j-2], replace character at position i-1 in word1
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
                


            

