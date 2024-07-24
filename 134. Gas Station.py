class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost):
            return -1
        g = 0
        index=0
        for i in range(len(gas)):
            # starting from i or continue from preview staring point 
            g += gas[i] - cost[i]
            # can not reach next gas station
            if g < 0:
                index = i+1
                g = 0
        return index




s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))


