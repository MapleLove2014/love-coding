class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start + 1) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return start


            # 1 2  4  6
            # 0 1 2 3 4 5

    def searchInsert2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        less = left
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                less = mid
                left = mid + 1
        return less
