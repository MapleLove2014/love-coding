
def isSorted(nums):
    if not nums:
        return False
    if len(nums) == 1:
        return True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return False
    return True
