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
                




            

