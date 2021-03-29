class Solution:
    def permuteUnique(self, nums):
        if not nums or len(nums) == 0:
            return []
        
        def doPermute(numsLeft, numsChoosen, results):
            if not numsLeft or len(numsLeft) == 0:
                results.append(numsChoosen)
                return
            prevSelected = None
            for i in range(len(numsLeft)):
                if numsLeft[i] == prevSelected:
                    continue
                doPermute(numsLeft[0:i] + numsLeft[i+1:], numsChoosen + [numsLeft[i]], results)
                prevSelected = numsLeft[i]

        results = []
        doPermute(sorted(nums), [], results)
        return results

s = Solution()
print(s.permuteUnique([1,1,2]))
print(s.permuteUnique([3, 3, 0, 3]))