class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        end = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                end = i - 1
                break
        if end >= 0:
            for j in range(len(nums)-1, end, -1):
                if nums[j] > nums[end]:
                    swap(nums, end, j)
                    break
        i = end + 1
        j = len(nums) - 1
        while i < j:
            swap(nums, i, j)
            i += 1
            j -= 1
        

s = Solution()
s.nextPermutation([1,3,2])
#s.nextPermutation([2,3,1,3,3])
#s.nextPermutation([3,2,1])