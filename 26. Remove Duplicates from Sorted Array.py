class Solution:
    def removeDuplicates(self, nums) -> int:
        
        last = None
        for i in range(len(nums)):
            ii = nums[i]
            if last == nums[i]:
                nums[i] = None
            last = ii
        i=-1 # number start
        j=0 # looking for number
        # 1 None None 2 3 None 4
        while j < len(nums):
            if nums[j] != None:
                nums[i+1]=nums[j]
                i+=1
                j+=1
            else:
                j += 1
        return i+1




