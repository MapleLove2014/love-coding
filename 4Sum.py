class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = {}
        nums = sorted(nums)
        for i in range(len(nums) - 3):
            threeSumResult = self.threeSum(nums[i+1:], target - nums[i])
            if threeSumResult:
                for triple in threeSumResult:
                    quadruplet = [nums[i]]
                    quadruplet.extend(triple)
                    result[str(quadruplet)] = quadruplet
        return list(result.values())

    def threeSum(self, nums, target):
        # assume nums are ordered
        result = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                middleSum = nums[i] + nums[j] + nums[k]
                if middleSum == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif middleSum > target:
                    k -= 1
                else:
                    j += 1
        return result

s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))