class Solution:
    def subsets(self, nums):
        if not nums or len(nums) == 0:
            return [[]]

        def doSubset(numsLeft, k, subset, results):
            if k == 0:
                results.append(subset)
                return
            # 增加剪枝
            if len(numsLeft) < k:
                return
            for i in range(k):
                doSubset(numsLeft[i+1:], k - i - 1, subset | set(numsLeft[i:i+1]), results)
        results = []
        for i in range(1, len(nums) + 1):
            doSubset(nums, i, set(), results)
        results.append([])
        return results

s = Solution()
print(s.subsets([1,2,3]))