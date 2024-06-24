# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.


class Solution:
    def removeElement2(self, nums: List[int], val: int) -> int:
        i=-1
        for j in range(len(nums)):
            if nums[j] != val:
                i+=1
                nums[i]=nums[j]
        return i+1

    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = -1
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i + 1
