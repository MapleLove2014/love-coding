class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = -1
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i + 1
