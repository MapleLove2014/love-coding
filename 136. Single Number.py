


class Solution:
    def singleNumber(self, nums) -> int:
        # [2,2,1]
        nums = sorted(nums)
        i = 1
        while(i < len(nums)):
            if nums[i-1] != nums[i]:
                return nums[i-1]
            else:

                i += 2
        return nums[i-1]
    
    def singleNumber2(self, nums: list[int]) -> int:
        xors = 0
        for n in nums:
            xors = xors ^ n
        return xors
s = Solution()
print(s.singleNumber([4,1,2,1,2]))