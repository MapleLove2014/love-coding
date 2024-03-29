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


