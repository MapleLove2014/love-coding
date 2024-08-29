class Solution:
    def summaryRanges(self, nums):
        nums = nums + [1+2**31]
        ans = []
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - end > 1:
                ans.append(str(end) if start == end else "{}->{}".format(str(start), str(end)))
                start = nums[i]
                end = nums[i]
            elif nums[i] - end == 1:
                end = nums[i]
        return ans
s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))