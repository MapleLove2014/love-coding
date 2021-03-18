class Solution:
    def combinationSum(self, candidates, target): 
        def lookup(candidates, index, target, combine, result):
            if target == 0:
                result.append(combine)
                return
            if index >= len(candidates) and target > 0:
                return
                
            if target >= candidates[index]:
                lookup(candidates, index, target - candidates[index], list(combine) + [candidates[index]], result)
            lookup(candidates, index + 1, target, list(combine), result)
        
        sorted(candidates)
        result = []
        lookup(candidates, 0, target, [], result)
        return result

s = Solution()
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
