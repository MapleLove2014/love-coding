class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        h = len(numbers) - 1
        while l < h:
            s = numbers[l] + numbers[h]
            if s == target:
                return [l + 1, h + 1]
            elif s > target:
                h -= 1
            else:
                l += 1
