


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
s = Solution()
print(s.singleNumber([4,1,2,1,2]))