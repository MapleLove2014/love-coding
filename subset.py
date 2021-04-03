class Solution:
    # 这个方法最快
    def subsets(self, nums):
        def doSubsets(nums, i):
            if len(nums) == i + 1:
                return [[nums[i]]]
            results = []
            results.append([nums[i]])
            subResults = doSubsets(nums, i+1)
            results.extend(subResults)
            for subResult in subResults:
                results.append([nums[i]] + subResult)
            return results

        return doSubsets(nums, 0) + [[]]

    # leetcode 大神的做法：https://leetcode.com/problems/subsets-ii/discuss/388566/
    def subsets1(self, nums):
        def doSubsets(nums, i, choosen, results):
            if i == len(nums):
                return
            # pick current value
            results.append(choosen + nums[i:i+1])
            doSubsets(nums, i+1, results[-1], results)
            # not pick current value
            doSubsets(nums, i+1, choosen, results)
        results = []
        doSubsets(nums, 0, [], results)
        results.append([])
        return results



    # 逻辑有点错误
    def subsets2(self, nums):
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
print(s.subsets1([1,2,3]))
print(s.subsets2([1,2,3]))