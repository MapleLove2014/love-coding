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
        result = []
        lookup(sorted(candidates), 0, target, [], result)
        return result

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def comb(nums, target):
            result = []
            for c in nums:
                if c > target:
                    break
                if c == target:
                    result.append([c])
                    break
                subResult = comb(nums, target - c)
                if len(subResult) > 0:
                    for s in subResult:
                        s.append(c)
                        result.append(s)
            return result
        sorted(candidates)
        result = comb(candidates, target)
        sr = [sorted(x) for x in result]
        d = {}
        for ss in sr:
            d["-".join([str(t) for t in ss])] = ss
        
        return d.values()
    
s = Solution()
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
