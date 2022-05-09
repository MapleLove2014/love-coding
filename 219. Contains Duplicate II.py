class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in m:
                if i - m[n] <= k:
                    return True
            m[n] = i
        return False  
            