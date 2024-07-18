class Solution:
    def subsets(self, nums):
        def com(nums, i, k, prefix):
            if k == 0:
                return [prefix]
            if len(nums) - i == k:
                return [prefix + nums[i:]]
            if i >= len(nums) or len(nums) - i < k:
                return []
            take=com(nums, i+1, k-1, prefix + [nums[i]])
            skip=com(nums, i+1, k, prefix)
            return take + skip


        result = []
        for c in range(1, len(nums) + 1):
            result += com(nums, 0, c, [])
        return [[]] + result
        
            
s = Solution()
print(s.subsets([1,2,3]))


