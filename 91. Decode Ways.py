class Solution:
    def numDecodings(self, s):
        n = len(s)
        result = [0] * (n+1)
        result[n-1] = 0 if s[-1] == '0' else 1
        result[n] = 1
        for i in range(n-2, -1, -1):
            firstTwo = int(s[i:i+2])
            if firstTwo >= 10 and firstTwo <= 26:
                result[i] = result[i+2] + result[i+1]
            elif firstTwo <= 9:
                result[i] = 0
            elif firstTwo > 26:
                result[i] = result[i+1]
        return result[0]     

    def numDecodings2(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        if s[0] == "0":
            return 0
        dp[0] = 1

        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i] += dp[i-1]
            if s[i-1] != "0" and int(s[i-1:i+1]) <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        return dp[-1]

s = Solution()
print(s.numDecodings('226') == 3)
print(s.numDecodings('12') == 2)
print(s.numDecodings('10') == 1)
print(s.numDecodings('30') == 0)
print(s.numDecodings('0') == 0)

    

