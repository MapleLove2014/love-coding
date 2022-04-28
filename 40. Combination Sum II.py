class Solution:
    def combinationSum2(self, candidates, target):
        if not candidates or len(candidates) == 0:
            return []
        
        def lookup(candidates, index, target, result, results):

            if target == 0:
                results.append(result)
                return
            if index == len(candidates):
                return
            leftsum = sum(candidates[index:]) 
            if leftsum < target:
                return
            if leftsum == target:
                results.append(list(result) + candidates[index:])
                return
            if candidates[index] <= target:
                copy = list(result)
                copy.append(candidates[index])
                lookup(candidates, index + 1, target - candidates[index], copy, results)
            lookup(candidates, index + 1, target, result, results)


        results = []
        lookup(candidates, 0, target, [], results)
        dedup = set()
        dedupResults = []
        for result in results:
            rs = str(sorted(result))
            if rs not in dedup:
                dedupResults.append(result)
                dedup.add(rs)
        return dedupResults



s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))

print(s.combinationSum2([2,5,2,1,2], 5))

print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))