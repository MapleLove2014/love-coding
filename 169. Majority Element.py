class Solution:
    def majorityElement(self, nums) -> int:
        
        pre = None
        count = 0
        for n in sorted(nums):
            if n == pre:
                count += 1
            
                if count > (len(nums)//2):
                    return pre

            else:
                count = 1
                pre = n
        return pre
    def majorityElement2(self, nums: list[int]) -> int:
        count = 1
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
                if count > len(nums)//2:
                    return nums[i]
            else:
                count = 1
        return nums[0]
    def majorityElement3(self, nums: list[int]) -> int:
        can = None
        count = 0
        for n in nums:
            if count == 0:
                can = n
                count += 1
            elif n == can:
                count += 1
            else:
                count -= 1
        return can

s = Solution()
print(s.majorityElement([3,2,3]))