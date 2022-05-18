class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        f = [0] * len(prices)
        for i in range(len(prices)):
            profit = 0 if i == 0 else f[i-1]
            for j in range(i-1+1):
                if j < 2:
                    profit = max(profit, prices[i] - prices[j])
                else:
                    profit = max(profit, f[j-2] + prices[i] - prices[j])
            f[i] = profit
        return f[-1]

s = Solution()
print(s.maxProfit([1,2,3,0,2]))
print(s.maxProfit([1,4,2, 8]))