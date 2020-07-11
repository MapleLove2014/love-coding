class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        sortedNums = sorted(nums)
        result = 1 << 31 
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while k > j:
                loopSum = sortedNums[i] + sortedNums[j] + sortedNums[k]
                if abs(target - loopSum) < abs(target - result):
                    result = loopSum
                if loopSum > target:
                    k -= 1
                elif loopSum < target:
                    j += 1
                else:
                    return target
        return result
            
s = Solution()    
print(s.threeSumClosest([-1,2,1,-4], 1))
print(s.threeSumClosest([0,2,1,-3], 1))
