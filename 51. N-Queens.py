class Solution:
    def solveNQueens(self, n: int):
        # dp[i]=j i行j列放一个quene -1 表示无
        def solve(dp, i, n):
            if i == n:
                return [[d for d in dp]]
            result=[]
            for j in range(n):
                can=True
                for r in range(i):
                    # r,dp[r] <==> i,j
                    if dp[r] != -1 and ( dp[r] == j or abs(r-i) == abs(dp[r]-j)):
                        can=False
                        break
                if can:
                    dp[i]=j
                    result += solve(dp, i + 1, n)
                    dp[i]=-1

            return result
        d=solve([-1]*n, 0, n)
        x=[]
        for dd in d:
            solu=[]
            for i in range(n):
                row=["."]*n
                row[dd[i]]="Q"
                solu.append("".join(row))
            x.append(solu)
        return x


            
s = Solution()
print(s.solveNQueens(4))




        







