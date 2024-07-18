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
    def search2(self, nums, target: int) -> bool:
        def b(nums, start, end, target):
            if start > end:
                return False


            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            if start == end:
                return False
            # mid ---- end   ordered
            if nums[end] > nums[mid]:
                if target > nums[mid] and target <= nums[end]:
                    return b(nums, mid + 1, end, target)
                else:
                    return b(nums, start, mid - 1, target)
            elif nums[mid] > nums[start]:
                # start ---- mid ordered
                if target >= nums[start] and target < nums[mid]:
                    return b(nums, start, mid - 1, target)
                else:
                    return b(nums, mid + 1, end, target)
            else:
                return b(nums, start, mid - 1, target) or b(nums, mid + 1, end, target)
        return b(nums, 0, len(nums) -1 , target)
    def search3(self, nums, target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while(start <= end):

            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            if(nums[start] == nums[mid] and nums[mid] == nums[end]):
                start += 1
                end -= 1
                continue
            # mid ---- end   ordered
            
            if nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] <= nums[end]:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False

