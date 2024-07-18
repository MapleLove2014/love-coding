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

    def removeDuplicates2(self, nums) -> int:
        if not nums:
            return 0
        i=0 # last result element
        count = 1
        last=nums[0]
        for j in range(1, len(nums)):
            if nums[j] != last:
                last = nums[j]
                count = 1
                nums[i+1] = nums[j]
                i += 1
            elif count < 2:
                nums[i+1] = nums[j]
                i += 1
                count += 1
            elif count >= 2:
                count += 1
        return i + 1

s = Solution()


print(s.removeDuplicates([1,1,1,2,2,3]))