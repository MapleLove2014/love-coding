class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        i = -1
        j = -1
        k = len(nums)
        p = 0
        while p < k:
            if nums[p] == 0:
                if j < 0:
                    i += 1
                    p += 1
                else:
                    swap(nums, p, i + 1)
                    i += 1
            elif nums[p] == 1:
                if j < 0:
                    j = p
                    p += 1
                else:
                    j += 1
                    p += 1
            else:
                swap(nums, p, k-1)
                k -= 1
    def sortColors2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
        def partition(nums, low, high):
            
            mid = low + (high - low) // 2
            pivot = nums[mid]
            low -= 1
            high += 1
            while True:
                low += 1
                while nums[low] < pivot:
                    low += 1
                high -= 1
                while nums[high] > pivot:
                    high -= 1
                # 1,2,3,5,8,7,6,5
                if low >= high:
                    return high
                nums[low],nums[high] = nums[high], nums[low]

        def quick(nums, low, high):
            if low < high:
                pivotIndex = partition(nums, low, high)
                quick(nums, low, pivotIndex)
                quick(nums, pivotIndex + 1, high)
        quick(nums, 0, len(nums) - 1)
                



            

