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

