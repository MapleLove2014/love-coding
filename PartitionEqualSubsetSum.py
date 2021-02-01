'''
Solution: https://afteracademy.com/blog/partition-equal-subset-sum
'''

class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        return self.hasSumDPSpace(nums, total // 2)

    def hasSum(self, nums, targetSum):
        if targetSum == 0:
            return True
        if targetSum < 0:
            return False
        if not nums or len(nums) == 0:
            return False
        return self.hasSum(nums[1:], targetSum) or self.hasSum(nums[1:], targetSum-nums[0])
    
    def hasSumDP(self, nums, targetSum):
        mem = [[False] * (targetSum + 1) for _ in range(len(nums) + 1)]
        mem[0][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(targetSum + 1):
                if j == 0:
                    mem[i][j] = True
                else:
                    if j - nums[i-1] >= 0:
                        mem[i][j] = mem[i-1][j-nums[i-1]]
                    mem[i][j] = mem[i][j] or mem[i-1][j]
        return mem[len(nums)][targetSum]

    def hasSumDPSpace(self, nums, targetSum):
        mem = [False] * (targetSum + 1)
        mem[0] = True
        for i in range(1, len(nums) + 1):
            for j in range(targetSum, -1, -1):
                if j - nums[i-1] >= 0:
                    mem[j] = mem[j - nums[i-1]] or mem[j]
        return mem[targetSum]



s = Solution()
assert s.canPartition([1,5,11,5]) == True, '[1,5,11,5]可以拆分'
assert s.canPartition([1,2,3,5]) == False, '[1,2,3,5]不能拆分'
assert s.canPartition([2,2,2,2]) == True, '[2,2]可以拆分'