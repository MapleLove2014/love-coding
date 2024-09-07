class Solution:
    def moveZeroes(self, nums: list[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        nzi = -1
        n = len(nums)
        while True:
            while i < n and nums[i] == 0:
                i += 1
            if i == n:
                break
            nzi += 1
            nums[nzi] = nums[i]
            i += 1
        for i in range(nzi+1, n):
            nums[i] = 0
    def moveZeroes2(self, nums: list[int]):
        i = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[i],nums[r] = nums[r], nums[i]
                i += 1

        
s = Solution()
print(s.moveZeroes([0,1,3,0,5]))

            
