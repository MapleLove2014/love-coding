class Solution:
    def subsetsWithDup(self, nums):
        def doSubset(nums, i, choosen, results, picked):
            if i == len(nums):
                return
            # 判断是否能pick当前元素，需要满足一下条件之一：
            # 1. i == 0
            # 2. nums[i-1] != nums[i]
            # 3. nums[i-1] == nums[i] and picked=True
            if i == 0 or nums[i-1] != nums[i] or picked:
                results.append(choosen + nums[i:i+1])
                doSubset(nums, i+1, results[-1], results, True)
            # 不pick当前元素
            doSubset(nums, i+1, choosen, results, False)

        results = []
        # 初始的这个pick可以随便填，已经有i==0的前置条件。过了0之后，这个值就有真的的含义了
        doSubset(sorted(nums), 0, [], results, True)
        results.append([])
        return results


s = Solution()
print(s.subsetsWithDup([1,2,2]))