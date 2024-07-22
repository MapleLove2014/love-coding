class Solution:
    def numTrees(self, n: int) -> int:
        def nt(i, j):
            if i >= j:
                return 1 
            c = 0
            for k in range(i, j+1):
                l = nt(i, k-1)
                r = nt(k+1, j)
                c += l*r
            return c
        return nt(1, n)
    def numTrees2(self, n: int) -> int:
        # dp[i] : num of trees formed by 1-i sequence
        # dp[i+1] : 1 - i+1    
        # for t in 1 to i+1  
        # left: 1 to t-1    dp[t-1]
        # right t+1 to n  dp[i+1-(t+1) + 1]
        dp = [0] * (n+1)
        dp[0] = 1 # None
        dp[1] = 1 # 1 as head
        for i in range(2, n+1):
            for t in range(1, i+1):
                dp[i] += dp[t-1]*dp[i-(t+1)+1]
        return dp[n]





    

s = Solution()
print(s.numTrees2(4))


            