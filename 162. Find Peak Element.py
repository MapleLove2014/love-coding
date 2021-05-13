class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        prev = float('-inf')


        for i in range(len(nums)):
            if nums[i] > prev:
                if i == len(nums)-1:
                    return i
                elif nums[i]>nums[i + 1]:
                    return i
                prev = nums[i]
        return -1

    def log2n(self, nums):

        def find(nums, i, j):
            if i == j:
                return i
            mid = (i + j) // 2
            if nums[mid] > nums[mid + 1]:
                return find(nums, i, mid)
            return find(nums, mid + 1, j)
        return find(nums, 0, len(nums)-1)
