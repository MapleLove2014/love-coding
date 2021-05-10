class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        def doSearch(nums, i, j, target):
            if i > j:
                return False
            mid = (i + j) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[i]:
                if target < nums[mid] and target >= nums[i]:
                    return doSearch(nums, i, mid - 1, target)
                else:
                    return doSearch(nums, mid + 1, j, target)
            elif nums[mid] < nums[j]:
                if target > nums[mid] and target <= nums[j]:
                    return doSearch(nums, mid + 1, j, target)
                else:
                    return doSearch(nums, i, mid - 1, target)
            else:
                return doSearch(nums, i, mid-1, target) or doSearch(nums, mid+1, j, target)
        return doSearch(nums, 0, len(nums)-1, target)

