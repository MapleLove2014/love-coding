import sys
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        result = -sys.maxsize
        f = [sys.maxsize] * len(prices)
        for i in range(len(prices)):
            if i == 0:
                f[i] = prices[i]
            else:
                f[i] = min(f[i-1], prices[i-1], prices[i])
            result = max(result, prices[i] - f[i])
        return result
    def maxProfit2(self, prices) -> int:
        buy = 2**31
        p = 0
        for t in prices:
            p = max(p, t - buy)
            buy = min(buy, t)
        return p    

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([6,5,4,3,2,1]))