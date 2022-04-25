import sys

class Solution:
    def coinChange(self, coins, amount):
        if not coins or not amount:
            return 0
        f = [ -1 ] * (amount + 1)
        for i in range(amount + 1):
            minI = sys.maxsize
            for coin in coins:
                if coin == i:
                    minI = 1
                elif coin < i and f[i-coin] != -1:
                    minI = min(minI if minI != -1 else sys.maxsize, f[i-coin] + 1)
                else:
                    minI = -1 if minI == sys.maxsize else minI
            f[i] = minI
        return f[-1]

s = Solution()
print(s.coinChange([1,2,5], 11))
print(s.coinChange([186,419,83,408], 6249))