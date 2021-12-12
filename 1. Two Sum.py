class Solution:
    def twoSum(self, nums, target: int):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        
    def twoSum2(self, nums, target: int):
        d = {}
        for i in range(len(nums)):
            left = target - nums[i]
            if left in d:
                return [i, d[left]]
            d[nums[i]] = i


        return []

s = Solution()
print(s.twoSum2([1,2,3], 5))