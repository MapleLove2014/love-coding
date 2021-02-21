class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        if not strs or len(strs) == 0:
            return 0
        if m == 0 and n == 0:
            return 0
        return self.finding(strs, m, n, [])
        
    def finding(self, strs, m, n, accepted):
        if m < 0 or n < 0:
            return 0
        if m == 0 and n == 0:
            return len(accepted)
        if len(strs) == 0:
            return len(accepted)
        s = strs[0]
        zeros = 0
        ones = 0
        for c in s:
            if c == '0':
                zeros += 1
            else:
                ones += 1
        acceptedFirst = [i for i in accepted]
        acceptedFirst.append(s)
        return max(self.finding(strs[1:], m - zeros, n - ones, acceptedFirst), self.finding(strs[1:], m, n, accepted))

    def dp(self, strs, m: int, n: int):
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]


s = Solution()
print(s.findMaxForm(["10","0001","111001","1","0"], m = 5, n = 3))
print(s.findMaxForm(["10","0001","111001","1","0"], m = 3, n = 4))
print(s.dp(["10","0001","111001","1","0"], m = 5, n = 3))
print(s.dp(["10","0001","111001","1","0"], m = 3, n = 4))


        