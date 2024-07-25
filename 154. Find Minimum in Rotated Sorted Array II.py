class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        h = len(nums) - 1
        m = 2**31
        while l <= h:
            mid = (l + h) // 2
            m = min(m, nums[mid])
            while nums[mid] == nums[l] and nums[mid] == nums[h] and l < mid and h > mid:
                l += 1
                h -= 1
            if nums[mid] >= nums[l]:
                # l -- mid ordered
                m = min(m, nums[l])
                l = mid + 1
            elif nums[mid] <= nums[h]:
                # mid -- h ordered
                m = min(m, nums[mid])
                h = mid - 1
        return m
s = Solution()
print(s.findMin([5,5,5,5,5]))

print(s.findMin([4,5,6,7,1,2,3,4]))
            
