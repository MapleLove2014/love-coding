class Solution:
    def majorityElement(self, nums) -> int:
        
        pre = None
        count = 0
        for n in sorted(nums):
            if n == pre:
                count += 1
            
                if count > (len(nums)//2):
                    return pre

            else:
                count = 1
                pre = n
        return pre

s = Solution()
print(s.majorityElement([3,2,3]))