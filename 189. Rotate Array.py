class Solution:
    def rotate(self, nums, k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            pre = nums[start]
            current = start
            while True:  
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = pre
                pre = temp
                count += 1
                current = next
                if start == current:
                    break
            start += 1
            
    def rotate2(self, nums: list[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2 or k == 0:
            return 
        k = k % len(nums)
        def reverse(nums, i, j):
            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
        
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
            





s = Solution()
print(s.rotate([1,2,3,4,5], 9))
print(s.rotate([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53],82))
print(s.rotate([1,2,3,4,5,6,7], 1))
print(s.rotate([1,2,3], 4))