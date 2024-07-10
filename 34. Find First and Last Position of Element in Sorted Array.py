class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        start = -1
        end = -1
        for i in range(len(nums)):
            n = nums[i]
            if n == target:
                if start < 0:
                    start = i
                    end = i
                else:
                    end = i
            if n > target:
                break
        return [start, end]

    def ologn(self, nums: List[int], target: int) -> List[int]:
        
        def find(nums, i, j, target):
            if i > j or nums[i] > target or target > nums[j]:
                return (-1,-1)
            mid = (i + j) // 2

            if nums[mid] == target:
                leftStart, _ = find(nums, i, mid - 1, target)
                _, rightEnd = find(nums, mid + 1, j, target)
                return (mid if leftStart == -1 else leftStart, mid if rightEnd == -1 else rightEnd)
            if nums[mid] > target:
                return find(nums, i, mid - 1, target)
            else:
                return find(nums, mid+1, j, target)
        start, end = find(nums, 0, len(nums)-1, target)
        return [start, end]

    def searchRange2(self, nums, target: int):
        def search(nums, left, right, target):
            while left <= right:
                mid = int((left + right) / 2)
                if nums[mid] == target:
                    
                    l=search(nums, left, mid - 1, target)
                    r=search(nums, mid + 1, right, target)
                    i=min(l[1], l[2]) if l[0] else mid
                    j=max(r[1], r[2]) if r[0] else mid
                    return [True, i, j]

                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return [False, -1, -1]
            
        return search(nums, 0, len(nums) - 1, target)[1:]