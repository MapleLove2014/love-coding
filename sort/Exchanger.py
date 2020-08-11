def exchange(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp