class Solution:
    def shoppingOffers(self, price, special, needs):
        def shopping(price, special, needs, index):
            if index == len(special):
                return purchaseWithOriginalPrice(price, needs)
            testNeeds = list(needs)
            notUse = False
            for i in range(0, len(special[index]) - 1):
                remain = needs[i] - special[index][i]
                if remain < 0:
                    notUse = True
                    break
                else:
                    testNeeds[i] = remain
            if notUse:
                return shopping(price, special, needs, index + 1)
            return min(shopping(price, special, testNeeds, index) + special[index][-1], 
                shopping(price, special, needs, index + 1))

        def purchaseWithOriginalPrice(price, needs):
            return sum([a * b for a, b in zip(price, needs)])

        return shopping(price, special, needs, 0)

s = Solution()
print(s.shoppingOffers( [2,5], [[3,0,5],[1,2,10]], [3,2]))








































