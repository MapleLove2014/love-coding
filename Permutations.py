class Solution:
    def permute(self, nums):
        if not nums or len(nums) == 0:
            return []
        
        def doPermute(numsLeft, numsChoosen, results):
            if not numsLeft or len(numsLeft) == 0:
                results.append(numsChoosen)
                return
            for i in range(len(numsLeft)):
                doPermute(numsLeft[0:i] + numsLeft[i+1:], numsChoosen + [numsLeft[i]], results)

        results = []
        doPermute(nums, [], results)
        return results

s = Solution()
print(s.permute([1,2,3]))
print(s.permute([0,1]))