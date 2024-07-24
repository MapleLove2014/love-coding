class Solution:
    def maxProfit(self, prices) -> int:
        p = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                p += prices[i] - prices[i-1]
        return p
s = Solution()
print(s.maxProfit([7,1,3,5,6,1]))
print(s.maxProfit([5,4,3,2,1]))