class Solution:
    def minCostClimbingStairs(self, cost):
        costs = [0] * len(cost)
        costs[0] = cost[0]
        costs[1] = cost[1]
        for i in range(2, len(cost)):
            costs[i] = min(costs[i-2], costs[i-1]) + cost[i]
        return min(costs[-1], costs[-2])
s = Solution()
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(s.minCostClimbingStairs([0, 0, 0, 1]))
print(s.minCostClimbingStairs([10, 15, 20]))