class Solution:
    def search(self, nums, target: int) -> int:
        
        def doSearch(nums, i, j, target):
            if i > j:
                return -1
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            
            if nums[i] <= nums[mid]:
                if nums[i] <= target and target < nums[mid]:
                    return doSearch(nums, i, mid - 1, target)
                else:
                    return doSearch(nums, mid+1, j, target)
            
            if target > nums[mid] and target <= nums[j]:
                return doSearch(nums, mid+1, j, target)
            
            return doSearch(nums, i, mid - 1, target)

        return doSearch(nums, 0, len(nums)-1, target)

    def search2(self, nums, target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                # left ------ mid is sorted
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                elif target < nums[mid] and target < nums[left]:
                    left = mid + 1
                else:
                    left = mid + 1
            else:
                # mid ----- right is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                elif target > nums[mid] and target > nums[right]:
                    right = mid - 1
                else:
                    right = mid - 1

        return -1

                





s = Solution()

print(s.search2([3,5,1], 3))
print(s.search2([4,5,6,7,0,1,2], 3))

print(s.search([7,8,1,2,3,4,5,6], 2) == 3)

print(s.search([4,5,6,1,2,3], 4) == 0)
print(s.search([4,5,6,1,2,3], 5) == 1)
print(s.search([4,5,6,1,2,3], 6) == 2)
print(s.search([4,5,6,1,2,3], 1) == 3)
print(s.search([4,5,6,1,2,3], 2) == 4)
print(s.search([4,5,6,1,2,3], 3) == 5)
print(s.search([4,5,6,1,2,3], 7) == -1)
print(s.search([4,5,6,1,2,3], 0) == -1)
print(s.search([3,5,1], 3) == 0)