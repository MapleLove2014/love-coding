class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        prev = float('-inf')


        for i in range(len(nums)):
            if nums[i] > prev:
                if i == len(nums)-1:
                    return i
                elif nums[i]>nums[i + 1]:
                    return i
                prev = nums[i]
        return -1

    def log2n(self, nums):

        def find(nums, i, j):
            if i == j:
                return i
            mid = (i + j) // 2
            if nums[mid] > nums[mid + 1]:
                return find(nums, i, mid)
            return find(nums, mid + 1, j)
        return find(nums, 0, len(nums)-1)

    def findPeakElement3(self, nums: list[int]) -> int:
        if not nums or len(nums) == 1:
            return 0 if nums else -1
        p = -2**31
        n = nums + [-2**31]
        for i in range(len(n)):
            if n[i] < p:
                return i - 1
            p = n[i]
    def findPeakElement2(self, nums: list[int]) -> int:
        l = 0
        h = len(nums) - 1
        while l < h:
            mid = l + (h-l)//2
            if nums[mid] > nums[mid + 1]:
                h = mid
            else:
                l = mid + 1
        return h
