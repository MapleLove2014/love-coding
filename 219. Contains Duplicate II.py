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
    def containsNearbyDuplicate2(self, nums: list[int], k: int) -> bool:
        # nums[i] == nums[j] and abs(i - j) <= k.
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = []
            m[nums[i]].append(i)
        for idx in m.values():
            for i in range(1, len(idx)):
                if idx[i] - idx[i-1] <= k:
                    return True
        return False
            