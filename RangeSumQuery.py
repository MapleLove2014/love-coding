class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.sums = [None] * len(nums)
        
        for i in range(len(nums)):
            if i== 0:
                self.sums[i] = nums[i]
            else:
                self.sums[i] = self.sums[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0 and j == 0:
            return self.sums[0]
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]



n = NumArray([-2, 0, 3, -5, 2, -1])
print(n.sumRange(0,2))
print(n.sumRange(2,5))
print(n.sumRange(0,5))