class Solution:
    def removeDuplicates(self, nums) -> int:
        
        start = 0
        repeat = 0
        for i in range(1, len(nums)):
            if nums[start] != nums[i]:
                nums[start + 1] = nums[i]
                start += 1
                repeat = 0
            else:
                repeat += 1
                if repeat == 1:
                    nums[start + 1] = nums[i]
                    start += 1
        return start + 1


s = Solution()


print(s.removeDuplicates([1,1,1,2,2,3]))