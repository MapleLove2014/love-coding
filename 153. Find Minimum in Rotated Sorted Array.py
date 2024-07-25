class Solution:
    def findMin(self, nums: List[int]) -> int:
        


        def find(nums, i, j):
            if i == j - 1 or i == j:
                return min(nums[i], nums[j])
            if nums[i] < nums[j]:
                return nums[i]
            mid = (i + j) // 2
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            if nums[i] < nums[mid]:
                return find(nums, mid + 1, j)
            return find(nums, i, mid - 1)
            
        return find(nums, 0, len(nums)-1)
    def findMin2(self, nums: list[int]) -> int:
        l = 0
        h = len(nums) - 1
        m = 2**31
        while l <= h:
            mid = (l + h) // 2
            m = min(m, nums[mid])
            if nums[mid] >= nums[l]:
                # l -- mid ordered
                m = min(m, nums[l])
                l = mid + 1
            elif nums[mid] <= nums[h]:
                # mid -- h ordered
                m = min(m, nums[mid])
                h = mid - 1
        return m
