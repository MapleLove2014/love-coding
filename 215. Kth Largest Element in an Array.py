class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def qs(nums, i, j):
            
            l = i - 1
            h = j + 1
            mid = i + (j - i) // 2
            pivot = nums[mid]
            while True:
                l += 1
                while nums[l] < pivot:
                    l += 1
                h -= 1
                while nums[h] > pivot:
                    h -= 1
                if l < h:
                    nums[l], nums[h] = nums[h], nums[l]
                else:
                    return h
        def qsw(nums, i, j, k):
            if i < j:
                index = qs(nums, i, j)
                kth = len(nums) - k
                if index >= kth:
                    qsw(nums, i, index, k)
                else:
                    qsw(nums, index + 1, j, k)
        qsw(nums, 0, len(nums) - 1, k)
        return nums[len(nums)-k]

s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))



