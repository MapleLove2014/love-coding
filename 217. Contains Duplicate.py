from operator import truediv


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        n = sorted(nums)
        for i in range(0, len(n) - 1):
            if n[i] == n[i + 1]:
                return True
        return False